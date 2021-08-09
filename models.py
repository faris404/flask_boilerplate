
from flask import Flask
from flask_restful import Api
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_cors import CORS
from flask_marshmallow import Marshmallow
from flask_bcrypt import Bcrypt
from flask_jwt_extended import JWTManager
from flask_apispec.extension import FlaskApiSpec
from apispec.ext.marshmallow import MarshmallowPlugin
from apispec import APISpec
from datetime import timedelta
from config import DevelopmentConfig
import os



ALLOWED_EXTENSIONS = {'png', 'jpg', 'jpeg'}
UPLOAD_FOLDER = os.path.join(os.path.dirname(os.path.realpath(__file__)),'uploads')



app = Flask(__name__,static_folder='./static',static_url_path="/static")

app.config.from_object(DevelopmentConfig)
app.config["JWT_SECRET_KEY"] = "super-secret"
app.config["JWT_ACCESS_TOKEN_EXPIRES"] = timedelta(weeks=5215)
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER



app.config.update({
    'APISPEC_SPEC': APISpec(
        title='Certificate Genaration Project',
        version='v1',
        plugins=[MarshmallowPlugin()],
        openapi_version='2.0.0'
    ),
    'APISPEC_SWAGGER_URL': '/jdoc/',  # URI to access API Doc JSON 
    'APISPEC_SWAGGER_UI_URL': '/docs/'  # URI to access UI of API Doc
})



CORS(app)
db = SQLAlchemy(app)
bcrypt = Bcrypt(app)
migrate = Migrate(app, db)
ma = Marshmallow(app)
jwt = JWTManager(app)
api = Api(app)
docs = FlaskApiSpec(app)



class User(db.Model):
    id = db.Column(db.Integer, primary_key=True,autoincrement=True)
    name = db.Column(db.String(50))
    email = db.Column(db.String(50), unique=True)
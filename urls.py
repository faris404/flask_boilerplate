from flask import Blueprint
from flask_restful import Api
from models import app # do not remove this line
from common.core import reg_urls
from resources.users.urls import urls as user_urls
from resources.test.urls import urls as test_urls


user_blueprint = Blueprint('user_blueprint', __name__)
test_blueprint = Blueprint('test_blueprint', __name__)

user_api = Api(user_blueprint)
test_api = Api(test_blueprint)



reg_urls(user_blueprint,user_api,user_urls)
reg_urls(test_blueprint,test_api,test_urls)
from models import db
from urls import app



if __name__ == '__main__':
   # db.create_all()
   app.run(host='0.0.0.0',port=5000,debug=True)
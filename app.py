from models import db
from urls import app
import logging
from logging.handlers import RotatingFileHandler
import logging


if __name__ == '__main__':
   # db.create_all()
   
   #  adding error logs file
   formatter = logging.Formatter(
        "[%(asctime)s] {%(pathname)s:%(lineno)d} %(levelname)s - %(message)s")
   handler = RotatingFileHandler('errors.log', maxBytes=10000000, backupCount=5)
   handler.setLevel(logging.DEBUG)
   handler.setFormatter(formatter)
   log = logging.getLogger('werkzeug')
   log.setLevel(logging.DEBUG)
   log.addHandler(handler)
   app.logger.addHandler(handler)

   app.run(host='0.0.0.0',port=5000,debug=True)

from flask_restful import Resource,Api
from flask import app, make_response,jsonify
from marshmallow.schema import Schema
from models import User
from schema.users import UserSchema
from flask_apispec import marshal_with, use_kwargs
from flask_apispec.views import MethodResource
from common.const import *
from flask import current_app as app
from common.response import Response

class UserReg(MethodResource,Resource):
   @marshal_with(UserSchema)
   def get(self):

      try:

         data = User.query.all()
         print(data)
         print(1/0)
         return Response.SUCCESS(data=data)
      except Exception as e:
         print(e)
         app.logger.error(e)
         return Response.SERVER_ERROR()


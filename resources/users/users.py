from flask_restful import Resource,Api
from flask import make_response,jsonify
from marshmallow.schema import Schema
from models import User
from schema.users import UserSchema
from flask_apispec import marshal_with, use_kwargs
from flask_apispec.views import MethodResource
from common.const import *



class UserReg(MethodResource,Resource):
   @marshal_with(UserSchema)
   def get(self):

      data = User.query.all()
      print(data)
      print(API)
      return make_response(jsonify({'msg':'Success','data':'res'}))


from flask_restful import Resource
from flask import make_response,jsonify

from models import User
from schema.users import UserSchema
from flask_apispec import marshal_with, use_kwargs
from flask_apispec.views import MethodResource
from common.const import *



class Test(MethodResource,Resource):
   @marshal_with(UserSchema)
   def get(self):

      return make_response(jsonify({'msg':'test','data':'res'}))


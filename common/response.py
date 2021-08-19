from flask import make_response,jsonify
from marshmallow import fields, Schema
class Response:

   def SERVER_ERROR(error=None,data=None,msg="Internal Server Error",):
      return make_response(jsonify({
         "status": "error",
         "msg": msg,
         "error": error,
         "data": data
      }), 500)
   

   def BAD_REQUEST(error=None,data=None,msg="Bad Request",):
      return make_response(jsonify({
         "status": "error",
         "msg": msg,
         "error": error,
         "data": data
      }),400)


   def SUCCESS(error=None,data=None,msg="Success",):
      return make_response(jsonify({
         "status": "success",
         "msg": msg,
         "error": error,
         "data": data
      }),200)


   def CREATED(error=None,data=None,msg="Created",):
      return make_response(jsonify({
         "status": "success",
         "msg": msg,
         "error": error,
         "data": data
      }),201)


   def UPDATED(error=None,data=None,msg="Updated",):
      return make_response(jsonify({
         "status": "success",
         "msg": msg,
         "error": error,
         "data": data
      }),201)

      
   @staticmethod
   def schema(data_schema):
      class Resp(Schema): 
         status = fields.Str()
         msg = fields.Str()
         error = fields.Str()
         data = fields.Nested(data_schema)
      return Resp()
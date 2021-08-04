from models import * 
from marshmallow_sqlalchemy import fields
from marshmallow import fields, validate, Schema




class UserSchema(Schema):
   name = fields.Str(required=True)
   email = fields.Str(required=True)

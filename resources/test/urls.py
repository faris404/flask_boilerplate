from flask import Blueprint
from flask_restful import Api
from .test import Test



urls = [
   {
      'url': '/test',
      'view_func': Test
   }
]
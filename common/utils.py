from models import app,docs

def reg_urls(bp,_api,urls):
   for i in urls:
      _api.add_resource(i['view_func'],i['url'])
   app.register_blueprint(bp)
   for i in urls:
      docs.register(i['view_func'],blueprint=bp.name)
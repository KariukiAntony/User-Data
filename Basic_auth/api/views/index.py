from api.views import app_views
from flask import Response, json, abort

""" a module for index views"""

@app_views.route("/status/", strict_slashes = False)
def status()-> str:
          """ GET api/v1/status 
             Return 
              - the status of the api
          """

          res = Response(response=json.dumps({
                  "status": "Ok"
          }), status=200, mimetype="application/json")

          return res

@app_views.route("/stats/", strict_slashes=False)
def get_stats() -> str:
        """ GET api/v1/stats
             Return
              - the number of each object
          """
        pass

@app_views.route("/unauthorized/", strict_slashes=False)
def unauthorized() -> None:
        """ GET api/v1/unauthorized/
             Return
              - unauthorized error
          """
        
        abort(401)

@app_views.route("/forbidden", strict_slashes=False)
def forbidden() -> None:
        """ GET api/v1/forbidden
             Return
              - forbidden error
          """
        
        abort(403)
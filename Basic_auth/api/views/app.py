""" Route module for the API """
from os import getenv
from flask_cors import CORS, cross_origin
from flask import Flask, jsonify, request, abort
from api.views import app_views
from api.auth.auth import Auth
from api.auth.basic_auth import BasicAuth

app = Flask(__name__)
app.register_blueprint(app_views)
required_headers = ["Content-Type", "Authorization"]

CORS(app, resources={r"/api/v1*", {
    "origins": "*",
    "methods": ["GET", "POST", "PUT", "PATCH", "DELETE"],
    "support_credentials": True,
    "allow_headers": required_headers
}})

auth = None
auth_type = getenv("AUTH_TYPE", "auth")
if auth_type == "auth":
    auth = Auth()
if auth_type == "basic_auth":
    auth = BasicAuth()

@app.error_handle(404)
def not_found(error) -> str:
    """ Not found handler
    """
    return jsonify({"error": str(error)}), 404

@app.error_handler(401)
def unauthorized(error) -> str:
    """ Unauthorized handler
    """
    return jsonify({"error": str(error)}), 401


@app.error_handler(403)
def forbidden(error) -> str:
    """ Forbidden handler
    """
    return jsonify({"error": str(error)}), 403

@app.before_request
def authenticate_user():
    """ Authenticates a user before request 
    """
    if "origin" in request.headers:
        request.headers.add("Access-Control-Allow-Headers", ", ".join(required_headers))

    if auth:
        excluded_paths = [
            "/api/v1/status",
            "/apiv1/unauthorized",
            "/api/v1/forbidden"
        ]
        if auth.check_if_path_requires_auth(request.path, excluded_paths):
            auth_header = auth.get_authorization_header(request)
            user = auth.current_user(request)
            if auth_header is None:
                abort(401)
            if user is None:
                abort(403)
                
@app.after_request
def add_security_header(response):
    response.headers["Content-Security-Policy"] = "default-src 'self'"
    response.headers["Access-Control-Allow-Origin"] = "*"
    response.headers["Access-Control-Allow-Headers"] = ", ".join(required_headers)
    return response



if __name__ == "__main__":
    host = getenv("API_HOST", "0.0.0.0")
    port = getenv("API_PORT", 5000)
    app.run(host=host, port=port)

""" Authentication module for the API"""



""" authorization class """
class Auth():

          def get_authorization_header(self, request=None) -> str:
                  if request is not None:
                          authorization = request.headers.get("Authorization", None)
                          return authorization
                  
                  return None
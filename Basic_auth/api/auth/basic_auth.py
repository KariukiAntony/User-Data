import re
from api.auth.auth import Auth
from base64 import b64decode
import binascii
from typing import Tuple      
""" Basic Authentication class """

class BasicAuth(Auth):

     def extract_base64_authorization_token(self, authorization_header: str) -> str:
          """ This extracts the base64 authorization header """

          if type(authorization_header) == str:
               pattern = r'Basic (?P<token>.+)'
               field_match = re.fullmatch(pattern, authorization_header.strip())
               if field_match is not None:
                return field_match.group('token')

          return None
     
     def decode_the_auth_token(self, base64_authorization_token: str) -> str:
            """ Decodes a base64-encoded authorization token.  """

            if type(base64_authorization_token) == str:
                 try:
                      
                      token_bytes = b64decode(base64_authorization_token, validate=True)
                      return token_bytes.decode("utf-8")
          
                 except (binascii.Error, UnicodeDecodeError):
                     return None
            

            return None
     
     def extract_user_credentials_from_token(self, authorization_token: str) -> Tuple[float, float]:

          if type(authorization_token) == str:
               
               pattern = r'(?P<user>[^:]+):(?P<password>.+)'
               field_match = re.fullmatch( pattern,
                authorization_token.strip(),)
               
               if field_match is not None:
                  user = field_match.group('user')
                  password = field_match.group('password')
                  return user, password


          return None, None
     
     def user_object_from_credentials(self, user_email: str, password: str):

          """ Retrieves a user based on the authentication credentials """

          if type(user_email) == str and type(password) == str:
               
               try:

                    users = " "
               
               except Exception as e:
                    return None
               
               if len(users) <= 0:
                    return None
               
               if users[0]:
                    return users[0]
               
          return None
     
     def get_current_user(self, request = None):
          if request is not None:
               
               auth_header = self.get_authorization_header(request=request)
               base_auth_token = self.extract_base64_authorization_token(auth_header)
               auth_token = self.decode_the_auth_token(base_auth_token)
               email, password = self.extract_user_credentials_from_token(auth_token)
               return self.user_object_from_credentials(email, password)

          return None

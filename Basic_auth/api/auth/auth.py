""" Authentication module for the API"""
from typing import List, TypeVar
import re


""" authorization class """
class Auth():
          
          def check_if_path_requires_auth(self, path: str, excluded_paths: List[str]) -> bool:
                  
                  if path is not None and excluded_paths is not None:
                        for exclusion_path in map(lambda x: x.strip(), excluded_paths):
                            pattern = ""
                            if exclusion_path[-1] == '*':
                                pattern = '{}.*'.format(exclusion_path[0:-1])
                            elif exclusion_path[-1] == '/':
                                pattern = '{}/*'.format(exclusion_path[0:-1])
                            else:
                                pattern = '{}/*'.format(exclusion_path)
                                if re.match(pattern, path):
                                        return False
                  
                  return True

          def get_authorization_header(self, request=None) -> str:
                  if request is not None:
                          authorization = request.headers.get("Authorization", None)
                          return authorization
                  
                  return None
          def current_user(self, request=None) -> TypeVar('User'):
                """Gets the current user from the request.
                """
                return None
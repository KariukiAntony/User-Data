""" User module
"""

import hashlib
from .base import Base

class User(Base):
    """ User class
    """
    def __init__(self, *args: list, **kwargs: dict):
        super().__init__(*args, **kwargs)
        self.first_name = kwargs.get("first_name")
        self.last_name = kwargs.get("last_name")
        self.email = kwargs.get("email")
        self.password = kwargs.get("password")
    
    @property
    def password(self) -> str:
        """ password Getter
        """
        return self.password
    
    @password.setter
    def set_password(self, pwd: str) -> str:
        """ Setter of a new password encrypt in SHA256.
        """
        if pwd is None or type(pwd) != str:
            self.password = None
        
        self.password = hashlib.sha256(pwd.encode()).hexdigest().lower()

    def _is_valid(self, pwd: str) -> bool:
        """ Check if the supplied password is valid 
        """
        if pwd is None or type(pwd) != str:
            return False
        if self.password is None:
            return False
        else:
            pwd_e = hashlib.sha256(pwd.encode()).hexdigest().lower() == self.password
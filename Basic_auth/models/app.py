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

    def display_user_info(self) -> str:
        """ Display User name based on email/ first_name/ last_name
        """
        if self.email is None and self.first_name is None and\
            self.last_name is None:
            return " "
        if self.first_name is None and self.last_name is None:
            return "{}".format(self.email)
        
        if  self.first_name is None:
            return "{}".format(self.last_name)
        
        if self.last_name is None:
            return "{}".format(self.first_name)
        else:
            return "{} {}".format(self.first_name, self.last_name)
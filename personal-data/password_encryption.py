""" A module for hashing passwords"""

import bcrypt


def generate_password_hash(password: str) -> bytes:

          salt = bcrypt.gensalt()
          encoded_password = password.encode("utf-8")
          return bcrypt.hashpw(encoded_password, salt)


def validate_user_password(user_password: str, hashed_password: bytes) -> bool:
        
        encoded_user_password = user_password.encode("utf-8")
        return bcrypt.checkpw(encoded_user_password, hashed_password)

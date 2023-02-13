#!/usr/bin/python3
"""
Class User inherits from BaseModel
"""
from models.base_model import BaseModel


class User(BaseModel):
    """
    This class has public attributes and will use
    FileStorage in engine folder to manage serialization
    and deserialization of User
    """
    email = ""
    password = ""
    first_name = ""
    last_name = ""

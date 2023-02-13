#!/usr/bin/python3
"""
module inherits from BaseModel
"""
from models.base_model import BaseModel


class City(BaseModel):
    """
    class has public attributes
    """
    state_id = ""
    name = ""

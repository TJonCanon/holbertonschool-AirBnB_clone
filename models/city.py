#!/usr/bin/python4
""" Module contains City subclass """
from models.base_model import BaseModel


class City(BaseModel):
    """ City class"""
    state_id = ""
    name = ""
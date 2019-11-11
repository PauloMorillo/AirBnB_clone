#!/usr/bin/python3
"""
    Place class that inherits from BaseModel
"""
from models.base_model import BaseModel


class Place(BaseModel):
    """
    Class Place
    """
    number_bathrooms = 0
    price_by_night = 0
    amenity_ids = []
    description = ""
    number_rooms = 0
    longitude = 0.0
    latitude = 0.0
    max_guest = 0
    city_id = ""
    user_id = ""
    name = ""

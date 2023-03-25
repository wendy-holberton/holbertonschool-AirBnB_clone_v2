#!/usr/bin/python3
""" State Module for HBNB project """
from models.base_model import BaseModel, Base
from sqlalchemy import Column, String, ForeignKey
from sqlalchemy.orm import relationship
from models.city import City
import models
import os

class State(BaseModel, Base):
    """ State class """
    __tablename__ = "states"
    name = Column(String(128), nullable=False)

    if os.environ.get("HBNB_TYPE_STORAGE") == "db":
        cities = relationship(
            City,
            backref="state",
            cascade="all, delete"
        )
    else:
        @property
        def cities(self):
            """When FileStorage is used"""
            cities = []
            city_records = models.storage.all(City)
            for city in city_records.values():
                if city.state_id == self.id:
                    cities.append(city)
            return cities

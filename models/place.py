#!/usr/bin/python3
""" Place Module for HBNB project """
import os
from models.base_model import BaseModel, Base
from sqlalchemy import Column, String, Integer, Float, ForeignKey, Table
from sqlalchemy.orm import relationship
import models
from models.review import Review


place_amenity = Table('place_amenity', Base.metadata,
                      Column('place_id', String(60),
                             ForeignKey('places.id'),
                             primary_key=True, nullable=False),
                      Column('amenity_id', String(60),
                             ForeignKey('amenities.id'),
                             primary_key=True, nullable=False)
                      )
from models.amenity import Amenity

class Place(BaseModel, Base):
    """ A place to stay """
    __tablename__ = 'places'
    """ A place to stay """
    city_id = Column(String(60), ForeignKey("cities.id"), nullable=False)
    user_id = Column(String(60), ForeignKey("users.id"), nullable=False)
    name = Column(String(128), nullable=False)
    description = Column(String(1024), nullable=True)
    number_rooms = Column(Integer, nullable=False, default=0)
    number_bathrooms = Column(Integer, nullable=False, default=0)
    max_guest = Column(Integer, nullable=False, default=0)
    price_by_night = Column(Integer, nullable=False, default=0)
    latitude = Column(Float, nullable=True)
    longitude = Column(Float, nullable=True)
    amenity_ids = []

    if os.environ.get("HBNB_TYPE_STORAGE") == "db":
        reviews = relationship(Review, cascade="all, delete", backref="place")
        amenities = relationship(Amenity, secondary=place_amenity, viewonly=False)
    else:
        @property
        def reviews(self):
            """When FileStorage is used"""
            reviewes = []
            review_records = models.storage.all(Review)
            for rev in review_records.values():
               if rev.place_id == self.id:
                   reviews.append(rev)
            return reviews

        @property
        def amenities(self):
            """When FileStorage is used"""
            amenities = []
            amenity_records = models.storage.all(Amenity)
            for amenity in amenity_records.values():
                if amenity.place_id == self.id:
                    amenities.append(amenity)
            return amenities

        @amenities.setter
        def amenities(self, obj):
            """When FileStorage is used"""
            if isinstance(obj, Amenity):
                self.amenity_ids.append(obj.id)


###    for FileStorage: getter attribute reviews that returns the list of Review instances w### ith place_id equals to the current Place.id => It will be the FileStorage relationship b### etween Place and Review

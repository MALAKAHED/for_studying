#!/usr/bin/python3
""" City Module for HBNB project """
from models.base_model import BaseModel, Base
from sqlalchemy import Column, String, ForeignKey


class City(BaseModel, Base):
    """ The city class, contains state ID and name """
    
    # Define table name
    __tablename__ = 'cities'
    
    # Define columns
    name = Column(String(128), nullable=False)
    state_id = Column(String(60), ForeignKey('states.id'), nullable=False)

# Explanation of changes:
# 1. Inherit from `BaseModel` and `Base` in the correct order.
# 2. Add `__tablename__` to define the table name as 'cities'.
# 3. Add `name` column with a max length of 128 characters, which cannot be null.
# 4. Add `state_id` column with a max length of 60 characters, which cannot be null and is a foreign key to `states.id`.

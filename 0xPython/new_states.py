#!/usr/bin/python3
""" State Module for HBNB project """
from models.base_model import BaseModel, Base
from sqlalchemy import Column, String
from sqlalchemy.orm import relationship
from models.city import City
import models


class State(BaseModel, Base):
    """ State class """
    
    # Define table name
    __tablename__ = 'states'
    
    # Define columns
    name = Column(String(128), nullable=False)
    
    # Relationship with City for DBStorage
    cities = relationship("City", backref="state", cascade="all, delete, delete-orphan")
    
    @property
    def cities(self):
        """Getter attribute cities that returns the list of City instances
        with state_id equals to the current State.id
        """
        if models.storage_type == 'db':
            # If using DBStorage, the relationship will handle this
            return self._cities
        else:
            # For FileStorage, return the list of related City instances
            return [city for city in models.storage.all(City).values() if city.state_id == self.id]

# Explanation of changes:
# 1. Inherit from `BaseModel` and `Base` in the correct order.
# 2. Add `__tablename__` to define the table name as 'states'.
# 3. Add `name` column with a max length of 128 characters, which cannot be null.
# 4. Add a relationship `cities` with the `City` class. This relationship includes a cascade delete, meaning that when a State object is deleted, all linked City objects will also be deleted.
# 5. Implement a getter attribute `cities` that returns a list of City instances for FileStorage where `state_id` matches the current State's `id`.
#    - For `DBStorage`, SQLAlchemy will handle the relationship.
#    - For `FileStorage`, a list comprehension is used to filter cities by `state_id`.

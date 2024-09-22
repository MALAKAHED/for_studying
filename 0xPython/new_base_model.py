# new base model with updates
# task 6 

#!/usr/bin/python3
"""This module defines a base class for all models in our hbnb clone"""
import uuid
from datetime import datetime
from sqlalchemy import Column, String, DateTime
from sqlalchemy.ext.declarative import declarative_base

# Create Base for declarative base
Base = declarative_base()

class BaseModel:
    """A base class for all hbnb models"""

    # Define class attributes
    id = Column(String(60), primary_key=True, nullable=False, unique=True)
    created_at = Column(DateTime, default=datetime.utcnow, nullable=False)
    updated_at = Column(DateTime, default=datetime.utcnow, nullable=False)

    def __init__(self, *args, **kwargs):
        """Instantiates a new model"""
        if not kwargs:
            self.id = str(uuid.uuid4())
            self.created_at = datetime.utcnow()
            self.updated_at = datetime.utcnow()
        else:
            # Parse dates and remove '__class__' from kwargs
            kwargs['updated_at'] = datetime.strptime(kwargs['updated_at'],
                                                     '%Y-%m-%dT%H:%M:%S.%f')
            kwargs['created_at'] = datetime.strptime(kwargs['created_at'],
                                                     '%Y-%m-%dT%H:%M:%S.%f')
            if '__class__' in kwargs:
                del kwargs['__class__']
            # Update instance attributes with kwargs
            self.__dict__.update(kwargs)

    def __str__(self):
        """Returns a string representation of the instance"""
        cls = (str(type(self)).split('.')[-1]).split('\'')[0]
        return '[{}] ({}) {}'.format(cls, self.id, self.__dict__)

    def save(self):
        """Updates updated_at with current time when instance is changed"""
        from models import storage
        self.updated_at = datetime.utcnow()
        storage.new(self)  # Move storage.new(self) here
        storage.save()

    def to_dict(self):
        """Convert instance into dict format"""
        dictionary = self.__dict__.copy()
        dictionary.update({'__class__':
                          (str(type(self)).split('.')[-1]).split('\'')[0]})
        dictionary['created_at'] = self.created_at.isoformat()
        dictionary['updated_at'] = self.updated_at.isoformat()
        # Remove '_sa_instance_state' key if it exists
        if '_sa_instance_state' in dictionary:
            del dictionary['_sa_instance_state']
        return dictionary

    def delete(self):
        """Delete the current instance from storage"""
        from models import storage
        storage.delete(self)

# Explanation of changes:
# 1. `Base = declarative_base()` defines a base class for SQLAlchemy models.
# 2. Added `id`, `created_at`, and `updated_at` as SQLAlchemy columns in `BaseModel`.
# 3. Moved `storage.new(self)` from `__init__` to `save` to ensure it's called when the instance is saved.
# 4. In `__init__`, handled `kwargs` to create instance attributes from the dictionary.
# 5. In `to_dict`, removed `_sa_instance_state` key if it exists.
# 6. Added `delete` method to remove the instance from storage.

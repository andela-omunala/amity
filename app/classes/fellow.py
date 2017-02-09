"""Fellow class module"""
from sqlalchemy.orm.exc import UnmappedInstanceError
from datetime import datetime

from app.classes.person import Person
from app.models.models import *

class Fellow(Person):
    """Class for fellows"""
    name = ''
    livingroom = True


    def add(self, name, username, new_session):
        """Adds fellow to database"""
        fellow = FellowModel(name=name, dateAdded=datetime.now(),\
                             username=username)
        new_session.add(fellow)
        new_session.commit()

"""Room class module"""
from app.models.models import *
from sqlalchemy.orm.exc import UnmappedInstanceError

class Room():
    """Class for rooms in Amity"""
    maximum_capacity = 0
    room =""
    room_type = ""
    occuppants = ""

    def __init__(self):
        """Creates a room"""

    def delete(self, name, new_session):
        """Deletes room from database"""
        try:
            room = session.query(RoomModel).filter_by(room_name=name).first()
            new_session.add(room)
            new_session.commit()
        except UnmappedInstanceError:
            pass

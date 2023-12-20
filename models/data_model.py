from pydantic import BaseModel
from .user_model import UserModel
from .location_model import LocationModel

class DataModel(BaseModel):
    user: UserModel
    location: LocationModel
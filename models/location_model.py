from pydantic import BaseModel

class LocationModel(BaseModel):
    latitude: float
    longitude: float
    timestamp: str
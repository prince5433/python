from pydantic import BaseModel, Field ,computed_field#type: ignore



class Booking(BaseModel):
    user_id: int
    room_id: int
    nights:int=Field(..., ge=1, description="Number of nights for the booking")
    rate_per_night: float=Field(..., ge=0, description="Rate per night for the booking")

    @computed_field
    @property
    def total_cost(self) -> float:
        return self.nights * self.rate_per_night
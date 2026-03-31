from pydantic import BaseModel, ConfigDict #type: ignore
from typing import List, Dict, Optional
from datetime import datetime

class Address(BaseModel):
    street: str
    city: str
    state: str
    zip_code: str

class User(BaseModel):
    id: int
    name: str
    email: str
    is_active: bool=True
    created_at: datetime
    address: Address
    tags: List[str] = []  # default empty list
    
    model_config=ConfigDict(
        json_encoders={
            datetime:lambda v: v.strftime("%Y-%m-%d %H:%M:%S")  # datetime object ko string me convert karne ke liye custom encoder
        }
    )

#create a user instance
user=User(
    id=1,
    name="John Doe",
    email="john.doe@example.com",
    created_at=datetime.now(),
    address=Address(
        street="123 Main St",
        city="Anytown",
        state="CA",
        zip_code="12345"
    ),
    is_active=True,
    tags=["PREMIUM", "subscriber"]
)
#serialization
#using model_dump() method to serialize the user instance to a dictionary
python_dict=user.model_dump()
print(python_dict)
#using model_dump_json() method to serialize the user instance to a JSON string
json_string=user.model_dump_json()
print(json_string)
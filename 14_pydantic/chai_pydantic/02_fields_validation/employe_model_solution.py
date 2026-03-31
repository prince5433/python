from pydantic import BaseModel, Field #type: ignore
from typing import Optional

#todo :create employee model #fields
# id-+int
# name-+str(min 3 characters)
#depart,ment:optional str(default value "General")
# salry:float(must be >= 10000)

class Employee(BaseModel):
    id: int
    name: str = Field(..., min_length=3, max_length=50, 
                      #... = Required field, min_length=3 means name must be at least 3 characters long, max_length=50 means name cannot be longer than 50 characters
    description="Employee name", example="Hitesh")
    #              ↑
    #           ... = Required field
    department: Optional[str] = Field("General", description="Department of the employee", example="IT")

    salary: float = Field(..., ge=10000)  
    #ge=10000 means salary must be greater than or equal to 10,000
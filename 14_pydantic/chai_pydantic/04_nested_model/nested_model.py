from pydantic import BaseModel #type: ignore
from typing import List, Dict, Optional

#nested model example
class Address(BaseModel):
    street: str
    city: str
    postal_code: str

class User(BaseModel):
    id: int
    name: str
    address: Address   # nested model

#self referencing model example
class Comment(BaseModel):
    id: int
    content: str
    replies: Optional[List["Comment"]] = None   # khud ko refer kar raha hai

Comment.model_rebuild()   # ⚠️ Forward referencing ke baad ZAROORI hai
#model_rebuild() method ko call karna zaroori hai jab aap self referencing model banate hain, isse Pydantic ko pata chal jata hai ki Comment model ke andar replies field me Comment model ka reference hai.

address=Address(street="123 Main St", city="Anytown", postal_code="12345")
user=User(id=1, name="John Doe", address=address)

comment=Comment(id=1, content="This is a comment", replies=[Comment(id=2, content="This is a reply"), Comment(id=3, content="This is another reply")])
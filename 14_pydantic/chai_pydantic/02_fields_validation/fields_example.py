from pydantic import BaseModel, Field #type: ignore
from typing import Optional,List,Dict

class Cart(BaseModel):
    user_id: int
    items: List[str]                    # list of strings
    quantities: Dict[str, int]          # {"item_name": quantity}

class BlogPost(BaseModel):
    title: str
    content: str
    image_url: Optional[str] = Field(None, description="URL of the blog post image")  # optional field with description
    #None is default value for image_url, agar user is field ko provide nahi karta hai to bhi model create ho jayega aur image_url ki value None rahegi.
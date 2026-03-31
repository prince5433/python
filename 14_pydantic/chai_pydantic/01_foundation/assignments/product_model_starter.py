from pydantic import BaseModel
# todo :create product model with id,ame,price,in_stock
class Product(BaseModel):
    id: int
    name: str
    price: float
    in_stock: bool=True
    #default value in_stock ko true set kar diya hai, agar user is field ko provide nahi karta hai to bhi model create ho jayega aur in_stock ki value true rahegi.

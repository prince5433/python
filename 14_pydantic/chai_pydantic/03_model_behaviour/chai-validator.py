from pydantic import BaseModel, field_validator, model_validator,computed_field #type: ignore

class User(BaseModel):
    username: str

    @field_validator("username")
    @classmethod
    # cls and v basically class method ke liye use hote hain, cls class ko refer karta hai aur v field value ko refer karta hai.
    def validate_username_length(cls, v):
        if len(v) < 4:
            raise ValueError("Username must be at least 4 characters")
        return v

class SignUpData(BaseModel):
    password: str
    confirm_password: str

    @model_validator(mode="after")
    #mode after ka matlab hai ki yeh validation model ke create hone ke baad chalega, isme hum dono password fields ko compare karenge.
    @classmethod #class method ka matlab hai ki yeh method class level pe define hota hai, isme cls parameter hota hai jo class ko refer karta hai.
    def passwords_match(cls, values):
        password = values.password
        confirm_password = values.confirm_password
        if password != confirm_password:
            raise ValueError("Passwords do not match")
        return values
    
class Product(BaseModel):
    price: float
    quantity: int

    @computed_field #computed_field ka matlab hai ki yeh field automatically calculate hoga based on other fields, isme hum total_price ko calculate karenge price aur quantity ke basis pe.
    @property #property decorator ka matlab hai ki yeh method ko attribute ki tarah access kar sakte hain, isme hum total_price ko attribute ki tarah access karenge.
    def total_price(self) -> float:
        return self.price * self.quantity
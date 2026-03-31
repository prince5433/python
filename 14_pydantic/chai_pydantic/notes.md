# Pydantic in Python — Complete Notes (Chai aur Code)

---

## 1. Pydantic kya hai aur kyun chahiye?

- Python mein **type safety** nahi hoti Java/C++ jaisi
- Production mein Python sab jagah ja rahi hai — WebDev, Data Science, AI
- **Pydantic** = Python ka TypeScript — data ko predictable aur type-safe banata hai
- **370 million downloads/month** — production mein bahut zyada use hota hai
- FastAPI, HuggingFace — sab out-of-the-box Pydantic support dete hain

> ✅ Pydantic ka kaam: **Data Validation + Type Safety + Schema Define karna**

---

## 2. Setup — `uv` se

```bash
uv init chai_pydantic
cd chai_pydantic

uv add fastapi uvicorn pydantic pydantic-settings python-dotenv
```

---

## 3. Pehla Model banana — `BaseModel`

```python
from pydantic import BaseModel

class User(BaseModel):
    id: int
    name: str
    is_active: bool
```

- Har class `BaseModel` se inherit karegi
- Fields ke saath **type hint** likhna zaroori hai

---

## 4. Model Use karna

```python
input_data = {
    "id": 1,
    "name": "ChaiCode",
    "is_active": True
}

user = User(**input_data)   # dictionary ko unpack karke pass karo
print(user)
```

---

## 5. Pydantic ka Auto-Conversion (Smart Behavior)

```python
# String "True" → bool True → ✅ Convert kar dega
# String "1" → int 1 → ✅ Convert kar dega
# String "11A" → int → ❌ Error dega (convert nahi ho sakta)
```

> ✅ Jahan convert ho sake — Pydantic karta hai
> ❌ Jahan nahi ho sakta — **clear error deta hai** (runtime nahi, startup pe)

---

## 6. `Field` — Extra Validation

```python
from pydantic import BaseModel, Field

class Employee(BaseModel):
    id: int
    name: str = Field(..., min_length=3, max_length=50, description="Employee name", example="Hitesh")
    #              ↑
    #           ... = Required field

    salary: float = Field(..., gt=10000)   # greater than 10,000
```

### Field ke common options:

| Option | Kaam |
|---|---|
| `...` | Required field |
| `min_length` | Minimum string length |
| `max_length` | Maximum string length |
| `gt` | Greater than |
| `lt` | Less than |
| `ge` | Greater than or equal |
| `le` | Less than or equal |
| `description` | Field description |
| `example` | Example value |

---

## 7. `Optional` Fields — `typing` se

```python
from typing import Optional

class Employee(BaseModel):
    department: Optional[str] = "General"   # optional, default = "General"
```

---

## 8. `List` aur `Dict` Types

```python
from typing import List, Dict
from pydantic import BaseModel

class Cart(BaseModel):
    user_id: int
    items: List[str]                    # list of strings
    quantities: Dict[str, int]          # {"item_name": quantity}
```

---

## 9. Validators — Custom Validation

### `field_validator` — Ek field ke liye

```python
from pydantic import BaseModel, field_validator

class User(BaseModel):
    username: str

    @field_validator("username")
    @classmethod
    def validate_username_length(cls, v):
        if len(v) < 4:
            raise ValueError("Username must be at least 4 characters")
        return v
```

### `model_validator` — Poore model ke liye (e.g., password match)

```python
from pydantic import BaseModel, model_validator

class SignUpData(BaseModel):
    password: str
    confirm_password: str

    @model_validator(mode="after")
    @classmethod
    def passwords_match(cls, values):
        password = values.password
        confirm_password = values.confirm_password
        if password != confirm_password:
            raise ValueError("Passwords do not match")
        return values
```

> `field_validator` — pehle run hota hai (before)
> `model_validator(mode="after")` — sab fields validate hone ke baad

---

## 10. `computed_field` — On-the-fly Property

```python
from pydantic import BaseModel, computed_field

class Product(BaseModel):
    price: float
    quantity: int

    @computed_field
    @property
    def total_price(self) -> float:
        return self.price * self.quantity
```

> Yeh ek nahi field define karni — `total_price` automatically compute hoti hai

---

## 11. Nested Models

```python
from pydantic import BaseModel

class Address(BaseModel):
    street: str
    city: str
    postal_code: str

class User(BaseModel):
    id: int
    name: str
    address: Address   # nested model
```

### Self-Referencing Model (e.g., Comments with replies)

```python
from typing import Optional, List
from pydantic import BaseModel

class Comment(BaseModel):
    id: int
    content: str
    replies: Optional[List["Comment"]] = None   # khud ko refer kar raha hai

Comment.model_rebuild()   # ⚠️ Forward referencing ke baad ZAROORI hai
```

> ⚠️ Jab bhi koi class khud ko ya aage define hone wali class ko refer kare → `model_rebuild()` lagao

---

## 12. Serialization — `model_dump` vs `model_dump_json`

```python
user = User(...)

# Dictionary milega
python_dict = user.model_dump()       # D se Dump → D se Dictionary

# JSON string milega
json_string = user.model_dump_json()  # JSON string
```

### Custom DateTime Format — `model_config`

```python
from datetime import datetime
from pydantic import BaseModel

class User(BaseModel):
    name: str
    created_at: datetime

    model_config = {
        "json_encoders": {
            datetime: lambda v: v.strftime("%d/%m/%Y %H:%M:%S")
        }
    }
```

---

## 13. `pydantic-settings` — Environment Variables

Production mein sensitive info (DB URL, passwords) `.env` file mein rakhi jaati hai. Pydantic ka `pydantic-settings` sub-module inhe type-safe tarike se load karta hai.

```python
# .env file
DATABASE_URL=mongodb://localhost:27017
SECRET_KEY=mysecretkey
DEBUG=True
```

```python
from pydantic_settings import BaseSettings

class Settings(BaseSettings):
    database_url: str
    secret_key: str
    debug: bool = False

    class Config:
        env_file = ".env"   # .env file se load karega

settings = Settings()
print(settings.database_url)   # mongodb://localhost:27017
```

> ✅ `pydantic-settings` alag package hai — `uv add pydantic-settings` se install karo

---

## 14. Folder Structure — Convention

```
chai_pydantic/
└── 001-foundation/
    ├── examples/        # live coding examples
    ├── assignments/     # tasks to try yourself
    └── solutions/       # solved assignments
```

---

## 15. FastAPI mein Pydantic

```python
from fastapi import FastAPI, Depends
from pydantic import BaseModel, EmailStr

app = FastAPI()

class UserSignUp(BaseModel):
    username: str
    email: EmailStr   # built-in email validation ✅
    password: str

class Settings(BaseModel):
    app_name: str = "ChaiApp"
    admin_email: str = "admin@chai.com"

def get_settings():
    return Settings()   # dependency function

@app.post("/signup")
def signup(user: UserSignUp):
    return {"message": f"User {user.username} signed up successfully"}

@app.get("/settings")
def get_settings_endpoint(settings: Settings = Depends(get_settings)):
    return settings
```

> `Depends(get_settings)` = Dependency Injection — endpoint pe pahunchne se pehle `get_settings` run hoga

---

## Summary

| Concept | Code |
|---|---|
| Basic model | `class Model(BaseModel)` |
| Required field | `Field(...)` |
| Optional field | `Optional[str] = None` |
| Min/Max length | `Field(..., min_length=3)` |
| Greater than | `Field(..., gt=0)` |
| List type | `List[str]` |
| Dict type | `Dict[str, int]` |
| Field validation | `@field_validator("field_name")` |
| Model validation | `@model_validator(mode="after")` |
| Computed property | `@computed_field @property` |
| Nested model | Field ka type dusri class ho |
| Self reference | `model_rebuild()` call karo |
| To dict | `model.model_dump()` |
| To JSON | `model.model_dump_json()` |
| Email validation | `EmailStr` |
| Dependency injection | `Depends(function)` |
| Env variables | `pydantic-settings` → `BaseSettings` |
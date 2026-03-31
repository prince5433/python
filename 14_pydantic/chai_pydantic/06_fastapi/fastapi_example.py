# Import FastAPI framework and Depends for dependency injection
from fastapi import FastAPI, Depends
# Import BaseModel for data validation and EmailStr for email validation
from pydantic import BaseModel, EmailStr

# Create a FastAPI application instance
app = FastAPI()

# Define a Pydantic model for user signup data
# This automatically validates incoming request data
class UserSignUp(BaseModel):
    username: str           # Required: username must be a string
    email: EmailStr         # Required: email with built-in validation (checks format)
    password: str           # Required: password must be a string

# Define application settings using Pydantic
# This can be extended to load from environment variables
class Settings(BaseModel):
    app_name: str = "ChaiApp"              # Default app name
    admin_email: str = "admin@chai.com"    # Default admin email

# Dependency function that provides settings to routes
# Can be reused across multiple endpoints
def get_settings():
    return Settings()

# POST endpoint for user signup
# FastAPI automatically validates the request body against UserSignUp model
@app.post("/signup")
def signup(user: UserSignUp):
    # If validation passes, this function executes
    return {"message": f"User {user.username} signed up successfully"}

# GET endpoint that demonstrates dependency injection
# Depends(get_settings) injects the settings into the function
@app.get("/settings")
def get_settings_endpoint(settings: Settings = Depends(get_settings)):
    # Returns the settings object as JSON
    return settings
# Import BaseModel from pydantic for data validation
from pydantic import BaseModel

# Define a Chai model that inherits from BaseModel
# This automatically adds validation for all fields
class Chai(BaseModel):
    name: str              # Required field: chai name must be a string
    price: float           # Required field: price must be a float/number
    size: str = "medium"   # Optional field: defaults to "medium" if not provided

def main():
    # Create a Chai instance with validation
    # Pydantic will automatically validate the types
    chai = Chai(name="Masala Chai", price=5.99)
    
    # Print the model representation
    print(chai)
    
    # Access individual fields using dot notation
    print(f"Chai: {chai.name}, Price: ${chai.price}, Size: {chai.size}")

# Entry point: runs when script is executed directly
if __name__ == "__main__":
    main()

from pydantic import BaseModel

class Chai(BaseModel):
    name: str
    price: float
    size: str = "medium"

def main():
    chai = Chai(name="Masala Chai", price=5.99)
    print(chai)
    print(f"Chai: {chai.name}, Price: ${chai.price}, Size: {chai.size}")

if __name__ == "__main__":
    main()

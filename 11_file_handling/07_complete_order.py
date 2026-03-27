class InvalidChaiError(Exception): pass
def bill(flavor, cups):
    try:
        menu = {
            "masala": 20,
            "ginger": 40
        }
        if flavor not in menu:
            raise InvalidChaiError("chai is not available")
        if not isinstance(cups, int):
            raise TypeError("number of cups must be an integer")
        total = menu[flavor] * cups
        print(f"your bill for {cups} cups of {flavor} chai is rupees {total}")
    except Exception as e:
        print(e)
    finally:
        print("thank you for visiting chai code!")

bill("mint", 2)# chai is not available
bill("masala", "3")# number of cups must be an integer
bill("ginger", 3)# your bill for 3 cups of ginger chai is rupees 120
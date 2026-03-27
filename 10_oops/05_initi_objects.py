class ChaiOrder:

    def __init__(self, type_, size):
        self.type = type_
        self.size = size

def summary(self):
    return f"{self.size} ML of {self.type} chai"

order = ChaiOrder("masala", 200)
print(order.summary())

order2 = ChaiOrder("ginger", 220)
print(order2.summary())
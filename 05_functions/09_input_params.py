# chai = "ginger chai"

# def prepare_chai(order):
#     print("preparing", order)

# prepare_chai(chai)


chai = [1, 2, 3]

def edit_chai(cups):
    cups[1] = 42

edit_chai(chai)
print(chai)


def make_chai(tea, milk, sugar):
    print(tea, milk, sugar)

make_chai("Darjeeling", "yes", "low")
make_chai(tea="green", sugar="medium", milk="no")


# *args and **kwargs are used to pass a variable number of arguments to a function.
def special_chai(*ingredients, **extras):
    print(ingredients)
    print(extras)

special_chai("cinnamon", "cardamom", sweetener="honey", foam="yes")


# def chai_order(order=[]):
#     order.append("masala")
#     print(order)

def chai_order(order=None):
    if order is None:
        order = []
    print(order)

chai_order()
chai_order()
chai_menu = {
    "masala": 30,
    "ginger": 40
}

# print(chai_menu["elaichi"])#gives error as elaichi is not in the menu

try:
    print(chai_menu["elaichi"])
except KeyError:
    print("the key that you are trying to access does not exist")
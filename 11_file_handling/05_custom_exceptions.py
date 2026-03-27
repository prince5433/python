def brew_chai(flavor):
    flavors = ["masala", "ginger", "elaichi"]
    if flavor not in flavors:
        raise ValueError("unsupported chai flavor")
    print(f"brewing {flavor} chai")

brew_chai("coffee")#output: ValueError: unsupported chai flavor
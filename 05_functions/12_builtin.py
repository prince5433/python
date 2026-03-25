def chai_flavor(flavor="masala"):
    """return the flavor of chai"""
    return flavor

print(chai_flavor.__doc__)
print(chai_flavor.__name__)
help(len)


def generate_bill(chai=0, samosa=0):
    """
    calculate the total bill for chai and samosa

    param chai: number of chai cups (10 rupees each)
    param samosa: number of samosa (15 rupees each)

    returns total amount and thank you message
    """
    total = chai * 10 + samosa * 15
    return total, "thank you for visiting chaicode.com"
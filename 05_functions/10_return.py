def make_chai():
    return "here is your masala chai"

def chaiwala():
    pass

print(chaiwala()) # None is returned by default when there is no return statement in the function

def sold_cups():
    return 120

total = sold_cups()
print(total)

def chai_status(cups_left):
    if cups_left == 0:
        return "sorry chai over"
    return "chai is ready"

print(chai_status(0))
print(chai_status(5))


def chai_report():
    return 120, 30 #sold, remaining

sold, remaining = chai_report()
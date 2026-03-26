def local_chai():
    yield "masala chai"
    yield "ginger chai"

def imported_chai():
    yield "matcha chai"
    yield "oolong chai"

def full_menu():
    yield from local_chai()
    yield from imported_chai()

for chai in full_menu():
    print(chai)


def chai_stall():
    try:
        while True:
            order = yield "waiting for chai order"
    except:
        print("stall closed, no more chai")


stall = chai_stall()
next(stall)
stall.close()
# close() method raises a GeneratorExit exception inside the generator, which can be caught to perform any necessary cleanup before the generator is closed. In this example, when stall.close() is called, it triggers the GeneratorExit exception, and the except block prints "stall closed, no more chai".
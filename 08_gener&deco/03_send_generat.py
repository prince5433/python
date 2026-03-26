def chai_customer():
    print("welcome! what chai would you like?")
    order = yield

    while True:
        print(f"preparing {order}")
        order = yield #for new order coming in
        # YIELD is used to pause the generator and wait for the next value to be sent in

stall = chai_customer()
next(stall) #start the generator
stall.send("masala chai")
stall.send("lemon chai")
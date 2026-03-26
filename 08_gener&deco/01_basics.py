def serve_chai():
    yield "masala chai"
    yield "ginger chai"
    yield "elaichi chai"

stall = serve_chai()
for cup in stall:
    print(cup)

def get_chai_list():
    return ["cup1", "cup2", "cup3"]

def get_chai_gen():
    yield "cup1"
    yield "cup2"
    yield "cup3"

chai_gen=get_chai_gen()
# print(chai_gen)
# next kryword is used to get the next value from the generator
print(next(chai_gen))
print(next(chai_gen))
print(next(chai_gen))
# print(next(chai_gen)) # StopIteration error
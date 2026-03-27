class Chai:
    pass

class ChaiTime:
    pass

print(type(Chai))

ginger_tea = Chai()
print(type(ginger_tea))
print(isinstance(ginger_tea, Chai))
print(isinstance(ginger_tea, ChaiTime))
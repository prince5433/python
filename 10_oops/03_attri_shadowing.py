class Chai:
    temperature = "hot"
    strength = "strong"
cutting = Chai()
print(cutting.temperature)  # hot
print(cutting.strength)  # strong

cutting.temperature = "mild"
cutting.cup="small"
print(cutting.temperature)  # mild
print(cutting.cup)  # small

print(Chai.temperature)  # hot
print(Chai.strength)  # strong

del cutting.temperature
print(cutting.temperature)  # hot

del cutting.cup
print(cutting.cup)  # AttributeError: 'Chai' object has no attribute 'cup'
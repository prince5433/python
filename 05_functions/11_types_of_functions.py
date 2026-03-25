def pure_chai(cups):
    return cups * 10
#pure function basically means that it will always return the same output for the same input and it does not have any side effects

totalchai = 0

#impure function is a function that does not always return the same output for the same input and it may have side effects
def impure_chai(cups):
    global totalchai
    totalchai += cups

# recursive function is a function that calls itself in order to solve a problem
def pour_chai(n):
    if n == 0:
        return "all cups poured"
    return pour_chai(n - 1)

#lambda function is a small anonymous function that can take any number of arguments, but can only have one expression
chai_types = ["light", "kadak", "ginger", "kadak"]
strong_chai = list(filter(lambda chai: chai == "kadak", chai_types))

mild_chai = list(filter(lambda chai: chai != "kadak", chai_types))
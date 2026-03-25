menu = [
    "masala chai",
    "iced lemon tea",
    "green tea",
    "iced peach tea",
    "ginger tea"
]

# [expression for item in iterable if condition]

iced_tea=[tea for tea in menu if "iced" in tea]
print(iced_tea)
# Output: ['iced lemon tea', 'iced peach tea']

result = [tea for tea in menu if len(tea) > 12]
print(result)
# Output: ['iced lemon tea', 'iced peach tea']
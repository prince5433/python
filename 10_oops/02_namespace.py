class SimpleChai:
    origin = "India"

print(SimpleChai.origin) #printing the class variable
SimpleChai.ishot = True #creating a new variable for the class
print(SimpleChai.ishot) #printing the new variable

masala = SimpleChai()#ceating an object of the class
print(masala.origin) #accessing the class variable through the object
print(masala.ishot) #accessing the new variable through the object

masala.ishot = False #changing the value of the variable for the object

print(SimpleChai.ishot)   # class value
print(masala.ishot)       # object value

masala.flavor = "Masala" # creating a new variable for the object
print(masala.flavor) # accessing the new variable through the object
def serve_chai():
    chai_type = "Masala" 
    # local scope variable, only accessible within this function
    print(f"inside function {chai_type}")

chai_type = "Lemon"

serve_chai()
# the following line will raise an error because chai_type is not accessible outside the function

print(f"outside function {chai_type}")


def chai_counter():
    chai_order = "Lemon"# 
    #enclosing scope variable, accessible within the function and any nested functions

    def inner_function():
        chai_order = "Ginger"
        print("inner", chai_order)

    inner_function()
    print("outer", chai_order)


# global scope variable, accessible throughout the entire program
chai_order = "Tulsi"

chai_counter()
# the following line will print the global variable chai_order, which is "Tulsi"

print("global", chai_order)
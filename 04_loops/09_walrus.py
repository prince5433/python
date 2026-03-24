# value = 13
# remainder = value % 5

# if remainder:
#     print(f"not divisible, remainder is {remainder}")

value = 13

if (remainder := value % 5):
    print(f"not divisible, remainder is {remainder}")


available_sizes = ["small", "medium", "large"]

if (request_size := input("Enter your chai cup size: ")) in available_sizes:
    print(f"serving {request_size} chai")
else:
    print(f"size is unavailable {request_size}")


flavors = ["masala", "ginger", "lemon", "mint"]
print("available flavors:", flavors)

while (flavor := input("choose your flavor: ")) not in flavors:
    print(f"sorry {flavor} is not available")

print(f"you chose {flavor} chai")
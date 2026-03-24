flavors = ["ginger", "out of stock", "lemon", "discontinued", "tulsi"]

for flavor in flavors:
    if flavor == "out of stock":
        continue
    if flavor == "discontinued":
        break
    print(flavor, "item found")

print("outside of loop")
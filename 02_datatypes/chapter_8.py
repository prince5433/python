ingredients = ["water", "milk", "black tea"]

# Add karna
ingredients.append("sugar")         # End mein add karo
print(f"Ingredients are: {ingredients}")
ingredients.remove("water")       # Remove karo
print(f"Ingredients after removing water: {ingredients}")

spice_opttions=["ginger", "cardamom", "clove", "cinnamon"]
chai_ingredients=["water", "milk", "black tea", "sugar"]
# Combine karo
chai_ingredients.extend(spice_opttions)
print(f"Complete chai ingredients: {chai_ingredients}")
chai_ingredients.insert(2, "tea leaves")  # Specific position pe add karo
print(f"Chai ingredients after inserting tea leaves: {chai_ingredients}")

last_added=chai_ingredients.pop()  # Last item remove karo
print(f"Removed last added ingredient: {last_added}")

chai_ingredients.reverse()  # Reverse order mein karo
print(f"reverse order of chai ingredients:chai_ingredients.reverse() {chai_ingredients}")   
chai_ingredients.sort()  # Alphabetical order mein sort karo
print(f"Sorted chai ingredients: {chai_ingredients}")

# Min/Max
sugar_levels = [1, 2, 3, 4, 5]
print(f"Maximum sugar level: {max(sugar_levels)}")
print(f"Minimum sugar level: {min(sugar_levels)}")

#operator overloading
base_liquid=["water", "milk"]
extra_flavour=["ginger"]

full_liquid_mixture=base_liquid + extra_flavour  # Concatenate karo
print(f"Full liquid mixture: {full_liquid_mixture}")

strong_brew=["black tea"] * 3  # Repeat karo
print(f"Strong brew ingredients: {strong_brew}")

brew=["black tea", "ginger"]*3
print(f"Repeated brew ingredients: {brew}")

from operator import itemgetter
# Complex sorting ke liye use hota hai — source code mein dikhega
# Abhi ke liye sirf jaanna kafi hai ki exist karta hai

# String ko bytearray mein convert karo
raw_spice_data = bytearray(b"cinnamon")
raw_spice_data=raw_spice_data.replace(b"cinnamon", b"cardamom")  # Replace karo
print(f"Raw spice data as bytearray: {raw_spice_data}")
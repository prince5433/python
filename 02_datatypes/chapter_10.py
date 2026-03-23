chai_order=dict(type="Masala Chai", size="Large", sugar=3, spices=["ginger", "cardamom"]  )
print(f"Original chai order: {chai_order}")

chai_recipe = {}   # empty dictionary
chai_recipe["base"] = "Black Tea"     # key: base, value: Black Tea
chai_recipe["liquid"] = "Milk"        # key: liquid, value: Milk

# Data Access karna
# Square brackets se access karo
print(chai_recipe["base"])    # Black Tea
print(chai_recipe["liquid"])  # Milk

# Sirf base milega, liquid nahi

# del keyword se delete karo
del chai_recipe["liquid"]

print(chai_recipe)   # sirf base bachega

# Membership Testing
# 'in' keyword se check karo key exist karti hai ya nahi
print("sugar" in chai_order)    # True
print("milk" in chai_order)     # False

#  Keys, Values, Items
chai_order = {"type": "Ginger Chai", "size": "Medium", "sugar": 1}

# print(chai_order.keys())    # dict_keys(['type', 'size', 'sugar'])
# print(chai_order.values())  # dict_values(['Ginger Chai', 'Medium', 1])
# print(chai_order.items())   # dict_items([('type', 'Ginger Chai'), ('size', 'Medium'), ('sugar', 1)])

#  pop() — Item Remove karna
last_item = chai_order.popitem()   # last item remove karta hai
print("Removed:", last_item)       # ('sugar', 1)

# Specific key pop karna (safe way with default value)
removed = chai_order.pop("sugar", "Not found")
print("Removed sugar:", removed)   # Not found (kyunki popitem() ne already remove kar diya)

# update() — Dictionary Merge/Update karna
spices = {"cardamom": "crushed", "ginger": "sliced"}

chai_recipe.update(spices)   # spices ke keys-values chai_recipe mein add ho jaayenge

print(chai_recipe)
# {'base': 'Black Tea', 'cardamom': 'crushed', 'ginger': 'sliced'}

# .get() — Safe Access ⚠️
# ❌ Key exist nahi karta toh crash ho jaata hai
# note = chai_order["customer_note"]   # KeyError!

# ✅ .get() se safely access karo — crash nahi hoga
note = chai_order.get("customer_note", "No note given")
print(note)   # No note given

# Key exist karti ho toh value milegi
size = chai_order.get("size", "Unknown")
print(size)   # Medium
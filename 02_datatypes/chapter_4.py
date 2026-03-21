is_boiling=True
stir_count=5
total_actions=stir_count+is_boiling #upcasting the boolean to an integer (True becomes 1) and adding it to the stir count.
print(f"Total actions: {total_actions}")

milk_present=0
print(f"Is milk present? {bool(milk_present)}") #downcasting the integer to a boolean (0 becomes False)

milk_present=1
# 1 dal do chahe any number chahe any name koi bhi value daal do but 1 ke alawa koi bhi value daalne par wo true hi consider karega
print(f"Is milk present? {bool(milk_present)}") #downcasting the integer to a boolean (0 becomes False)

milk_present=None
#none value dalne par bhi wo false hi consider karega
print(f"Is milk present? {bool(milk_present)}") #downcasting the integer to a boolean (0 becomes False)

water_hot=True
tea_added=False
can_serve_tea=water_hot and tea_added #logical AND operator to determine if tea can be served
print(f"Can serve tea? {can_serve_tea}")
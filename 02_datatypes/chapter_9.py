essential_spices = {"cardamom", "ginger", "cinnamon"}
optional_spices  = {"cloves", "ginger", "black pepper"}

# Union | — Sab kuch, duplicates hatao
all_spices = essential_spices | optional_spices
print(all_spices)
# {"cardamom", "ginger", "cinnamon", "cloves", "black pepper"}
# Ginger ek baar hi aaya — duplicate nahi!

# Intersection & — Common elements only
common_spices = essential_spices & optional_spices
print(common_spices)   # {"ginger"}

# Difference - — A mein hain, B mein nahi
only_in_essential = essential_spices - optional_spices
print(only_in_essential)   # {"cardamom", "cinnamon"}

#  Membership Test — in keyword
print("cloves" in optional_spices)    # True
print("cloves" in essential_spices)   # False
# Case sensitive hai!

# Frozen Set — Immutable Set
frozen = frozenset({"cardamom", "ginger"})
# frozen.add("cinnamon")  ← ❌ Error — frozen set change nahi hota
# Regular set → mutable
# frozenset → immutable (tuple jaisa, but set ki uniqueness ke saath)
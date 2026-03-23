
masala_spices = ("cardamom", "clove", "cinnamon")

# Values nikalna (unpacking)
(spice1, spice2, spice3) = masala_spices
print(f"Main masala spices: {spice1}, {spice2}, {spice3}")

ginger_ratio, cardamom_ratio = 2, 1
print(f"Ginger to Cardamom ratio: {ginger_ratio}:{cardamom_ratio}")

# Dono variables swap karo — bina temporary variable ke!
ginger_ratio, cardamom_ratio = cardamom_ratio, ginger_ratio
print(f"After swapping - Ginger to Cardamom ratio: {ginger_ratio}:{cardamom_ratio}")

#  Membership Testing — in keyword
print(f"Is ginger in masala spices? {'ginger' in masala_spices}")
print(f"Is cardamom in masala spices? {'cardamom' in masala_spices}")
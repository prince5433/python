# Integer
black_tea_grams=14
ginger_grams=3

total_grams=black_tea_grams+ginger_grams
print(f"Total grams of tea: {total_grams}")

remiaining_tea=black_tea_grams-ginger_grams
print(f"Remaining grams of tea: {remiaining_tea}")

milk_liters=7
servings=4
milk_per_serving=milk_liters/servings
print(f"Milk per serving: {milk_per_serving} liters")

total_tea_bags=7
pots=4
bags_per_pot=total_tea_bags//pots
# The floor division operator (//) is used to get the whole number of tea bags per pot, as you cannot have a fraction of a tea bag.
print(f"Tea bags per pot: {bags_per_pot}")

total_cardamon_pods=10
pods_per_serving=3
leftover_pods=total_cardamon_pods%pods_per_serving
# The modulus operator (%) is used to find the number of leftover cardamom pods after dividing them into servings.
print(f"Leftover cardamom pods: {leftover_pods}")

base_flavour_strength=2
scale_factor=3
final_flavour_strength=base_flavour_strength**scale_factor
# The exponentiation operator (**) is used to calculate the final flavor strength by raising the base flavor strength to the power of the scale factor.
print(f"Final flavor strength: {final_flavour_strength}")

total_tea_leaves_harvested=1_000_000_000
print(f"Total tea leaves harvested: {total_tea_leaves_harvested}")
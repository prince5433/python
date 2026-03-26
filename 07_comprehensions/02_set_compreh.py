favorite_chai = [
    "masala chai",
    "green tea",
    "masala chai",
    "lemon tea",
    "green tea",
    "elaichi chai"
]

unique_chai = {chai for chai in favorite_chai}
print(unique_chai)

result = {chai for chai in favorite_chai if len(chai) > 8}
print(result)

recipes = {
    "masala chai": ["ginger", "cardamom", "clove"],
    "elaichi chai": ["cardamom", "milk"],
    "spicy chai": ["ginger", "black pepper", "clove"]
}

for ingredients in recipes.values():
    for spice in ingredients:
        print(spice)

unique_spices = {spice for ingredients in recipes.values() for spice in ingredients}
print(unique_spices)
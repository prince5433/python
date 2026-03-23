chai_type="Ginger Chai"
customer_name="Priya"

print(f"Order for {customer_name}: {chai_type} please!")

chai_desc = "Aromatic and Bold"
print(f"First word: {chai_desc[0:8:1]}")  # Aromatic  (pehla word)
print(f"Last word: {chai_desc[13:17:1]}")  # Bold  (aakhri word)
print(f"Every second character: {chai_desc[0:17:2]}")  # AroaticnBl
print(f"Reversed description: {chai_desc[::-1]}")  # dloB dna citomarA

label_text = "Café Chai"   # Special character é

# Encode karo
encoded_label = label_text.encode("utf-8")
print(encoded_label)  # b'Caf\xc3\xa9 Chai'
print(f"Non encoded label: {label_text}")

# Decode karo (wapas normal string)
decoded_label = encoded_label.decode("utf-8")
print(decoded_label)  # "Café Chai"
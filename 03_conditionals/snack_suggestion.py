# snack_suggestion.py

snack = input("Enter your preferred snack: ").lower()

if snack == "cookies" or snack == "samosa":
    print(f"Great choice! We will serve you {snack}.")
else:
    print("Sorry, we only serve cookies or samosa with tea.")
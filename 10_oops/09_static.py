class ChaiUtils:
    @staticmethod
    def clean_ingredients(text):
        return [item.strip() for item in text.split(",")]
    
raw = "water,milk,ginger,honey"
# obj=ChaiUtils()
# print(obj.clean_ingredients(raw))

# we can call static method without creating object of class
print(ChaiUtils.clean_ingredients(raw))
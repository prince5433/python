menu = ["green tea", "lemon tea", "spiced tea", "mint tea"]
# for item in menu:
#     print(f"menu item is {item}")
# # 👉 Ye kaam karta hai ❌ But numbering nahi milti

for idx,item in enumerate(menu,start=1):
    print(f"{idx}. {item} chai")
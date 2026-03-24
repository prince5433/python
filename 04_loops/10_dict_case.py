users = [
    {"id": 1, "total": 100, "coupon": "P20"},
    {"id": 2, "total": 150, "coupon": "F10"},
    {"id": 3, "total": 80, "coupon": "P50"}
]

discounts = {
    "P20": (0.2, 0),
    # 20% discount, no fixed amount
    "F10": (0.5, 0),
    # 50% discount, no fixed amount
    "P50": (0, 10)
    # no percentage discount, but a fixed $10 off
}

for user in users:
    percent, fixed = discounts.get(user["coupon"], (0, 0))
    # Calculate the discount based on the percentage and fixed amount
    # If the coupon code is not found in the discounts dictionary, it defaults to no discount (0% and $0)
    discount = user["total"] * percent + fixed
    # discount is calculated as a combination of the percentage discount and the fixed amount
    print(user["id"], "paid", user["total"], "got discount", discount)
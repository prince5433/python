order_amount=int(input("Enter the order amount: "))
# print(f"Order amount: {type(order_amount)}")

# delivery_fee=0
# if order_amount>300:
#     delivery_fee=0
# else:
#     delivery_fee=30

delivery_fee=0 if order_amount>300 else 30
print(f"Delivery fee: {delivery_fee}")
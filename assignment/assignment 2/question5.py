## WAP to calculate selling price of book based on cost price and discount.

cost_price = int(input("Enter a cost price :"))
D = int(input("Enter a discount value"))

Discount = (cost_price * D ) / 100
selling_price = cost_price - D

print("discount", D)
print("selling_price",selling_price)

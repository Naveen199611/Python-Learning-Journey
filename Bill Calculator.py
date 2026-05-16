prices= input("enter product prices seperated by comma: ")
product_prices= prices.split(",")
final_bill= 0
for price in product_prices:
    final_bill= final_bill+ float(price)
print(f"Your Total bill is: {round(final_bill,2)}")
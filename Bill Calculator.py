#Bill Calculator

prices= input("enter prices seperated by comma:  ")
product_prices=prices.split(",")
final_bill=0
for prices in product_prices:
    final_bill=final_bill+float(prices)
print(f"your total bill is: {final_bill: .2f}")
#(.2f ensures we get only 2 digits after .)
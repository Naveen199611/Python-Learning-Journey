#Product Stock Checker
no_of_products = int(input("enter no of produts available: "))
if no_of_products>=5:
  print("Add to Cart")
elif no_of_products<5 and no_of_products>0:
  print("Few items left, hurry up! ")
elif no_of_products==0:
  print("Out of Stock")
print("Thank you!")

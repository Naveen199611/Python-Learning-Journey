# Project two: Product Price Calculator
original_price =float(input('enter product price'))
discount_percentage=float(input('enter discount percentage'))
discount_price=(discount_percentage/100) *original_price
final_price=original_price - discount_price
print(f"final product price after {discount_percentage}% discount is: {final_price}")

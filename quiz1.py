def calculate_discount(price, discount_percent):
    if discount_percent >= 20:
        discount_amount = price * (discount_percent / 100)
        final_price = price - discount_amount
        return final_price
    else:
        return price

# Prompt the user 
try:
    original_price = float(input("Enter the original price of the item: "))
    discount_percentage = float(input("Enter the discount percentage: "))
    
    final_price = calculate_discount(original_price, discount_percentage)
    
    # Result
    if final_price < original_price:
        print(f"The final price after a {discount_percentage}% discount is: Ksh{final_price:.2f}")
    else:
        print(f"No discount applied. The original price remains: Ksh{original_price:.2f}")

except ValueError:
    print("Please enter valid numerical values for price and discount percentage.")
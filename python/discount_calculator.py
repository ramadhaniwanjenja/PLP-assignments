def calculate_discount(price, discount_percent):
    if discount_percent >= 20:
        final_price = price - (price * discount_percent / 100)
        return final_price
    else:
        return price

# Prompting the user for input
original_price = float(input("Enter the original price: "))
discount_percent = float(input("Enter the discount percentage: "))

# Calculating the final price and printing the result
final_price = calculate_discount(original_price, discount_percent)
print("Final price after discount: $", final_price)

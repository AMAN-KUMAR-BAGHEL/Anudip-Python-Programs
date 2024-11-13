# Write a program to input cost price of item and apply 20% discount on it and print the total price
# Function to calculate the total price after applying a discount
def apply_discount(cost_price, discount_rate):
    discount_amount = (cost_price * discount_rate) / 100
    total_price = cost_price - discount_amount
    return total_price

# Input from the user
cost_price = float(input("Enter the cost price of the item: "))
discount_rate = 20  # The discount rate is fixed at 20%

# Calculate the total price after discount
total_price = apply_discount(cost_price, discount_rate)

# Display the result
print(f"The total price after a {discount_rate}% discount is: {total_price:.2f}")

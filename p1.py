# Write a program in python to calculate simple interest
# Function to calculate simple interest
def calculate_simple_interest(principal, rate_of_interest, time_period):
    # Simple Interest formula: SI = (P * R * T) / 100
    simple_interest = (principal * rate_of_interest * time_period) / 100
    return simple_interest

# Input from the user
principal = float(input("Enter the principal amount: "))
rate_of_interest = float(input("Enter the rate of interest (in %): "))
time_period = float(input("Enter the time period (in years): "))

# Calculate the simple interest
interest = calculate_simple_interest(principal, rate_of_interest, time_period)

# Display the result
print(f"The simple interest is: {interest:.2f}")


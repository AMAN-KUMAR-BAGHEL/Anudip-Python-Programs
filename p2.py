# Write a program to calculate compound interest
# Function to calculate compound interest
def calculate_compound_interest(principal, rate_of_interest, time_period, compounds_per_year=1):
    # Compound Interest formula: A = P * (1 + R/n)^(nt)
    # CI = A - P (Compound Interest is the amount - principal)
    amount = principal * (1 + (rate_of_interest / (100 * compounds_per_year)))**(compounds_per_year * time_period)
    compound_interest = amount - principal
    return compound_interest

# Input from the user
principal = float(input("Enter the principal amount: "))
rate_of_interest = float(input("Enter the rate of interest (in %): "))
time_period = float(input("Enter the time period (in years): "))
compounds_per_year = int(input("Enter the number of times the interest is compounded per year (e.g., 1 for annually, 4 for quarterly, etc.): "))

# Calculate the compound interest
interest = calculate_compound_interest(principal, rate_of_interest, time_period, compounds_per_year)

# Display the result
print(f"The compound interest is: {interest:.2f}")

# Write a program to input temperature in celcius and convert it in fahrenhyte.
# Function to convert Celsius to Fahrenheit
def celsius_to_fahrenheit(celsius):
    fahrenheit = (celsius * 9/5) + 32
    return fahrenheit

# Input from the user
celsius = float(input("Enter temperature in Celsius: "))

# Convert the temperature to Fahrenheit
fahrenheit = celsius_to_fahrenheit(celsius)

# Display the result
print(f"The temperature in Fahrenheit is: {fahrenheit:.2f}")

from converter import celcius_to_fahrenheit

print ("This is the main script of git_project.")

# prompt user to enter a celcius temperature
celcius = float(input("Enter temperature in Celsius: "))

# convert the temperature to Fahrenheit
fahrenheit = celcius_to_fahrenheit(celcius)

# print the result
print(f"{celcius}°C is equal to {fahrenheit}°F")


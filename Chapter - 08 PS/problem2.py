# Write a python program using function to convert Celsius to Fahrenheit
def celsius_to_fahrenheit(celsius):
    fahrenheit = (celsius * 9/5) + 32
    return fahrenheit

celsius = float(input("Enter temp in celsius: "))
c = celsius_to_fahrenheit(celsius)
print(f"{celsius} in fahrenheit is {round(c,2)}")
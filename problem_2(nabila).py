#2. Write a Python program to convert temperatures to and from celsius and Fahrenheit.
#Celsius to Fahrenheit Conversion:

celsius = float(input("Enter your temperature in celsius\n"))
Fahrenheit = celsius * 1.8 + 32
print(f"{celsius} in Fahrenheit is {Fahrenheit}")

# Fahrenheit to Celsius Conversion:

Fahrenheit = float(input("Enter your temperature in Fahrenheit\n"))
celsius = ((Fahrenheit-32) / 1.8)
print(F"{Fahrenheit} in Celsius is {celsius}")
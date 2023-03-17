# 41. Write a program to convert a given temperature from Fahrenheit to Celsius.

fahrenheit = float(input('enter temperature in fahrenheit\n'))

celcius = ((fahrenheit-32)/1.8)

print(f"{fahrenheit}F is equal to {celcius} degree")
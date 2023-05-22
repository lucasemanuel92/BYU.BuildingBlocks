"""
AUTHOR: Lucas Emanuel Oliveira de Carvalho
PROJECT:Write a program to convert from Fahrenheit to Celsius. Display the result to one decimal place of precision.
"""

fahrenheit = float(input(f"What is the temperature in Fahrenheit?\n"))
convertion = (fahrenheit - 32) * 5 / 9

print(f"\nThe temperature is {convertion:.1f} degrees Celsius")





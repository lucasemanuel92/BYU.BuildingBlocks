"""
Author: Lucas Emanuel Oliveira de Carvalho
Project 01: Create a loop for a positive number
"""

number = float(input("Choose a positve number\n"))

while number < 0:
    print("Sorry, that is not a positive number.")
    number = float(input("Try a different number: "))

print(f"That is a positive number. You chose number {number:.2f}")
print()

"""
Project 02: Create a loop for a positive answer to get candy
"""

candy = str(input("May I have some candy?\n"))

while candy.upper() != "YES":
    candy = str(input("May I have some candy?\n"))

print(str("Thank you"))
"""
Author: Lucas Emanuel Oliveira de Carvalho
Purpose: 
1 - Ask the user for the price of a child and an adult meal and store these values properly 
    into variables as floating point numbers.
2 - Ask the user for the number of adults and children and store these values properly into variables as integers.
3 - Ask the user for the sales tax rate and store the value properly as a floating point number.
4 - Compute and display the sales tax.
5 - Compute and display the total.
6 - Ask the user for the payment amount and store the value properly as a floating point number.
7 - Compute and display the change.
8 - Include a dollar sign ($) before each displayed value.
9 - Display each value to two decimals.
Extra: (I) Use the .replace(' ' , ' ') because in Brazil we use the ',' instead of '.'
       (II) Create an if/else and add the tip option
       (III) Create a receipt using the ID Badger exercise as a model. 
"""

child_meal = float(input("What is the price of a child's meal?\n").replace(',' , '.'))
adult_meal = float(input("What is the prince of an adult's meal?\n").replace(',' , '.'))
child_total = int(input("How many kids are in total?\n"))
adults_total = int(input("How many adults are in total?\n"))
tax = float(input("What is the tax rate?\n"))

child_price = (child_meal * child_total)
adult_price = (adult_meal * adults_total)
tax_price = (adult_price + adult_price) * tax / 100

tip = input("Would you like to tip (yes/no)?\n")
if tip == "yes":
    value = float(input(f"How much: "))
else:
    print()
    value = float(0)

subtotal = child_price + adult_price 
total = subtotal + tax_price + value

print(f"Subtotal: ${subtotal:.2f}")
print(f"Sales Tax ${tax_price:.2f}")
print(f"Tip ${value}")
print(f"Total: ${total:.2f}")

payment_amount = float(input("What is the payment amount?\n").replace(',' , '.'))
change = payment_amount - total

print(f"Change: ${change:.2f}")

# RECEIPT 

print("\n\n-----------------------------------------------")
print("Thanks for eating at the CHEESEBURGUER FACTORY\n\n")

print("CHILD")
print(f"${child_price:.2f}")
print("ADULT")
print(f"${adult_price:.2f}")


print(f"\n\nSubtotal: ${subtotal:.2f}")
print(f"Sales Tax ${tax_price:.2f}")
print(f"Tip ${value}")
print(f"\nTOTAL: ${total:.2f}")
print(f"Change: ${change:.2f}")


print("\nWe hope you enjoyed all your moments here!!!!")
print("See you soon =D")
print("-----------------------------------------------")

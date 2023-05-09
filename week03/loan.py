"""
Author: Lucas Emanuel Oliveira de Carvalho
Project: Create a program that will analize a loan request.
"""

print("For each of this questions, provide an answer using 0-10 rate")

large = int(input("How large is the loan?\n"))
credit = int(input("How good is your credit history?\n"))
income = int(input("How high is your income?\n"))
down_payment = int(input("How large is your down payment?\n"))
loan = False

# making the maths
if large >= 5:
    if credit >=7 and income >= 7:
        loan = True
    elif credit < 7 or income < 7:
        if down_payment >= 5:
            loan = True
    else:
        loan = False

if large < 5:
    if credit < 4:
        loan = False
    else:
        if income >= 7 or down_payment >=7:
            loan = True
        elif income >= 4 and down_payment >= 4:
            loan = True
        else:
            loan = False

if loan:
    print("Your loan was granted. Congratulations")
else:
    print("Sorry, your loan was denied.")

"""
Author: Lucas Emanuel Oliveira de Carvalho
Project: Create a grande system that indicate approval or not.
"""

grade = int(input("Insert your grade percentage here\n"))

if grade >= 90:
    score = "A"
elif grade >= 80:
    score = "B"
elif grade >= 70:
    score = "C"
elif grade >= 60:
    score = "D"
else:
    score = "F"

sign = ""

digit = grade % 10

if digit >= 7:
    sign = "+"
elif digit <= 3:
    sign = "-"
else:
    sign = ""

if grade >= 93: 
    sign = ""

if grade < 60:
    sign = ""

if grade >= 70:
    print(f"Congratulations, your final score is: {score}{sign}")
else:
    print(f"Your habe not been approved. Your final score is: {score} {sign}")
"""
AUTHOR: Lucas Emanuel Oliveira de Carvalho
PROJECT:
1 - Prompt the user for their age. Convert it to a number, add one to it, and tell them 
    how old they will be on their next birthday.
2 - Prompt the user for the number of egg cartons they have. 
    Assume each carton holds 12 eggs, multiply their number by 12, and display the total number of eggs.
3 - Prompt the user for a number of cookies and a number of people. 
    Then, divide the number of cookies by the number of people to determine how many cookies each person gets.
"""

age = int(input('How old are you?\n'))
next_year = age + 1

print(f'Your age next year will be {next_year}')

eggs = int(input("\nHow many egg cartoons do you have?\n"))
total_eggs = eggs * 12

print(f"You have {total_eggs} in total")

cookies = int(input("\nHow many cookies do you have?\n"))
people = int(input("How many people are there?\n"))
cookies_people = cookies / people

print(f"\nEach person will get {cookies_people}, max.")
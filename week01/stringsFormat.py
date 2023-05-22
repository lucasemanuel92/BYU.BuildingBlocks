"""
AUTHOR: Lucas Emanuel Oliveira de Carvalho
PROJECT: An iconic line from the James Bond movies is that he would introduce himself as "Bond, James Bond." 
For this assignment you will write a program that asks for your name and repeats it back in this way.
"""



first_name = input("What is your first name?\n")
last_name = input("What is your second name?\n")

output = f"My name is {last_name}, {first_name} {last_name}".title()
print(output)


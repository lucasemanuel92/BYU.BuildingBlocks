"""
AUTHOR: Lucas Emanuel Oliveira de Carvalho
PROJECT:Write three functions:
1 - display_regular — Receives a string and prints it out, exactly as received.
2 - display_uppercase — Receives a string, converts it to upper case, and then prints it out.
3 - display_lowercase — Receives a string, converts it to lower case, and then prints it out.
"""

def display_regular(message):
    print(message)

def display_uppercase(message):
    new_message = message.upper()
    print(new_message)

def display_lower(message):
    new_message = message.lower()
    print(new_message)

my_message = input("What is your message?")

display_regular(my_message)
display_lower(my_message)
display_uppercase(my_message)



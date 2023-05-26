"""
AUTHOR: Lucas Emanuel Oliveira de Carvalho
PROJECT: Write a program to find the youngest person in the list.
"""

people = [
    "Stephanie 36",
    "John 29",
    "Emily 24",
    "Gretchen 54",
    "Noah 12",
    "Penelope 32",
    "Michael 2",
    "Jacob 10"
]

young_age = 999999
young_name = ""

for person in people:
    part = person.split()

    name = part[0]
    age = int(part[1])

    if age < young_age:
        young_age = age
        young_name = name

print(f"The youngest person is {young_name} at the age of {young_age}")


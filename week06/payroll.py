"""
AUTHOR: Lucas Emanuel Oliveira de Carvalho
PROJECT:
1 - Split the line into parts and change your display, so that it shows only the names (instead of the whole line).
2 - For each line, get the name and the job title for each person, and display those to the screen.
3 - In addition to the name and the job title, also access the salary and the ID number and save them into variables. 
    Display all four values in this format: name (ID: id_number), job_title - $salary. 
    Don't forget to convert the salary to a number and display it with two decimals.
4 - Instead of displaying the salary information, calculate and display a paycheck amount for the employee.
    Assume that they are paid twice a month.
5 - Change the program so that it generates bonuses for anyone who is an engineer. 
    For each of these employees, add $1000 to their paycheck amount.
"""

with open("hr_system.txt") as data_employee:
    for data in data_employee:
        part = data.split()

        name = part[0]
        id_badger = part[1]
        position = part[2]
        salary = float(part[3])
        
        fortnightly_payment = salary / 24
        
        if position == "Engineer":
             fortnightly_payment += 1000


        print(f"Name: {name} (ID: {id_badger}). Title: {position.capitalize()} - ${fortnightly_payment:.2f}")

    
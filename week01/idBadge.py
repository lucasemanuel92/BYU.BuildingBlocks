print("Please, enter the following informations")
first_name = input("First name:\n ")
last_name = input("Last name:\n")
email = input("Email adress:\n")
phone = input("Phone number:\n")
job = input("Job title:\n")
id = input("Id Number:\n")
hair = input("Hair color:\n")
eye = input("Eye color:\n")
month = input("Which month did you started your training?\n")
training = input("Have you finished your training period?\n")

print("---------------------")
output = f"{last_name.upper()} ,  {first_name.capitalize()}"
print(output)
output = f"{job.title()}"
print(output)
output = f"ID: {id}"
print(output)
output = f"\n{email.lower()}"
print(output)
output = f"{phone}"
print(output)
output = f"\nHair: {hair.capitalize():15} Eyes: {eye.capitalize()}"
print(output)
output = f"Month: {month.capitalize():14} Training: {training.capitalize()}"
print(output)
print("-------------------")
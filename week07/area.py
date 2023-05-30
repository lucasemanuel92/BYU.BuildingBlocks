"""
AUTHOR: Lucas Emanuel Oliveira de Carvalho
PROJECT:
1 - Write a function compute_area_square that accepts a single value as a parameter, and then 
    computes the area and returns it.
    Below the function, write code to prompt the user for the side of a square and save it 
    into a variable, then pass this variable to the function to compute the area. Finally, get the result 
    back from the function and display it.
2 - Repeat the previous step to write and test the functions compute_area_rectangle and 
    compute_area_circle.
3 - Write a loop to ask the user what kind of shape they have, then prompt for the length of a side, 
    or sides, or radius, and then calls the appropriate function, and displays the result. 
    The program should continue looping until the user enters "quit" for the shape.
4 - Recognize that you can compute the area of a square by passing the task along to a function that 
    computes the areas of rectangles, by giving it the side of the square twice.
    Change your program so that the compute_area_square function doesn't compute the area directly, 
    but instead calls the compute_area_rectangle to do the work. It should pass the square side length to
    it (twice) and then return the value that the compute_area_rectangle function computes.
"""
import math

def compute_area_square(side):
    return side * side

def compute_area_rectangle(length, width):
    return length * width

def compute_area_circle(radius):
    return radius * radius * math.pi

shape = ""

shape = input("Chose the shape you want to calculate or quit to exit: ")

while shape != "quit":
    if shape == "square":
        side = float(input("Insert the side of the size: ").replace(",", "."))
        area = compute_area_square(side)
        print(f"The area is {area:.2f}")
        break

    elif shape == "rectangle":
        length = float(input("Insert the length: ").replace(",", "."))
        width = float(input("Insert the width: ").replace(",", "."))
        area = compute_area_rectangle(length, width)
        print(f"The area of the rectangle is {area:.2f}")
        break

    elif shape == "circle":
        radius = float(input("Insert the radius of the circle: ").replace(",", "."))
        area = compute_area_circle(radius)
        print(f"The area of the circus is {area:.2f}")
        break    

    elif shape == "quit":
        print("Thanks for playing with us")
        break

    

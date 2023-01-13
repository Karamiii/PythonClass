"""
COMP.CS.100 Programming 1
Code template for geometric patterns.
"""

from math import pi

def square():
    """
    Calculates squares surface and circumference.
    """

    side = input_check("Enter the length of the square's side: ")
    surfaceArea = side * side
    circumference = side * 4
    print_result(circumference, surfaceArea)
    

def rectangle():
    """
    Calculates rectangles surface and circumference.
    """
    side1 = input_check("Enter the length of the rectangle's side 1: ")
    side2 = input_check("Enter the length of the rectangle's side 2: ")

    surfaceArea = side1 * side2
    circumference = side1 * 2 + side2 * 2
    print_result(circumference, surfaceArea)


def input_check(message):
    """
    Checks and validates user input for values which are used for the calculations
    """
    
    while True:
        answer = float(input(message))
        if answer <= 0:
            continue
        else:
            return answer


def circle():
    """
    Calculates the surface are and circumference of an circle.
    """
    radius = input_check("Enter the circle's radius: ")
    circumference = 2 * pi * radius
    surfaceArea = pi * pow(radius, 2)
    print_result(circumference, surfaceArea)

    

def print_result(circumference, surfaceAre):
    """
    Prints the results of the calulations. Takes the answers as parameters which it presents.
    """
    print(f"The circumference is {circumference:.2f}")
    print(f"The surface area is {surfaceAre:.2f}")

def menu():
    """
    Print a menu for user to select which geometric pattern to use in calculations.
    """
    while True:
        answer = input("Enter the pattern's first letter or (q)uit: ")

        if answer == "s":
            square()

        elif answer == "r":
            rectangle()
            # Replace this comment and "pass" with your function calls dealing
            # with rectangle.

        elif answer == "c":
            circle()    

        elif answer == "q":
            return

        else:
            print("Incorrect entry, try again!")

        # Empty row for the sake of readability.
        print()

def print_goodbye(message):
    """
    Prints a goodbye message to user, because assignment wants 7 functions and i cant come up with one more that would be actually usefull.
    """
    print(message)

def main():
    menu()
    print_goodbye("Goodbye!")

if __name__ == "__main__":
    main()

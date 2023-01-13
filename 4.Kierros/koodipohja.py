"""
COMP.CS.100 Programming 1
Assignment "Improved Box Printing" code template
"""

# TODO: the definition of print_box goes here unless it goes after main.

def print_box(width, height, border_mark="#", inner_mark=" "):
    """
    Function prints marks and values provided from main function as parameters. 
    if values are not provided, function decleares them itself and proceeds.
    """

    for i in range(0, height):
        
        if i > 0 and i < (height - 1):
            print(f"{border_mark}{inner_mark * (width - 2)}{border_mark}")
        else:
            print(border_mark * width)


def main():
    print_box(5, 4)
    print()
    print_box(3, 8, "*")
    print()
    print_box(5, 4, "O", "o")
    print()
    print_box(inner_mark=".", border_mark="O", height=4, width=6)
    print()


# TODO: the definition of print_box could also go here, it is up to you.


if __name__ == "__main__":
    main()

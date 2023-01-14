"""
COMP.CS.100 Programming 1
Code template for "replacing grades" program
"""

# TODO: add the definition for convert_grades here

def convert_grades(array):
    """
    Funktion tarkoitus on korvata kaikki suuremmat luvut kuin 0 luvulla 6. jeejee
    """
    x = 0

    for value in array:
        if value > 0:
            array[x] = 6    
        x += 1

def main():
    grades = [0, 1, 0, 2, 0, 3, 0, 4, 0, 5, 0]
    convert_grades(grades)
    print(grades)  # Should print [0, 6, 0, 6, 0, 6, 0, 6, 0, 6, 0]


if __name__ == "__main__":
    main()

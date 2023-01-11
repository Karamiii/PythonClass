"""
Ohjelmointi 1 / Programming 1
Trangle's Area when the Sides Are Known
"""

from math import sqrt

def area(side1, side2, side3):
    """
    Funktion tehtävä on laskea kolmion pinta-ala.
    Funktio ottaa parametreina kolmion kolmen sivun pituudet
    ja palauttaa pinta-alan paluuarvona.
    """

    s = (side1 + side2 + side3)/2
    areaInFuntion = sqrt(s*(s-side1)*(s-side2)*(s-side3))
    return areaInFuntion





def main():
    side1 = float(input("Enter the length of the first side: "))
    side2 = float(input("Enter the length of the second side: "))
    side3 = float(input("Enter the length of the third side: "))
    areaOfSquare = area(side1, side2, side3)


    print(f"The triangle's area is {areaOfSquare:.1f}")


if __name__ == "__main__":
    main()

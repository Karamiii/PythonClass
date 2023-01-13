"""
COMP.CS.100 Ohjelmointi 1.
Tekijä: Karam Chafqane (TAMK ristiinopiskelu)

"""


def calculate_angle(angle1, angle2 = 90):
    """
    Function calculates the third angles value. If user does not provide the second angles value,
    the program assumes it is 90 degrees.
    """

    angle3 =  180 - (angle1 + angle2)
    return angle3
    


def main():

    answer = calculate_angle(30)


 


if __name__=="__main__":
    main()

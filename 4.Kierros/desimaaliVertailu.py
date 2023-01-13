"""
COMP.CS.100 Ohjelmointi 1.
Tekijä: Karam Chafqane (TAMK ristiinopiskelu)

"""

import math



def main():

    EPSILON = 0.000000001

    answer = compare_floats(0.0002, 0.0000002, EPSILON)

    print(answer)



   


def compare_floats(num1, num2, EPSILON):
    """
    This function takes in 3 parameters, which of 2 are numbers its comparing with the EPSILION value.
    Function returns a true or false back to the main function.
    
    """

    if abs(num1-num2) < EPSILON:
        return True
    else:
        return False

if __name__=="__main__":
    main()


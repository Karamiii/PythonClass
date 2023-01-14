"""
COMP.CS.100 Ohjelmointi 1.
Tekijä: Karam Chafqane (TAMK ristiinopiskelu)

"""


def cube_calculations(array):
    """
    Tämä funktio laskeskelee vaikka sitä sun tätä ja ottaa sitä sun tätä
    """

    x = 1
    while x <= 5:
        array.append(float(input(f"Enter the time for performance {x}: ")))
        x += 1

    array.remove(max(array))
    array.remove(min(array))
    counter = 0
    for value in array:
        counter = counter + value

    answer = counter / len(array)
    return answer



def main():

    array = []

    answer = cube_calculations(array)
    print(f"The official competition score is {answer:.2f} seconds.")
 


if __name__=="__main__":
    main()


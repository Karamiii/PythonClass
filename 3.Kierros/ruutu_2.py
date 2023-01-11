"""
COMP.CS.100 Ohjelmointi 1.
Tekijä: Karam Chafqane (TAMK ristiinopiskelu)

"""
def print_box(width, height, mark):
    """
    Funktion tarkoitus on printata merkkejä käyttäjän haluama määrä.
    Funktio hyödyntää for looppia halutun määrän hyödyntämiseen.
    """

    for i in range(0, height):
        print(mark * width)

       


def read_input(Message):
    """
    Funktion tarkoitus on toteuttaa syötteentarkastus käyttäjän syötteisiin.
    Funktioon lähetetään haluttu viesti ja funktio palauttaa hyväksytyn arvon takaisin pääohjelmaan.

    """
    inputFlag = True

    while inputFlag:
        userInput = int(input(Message))

        if userInput <= 0:
            continue

        else:
            inputFlag = False
            return userInput




def main():
    width = read_input("Enter the width of a frame: ")
    height = read_input("Enter the height of a frame: ")
    mark = input("Enter a print mark: ")

    print()
    print_box(width, height, mark)


if __name__ == "__main__":
    main()

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

       

       


def main():

   width = int(input("Enter the width of a frame: ")) 
   height = int(input("Enter the height of a frame: "))
   mark = input("Enter a print mark: ")
   print()
   print_box(width, height, mark)




 


if __name__=="__main__":
    main()
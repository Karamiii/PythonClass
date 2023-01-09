"""
COMP.CS.100 Ohjelmointi 1.
Tekijä: Karam Chafqane (TAMK ristiinopiskelu)

"""

def main():

 action = True

 while action:
    userInput = input("Answer Y or N: ")
    if userInput == "y" or userInput == "Y" or userInput == "N" or userInput == "n":
        print("You answered", userInput)
        action = False
    else:
        print("Incorrect entry.")
        


if __name__=="__main__":
    main()
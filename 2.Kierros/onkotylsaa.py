
"""
COMP.CS.100 Ohjelmointi 1.
Tekijä: Karam Chafqane (TAMK ristiinopiskelu)

"""

def main():

 action = True

 while action:
    userInput = input("Answer Y or N: ")
    if userInput == "y" or userInput == "Y":
        print("Well, let's stop this, then.")
        action = False
    while userInput != "Y" and userInput != "y" and userInput != "n" and userInput != "N":
        print("Incorrect entry.")
        userInput = input("Answer Y or N: ")


if __name__=="__main__":
    main()
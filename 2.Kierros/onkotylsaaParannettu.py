"""
COMP.CS.100 Ohjelmointi 1.
Tekijä: Karam Chafqane (TAMK ristiinopiskelu)

"""

def main():

 action = True
 
 while action:
    userInput = input("Bored? (y/n) ")
    if userInput == "y" or userInput == "Y":
        print("Well, let's stop this, then.")
        action = False
    while userInput != "Y" and userInput != "y" and userInput != "n" and userInput != "N":
        print("Incorrect entry.")
        break
    


if __name__=="__main__":
    main()
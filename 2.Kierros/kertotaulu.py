"""
COMP.CS.100 Ohjelmointi 1.
Tekijä: Karam Chafqane (TAMK ristiinopiskelu)

"""

def main():
 
 chosenNumber = int(input("Choose a number: "))
 number = 1
 while number <= 10:
    print(number, "*", chosenNumber, "=", number * chosenNumber)
    number += 1


 
 


if __name__=="__main__":
    main()
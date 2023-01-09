"""
COMP.CS.100 Ohjelmointi 1.
Tekijä: Karam Chafqane (TAMK ristiinopiskelu)

"""

def main():
 
 chosenNumber = int(input("Choose a number: "))
 number = 1
 result = 0
 while result <= 100:
    result = number * chosenNumber
    print(number, "*", chosenNumber, "=", result)
    number += 1
    


 
 


if __name__=="__main__":
    main()
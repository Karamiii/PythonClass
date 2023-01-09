"""
COMP.CS.100 Ohjelmointi 1.
Tekijä: Karam Chafqane (TAMK ristiinopiskelu)

"""

def main():

 chosenNumber = int(input("How many numbers would you like to have? "))
 counter = 1
 while counter <= chosenNumber:
    if (counter % 3) == 0 and (counter % 7) == 0:
        print("zip boing") 
    elif (counter % 3) == 0:
        print("zip")
    elif (counter % 7) == 0:
        print("boing")
    else:
        print(counter)
    counter += 1


if __name__=="__main__":
    main()
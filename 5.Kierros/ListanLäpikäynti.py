
"""
COMP.CS.100 Ohjelmointi 1.
Tekijä: Karam Chafqane (TAMK ristiinopiskelu)

"""

def main():

    flag = True
    numbers = []
    print("Give 5 numbers:")

    for i in range(0, 5):
        value = int(input("Next number: "))
        if value > 0:
            numbers.append(value)

    print("The numbers you entered that were greater than zero were:")
    for values in numbers:
        print(values)       





if __name__=="__main__":
    main()


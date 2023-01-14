"""
COMP.CS.100 Ohjelmointi 1.
Tekijä: Karam Chafqane (TAMK ristiinopiskelu)

"""

def main():

    flag = True
    numbers = []
    print("Give 5 numbers:")

    for i in range(0, 5):
        numbers.append(int(input("Next number: ")))


    print("The numbers you entered, in reverse order:")
    for index in range(4, -1, -1):
        print(numbers[index])

if __name__=="__main__":
    main()


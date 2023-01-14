"""
COMP.CS.100 Ohjelmointi 1.
Tekijä: Karam Chafqane (TAMK ristiinopiskelu)

"""


def input_to_list(value):
    """
    jeee tämä tekee hienoja asioita silee hienosti
    """
    print("Enter", value, "numbers: ")
    array = []

    for i in range(0, value):
        array.append(int(input()))

    return array    

    




def main():


    value = int(input("How many numbers do you want to process: "))
    array = input_to_list(value)
    searchValue = int(input("Enter the number to be searched: "))
    counter = 0

    for index in array:
        if index == searchValue:
            counter += 1 

    if counter == 0:
        print(searchValue, "is not among the numbers you have entered.")
    
    else:
        print(searchValue, "shows up", counter, "times among the numbers you have entered.")




if __name__=="__main__":
    main()


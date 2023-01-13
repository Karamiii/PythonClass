"""
COMP.CS.100 Ohjelmointi 1.
Tekijä: Karam Chafqane (TAMK ristiinopiskelu)

"""


def main():

    totalBalls = read_input("Enter the total number of lottery balls: ")
    drawnBalls = read_input("Enter the number of the drawn balls: ")

    check_input(totalBalls, drawnBalls)



def read_input(message):
    """
    Function gets a message as a parameter, which it uses when asking the user for values. Function then returns the values back to the 
    main function.

    """

    answer = int(input(message))
    return answer



def check_input(totalBalls, drawnBalls):
    """
    Fucntion checks whether or not the values provided by the user are acceptable. IF they are not, the porgram informs of this and
    ends the program. Else, it sends the values forward to make calulations.
    """

   
    if totalBalls <= 0 and drawnBalls > 0:
        print("The number of balls must be a positive number.")
        return
    elif totalBalls < drawnBalls:
        print("At most the total number of balls can be drawn.")
        return       
    elif totalBalls <= 0 or drawnBalls <= 0:
        print("The number of balls must be a positive number.")
        return
    else:
        calculate_results(totalBalls, drawnBalls)


def calculate_results(totalBalls, drawnBalls):
    """
    Function calulates the value of odds in the lottery. AFter calulations the function prints the answer to the user and ends the program
    """
    n = 1
    p = 1
    z = 1
    calculation = totalBalls - drawnBalls


    for i in range(1, totalBalls + 1):
        n = n * i
    for j in range(1, drawnBalls + 1):
        p = p * j   
    for k in range(1, calculation + 1):
        z = z * k

    

    answer = n//(z * p)
    
    print(f"The probability of guessing all {drawnBalls} balls correctly is 1/{answer}")


if __name__=="__main__":
    main()
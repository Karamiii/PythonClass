"""
COMP.CS.100 Ohjelmointi 1.
Tekijä: Karam Chafqane karam.chafqane@tuni.fi (TAMK ristiinopiskelu)
Opiskelijanumero (TAMK): 2207055
Opiskelijanumero (Yliopisto): 151552274

Ohjelman tarkoitus on laskea suurin inflaation muutos käyttäjän syötteiden väliltä.

"""


def main():

    # initialize local and global variables.

    ExitFlag = True
    newMonth = 0
    monthCounter = 0
    previousMonth = 0
    inflationRate = -5000
    MINIMUM_MONTHS = 2
    
    # Begin a while loop that ends, when the user gives and empty string as an input (Enter).
    # Loop collects user inputs, from which the program calculates the biggest inflation rate.

    while ExitFlag:
        previousMonth = newMonth
        UserInput = input(f"Enter inflation rate for month {monthCounter + 1}: ")
        
        if UserInput == '':
            ExitFlag = False
            # When the program recieves an empty input, program checks whether or not user has provided at least 2 valuas prior to the empty input.
            # If the condition is not met, porgram exits.
            # If the condition is met, program breaks out of the loop and presents the results.

            if monthCounter < MINIMUM_MONTHS:
                print("Error: at least 2 monthly inflation rates must be entered.")
                return
            else:
                break    
        else:
             monthCounter += 1
             newMonth = float(UserInput)

        # Calculate inflation rate between 2 months. If the inflation rate is bigger than the calculated value of
        # the previous months, the inflation rate is the updated with the latest value
        if monthCounter >= 2:
            if (previousMonth >= newMonth) and (newMonth - previousMonth) > inflationRate:
                inflationRate = (newMonth - previousMonth)
            elif (newMonth > previousMonth) and (newMonth - previousMonth) > inflationRate:
                inflationRate = (newMonth - previousMonth)   
            else:
                continue
            
    print(f"Maximum inflation rate change was {inflationRate:.1f} points.")
    return
    


if __name__=="__main__":
    main()
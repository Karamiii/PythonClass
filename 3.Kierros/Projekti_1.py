"""
COMP.CS.100 Ohjelmointi 1.
Tekijä: Karam Chafqane (TAMK ristiinopiskelu)

"""

def main():

    ExitFlag = True
    holder = 0
    monthCounter = 0
    holder2 = 0
    inflationRate = -500
    MINIMUM_MONTHS = 2
    
    
 
    while ExitFlag:
        holder2 = holder
        UserInput = input(f"Enter inflation rate for month {monthCounter + 1}: ")
        
        if UserInput == '':
            ExitFlag = False
            if monthCounter < MINIMUM_MONTHS:
                print("Error: at least 2 monthly inflation rates must be entered.")
                exit(1)        
        else:
             monthCounter += 1
             holder = float(UserInput)

        if monthCounter >= 2:
            if (holder2 > holder):
                if (holder - holder2) > inflationRate:
                    inflationRate = (holder - holder2)
            elif (holder > holder2):
                if (holder - holder2) > inflationRate:
                    inflationRate = (holder - holder2)   
            else:
                continue
            
    print(f"Maximum inflation rate change was {inflationRate:.1f} points.")
    return
    
    

    



if __name__=="__main__":
    main()
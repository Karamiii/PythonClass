"""
COMP.CS.100 Ohjelmointi 1.
Tekijä: Karam Chafqane karam.chafqane@tuni.fi (TAMK ristiinopiskelu)
Opiskelijanumero (TAMK): 2207055
Opiskelijanumero (Yliopisto): 151552274

Ohjelman tarkoitus on laskea suurin inflaation muutos käyttäjän syötteiden väliltä.

"""

def main():

    # Alustetaan paikalliset ja globaalit muuttujat.

    ExitFlag = True
    newMonth = 0
    monthCounter = 0
    previousMonth = 0
    inflationRate = -500
    MINIMUM_MONTHS = 2
    
    # Aloitetaan while looppi joka päättyy, kun käyttäjä antaa tyhjän syötteen.
    # Loopissa otetaan käyttäjältä syötteitä, joista lasketaan suurin inflaation muutos.
    
    while ExitFlag:
        previousMonth = newMonth
        UserInput = input(f"Enter inflation rate for month {monthCounter + 1}: ")
        
        if UserInput == '':
            ExitFlag = False 

            # Tyhjän syötteen tullessa ohjelma tarkistaa, että onko syötetty vähintään 2 lukua. Ohjelma poistuu virhekoodilla 1, jos ehto ei täyty.
            if monthCounter < MINIMUM_MONTHS:
                print("Error: at least 2 monthly inflation rates must be entered.")
                exit(1)            
        else:
             monthCounter += 1
             newMonth = float(UserInput)

        # Lasketaan kahden kuukauden välinen inflaatio. Jos inflaatio on suurempi kuin edellisten kuukausien laskettu arvo,
        # niin tulos päivitetään.
        if monthCounter >= 2:
            if (previousMonth > newMonth) and (newMonth - previousMonth) > inflationRate:
                inflationRate = (newMonth - previousMonth)
            elif (newMonth > previousMonth) and (newMonth - previousMonth) > inflationRate:
                inflationRate = (newMonth - previousMonth)   
            else:
                continue
            
    print(f"Maximum inflation rate change was {inflationRate:.1f} points.")
    return
    


if __name__=="__main__":
    main()
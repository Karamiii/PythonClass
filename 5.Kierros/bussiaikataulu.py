"""
COMP.CS.100 Ohjelmointi 1.
Tekijä: Karam Chafqane (TAMK ristiinopiskelu)

"""

def main():

    busTimes = [630, 1015, 1415, 1620, 1720, 2000]

    leaveTime = int(input("Enter the time (as an integer): "))
    counter = 0
    i = -1
    print("The next buses leave:")
    while i <= len(busTimes):
        i += 1
        if busTimes[i] >= leaveTime:
            print(busTimes[i])
            counter += 1
        if counter < 3 and i == len(busTimes) - 1:
            i = -1
            leaveTime = 0
        if counter == 3:
            break        
        





if __name__=="__main__":
    main()

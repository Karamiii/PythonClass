
"""
COMP.CS.100 Ohjelmointi 1.
Tekijä: Karam Chafqane (TAMK ristiinopiskelu)

"""

def main():

 for month in range(1,13):
    for day in range(1,32):
        if month == 2 and day == 28:
            print(f"{day}.{month}.")
            break
        if (month == 4 or month == 6 or month == 9 or month == 11) and day == 30:
            print(f"{day}.{month}.")
            break
        else:    
            print(f"{day}.{month}.")


if __name__=="__main__":
    main()
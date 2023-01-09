"""
COMP.CS.100 Ohjelmointi 1.
Tekijä: Karam Chafqane (TAMK ristiinopiskelu)

"""

def main():

 chosenRange = int(input("How many Fibonacci numbers do you want? "))
 number = 0
 fib = 0
 holder = 1
 for value in range(1, chosenRange + 1):
    
    print(f"{value}. {holder}")
    fib = number
    number = holder
    holder = fib + number
    


if __name__=="__main__":
    main()
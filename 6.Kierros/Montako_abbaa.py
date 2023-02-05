"""
COMP.CS.100 Ohjelmointi 1.
Tekijä: Karam Chafqane (TAMK ristiinopiskelu)

"""


def count_abbas(string):
    """This function gets a parameter which it checks for occurances of "abba". 
    evrytime it finds the word abba in the string, calue of count is raised by one. The result is then send back to main function.
    """
    if len(string) < 4:
        return 0
    count = 0
    for i in range(len(string) - 3):
        if string[i:i+4] == "abba":
            count += 1
    return count

def main():

    answer = count_abbas("barbapapa")
    

if __name__=="__main__":
    main()


    

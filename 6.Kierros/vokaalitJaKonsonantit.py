
"""
COMP.CS.100 Ohjelmointi 1.
Tekijä: Karam Chafqane (TAMK ristiinopiskelu)

"""

def main():

    userIput = input("Enter a word: ")
    consonants = 0
    vowels = 0
    vowelsList = ['a', 'e', 'i', 'o', 'u', 'y']
    counter = 0
    


    for index in userIput:
        for i in vowelsList:
            if index == i:
                counter += 1
                break
        if counter == 0:
            consonants += 1
            counter = 0
        else:
            vowels += 1
            counter = 0           
                     

    print(f"The word \"{userIput}\" contains {vowels} vowels and {consonants} consonants.")


    

 


if __name__=="__main__":
    main()


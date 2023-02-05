
"""
COMP.CS.100 Ohjelmointi 1.
Tekijä: Karam Chafqane (TAMK ristiinopiskelu)

"""

def capitalize_initial_letters(paragraph):
    """ 
    Function takes in a paragraph as a parameter, goes through it and changes first letters in a word
    as an uppercase character.
    """

    array = paragraph.split()
    result = ""
    i = 0
    for word in array:
        for letter in word:
            if i == 0:
                result += letter.upper()
                i += 1
            else:
                result += letter.lower()
                i += 1
        result += " "
        i = 0
    return result.strip()
        




def main():

    result = capitalize_initial_letters("kAram cHAFQane")
    
    
 


if __name__=="__main__":
    main()


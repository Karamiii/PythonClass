"""
COMP.CS.100 Ohjelmointi 1.
Tekijä: Karam Chafqane (TAMK ristiinopiskelu)

"""

def is_the_list_in_order(array):
    """
    Funktio katsoo onko lista suuruusjärjestyksessä ja silleensä ja silleen juu
    """

    newArray = sorted(array)

    

    if newArray == array:
        return True

    else:
        return False    




def main():


    array = [12, 13, 11, 15]
    answer = is_the_list_in_order(array)
    
 


if __name__=="__main__":
    main()

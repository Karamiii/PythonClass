"""
COMP.CS.100 Ohjelmointi 1.
Tekijä: Karam Chafqane (TAMK ristiinopiskelu)

"""

def are_all_members_same(array):
    """
    Tämä funktio tekee vaikka mink'laista ihmeellisyyttä ja silleee
    """

    x = 0
    flag = True


    for value in array:
        if value == array[x - 1]:
            flag = True
            continue 
        else:
            return False
               
    return flag   



def main():


    array = [22, 21, 21, 22]

    answer = are_all_members_same(array)
    



if __name__=="__main__":
    main()


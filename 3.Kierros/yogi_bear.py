"""
COMP.CS.100 Ohjelmointi 1.
Tekijä: Karam Chafqane (TAMK ristiinopiskelu)
"""

def repeat_name(name, amount):
    """
    Funktion tarkoitus on printata laulussa kätettävää nimeä tietyn verran.
    Funtio ottaa parametreina nimen ja summan, jota käytetään printtien määrässä hyödyntäes.
    
    """

    if amount == 1:
        print(f"{name}, {name}")

    elif amount == 3:
        for i in range(1, 4):
            print(f"{name}, {name} Bear")

    elif amount == 2:
        print(f"{name}, {name} Bear")       


def verse(lyrics, name):

    """
    Funktion tarkoitus on ottaa pääohjelmasta lyriikoita ja printata niitä.
    Funktio käyttää apunaan toista funktiota, jolla printataan käytettävää nimeä kappaleessa

    """
    print(lyrics)
    repeat_name(name, 1)
    print(lyrics)
    repeat_name(name, 3)
    print(lyrics)
    repeat_name(name, 2)




def main():

    verse("I know someone you don't know", "Yogi")
    print()
    verse("Yogi has a best friend too", "Boo Boo")
    print()
    verse("Yogi has a sweet girlfriend", "Cindy")

if __name__ == "__main__":
    main()

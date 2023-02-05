"""
COMP.CS.100 Ohjelmointi 1.
Tekijä: Karam Chafqane (TAMK ristiinopiskelu)

"""
def create_an_acronym(name):
    """Functio oottaa parametreina vähän sitä sun tätä ja tekee tota ja tätä tolleen."""
    name_parts = name.split()
    acronym = ""
    
    for part in name_parts:
        acronym += part[0].upper()
    return acronym




def main():

    name = "yeee jee"
    acronym = create_an_acronym(name)
 


if __name__=="__main__":
    main()


    
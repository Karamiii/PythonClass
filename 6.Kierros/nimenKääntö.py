"""
COMP.CS.100 Ohjelmointi 1.
Tekijä: Karam Chafqane (TAMK ristiinopiskelu)

"""

def reverse_name(name):
    """
    Ohjelma tekee vähän sitä sun tätä ja tälleen eteenpäin jeee
    """

    if name.find(",") < 0:
        return name

    else:
        nameList = name.split(",")

        firstName = nameList[1].strip()


        if len(nameList[0]) > 0:
            sukuninemOsat = nameList[0].split()

            if len(sukuninemOsat) >= 1:
                sukunimi = sukuninemOsat[0]

            if len(sukuninemOsat) > 1:
                sukunimi2 = sukuninemOsat[1]
                sukunimi = sukunimi + " " + sukunimi2

        if len(nameList[1]) == 0 and len(nameList[0]) == 0:
            name = nameList[0]
            return name

        if len(nameList[1]) == 0 and len(sukuninemOsat) > 0:
            nimi = sukunimi

        if len(nameList[0]) == 0 and len(firstName) > 0:
            nimi = firstName
            return nimi



        if len(firstName) == 0 and len(sukuninemOsat) > 0:
            nimi = sukunimi

        if len(firstName) > 0 and len(sukuninemOsat) == 0:
            nimi = firstName 

        if len(firstName) > 0 and len(sukuninemOsat) > 0:
            nimi = firstName + " " + sukunimi

        return nimi                                           



def main():

    name = reverse_name("X, ")
    print(name)






if __name__=="__main__":
    main()


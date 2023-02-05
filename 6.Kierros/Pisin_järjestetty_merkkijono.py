"""
COMP.CS.100 Ohjelmointi 1.
Tekijä: Karam Chafqane (TAMK ristiinopiskelu)

"""
def longest_substring_in_order(string):
    """Funktio tarkistaa stringin aakkojsärjestytsä. Palauttaa pisimmän järjestyksen stringistä."""
    if len(string) <= 1:
        return string
    current_substring = string[0]
    longest_substring = string[0]
    for i in range(1, len(string)):
        if string[i] >= current_substring[-1]:
            current_substring += string[i]
            if len(current_substring) > len(longest_substring):
                longest_substring = current_substring
        else:
            current_substring = string[i]
    return longest_substring




def main():

    answer = longest_substring_in_order()


if __name__=="__main__":
    main()


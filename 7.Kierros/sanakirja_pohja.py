"""
COMP.CS.100 Programming 1
Code template for  tourist dictionary.
"""

def getInput(string):
    """
    This function gets the user input. This is completely useless, because pythons input function does exactly
    the same thing lol
    """
    return input(string)



def main():

    english_spanish = {"hey": "hola", "thanks": "gracias", "home": "casa"}
    spanish_english = {"hola": "hey", "gracias": "thanks", "casa": "home"}
    print("Dictionary contents:")
    print(", ".join(sorted(english_spanish)))

    while True:
        command = getInput("[W]ord/[A]dd/[R]emove/[P]rint/[T]ranslate/[Q]uit: ")

        if command == "W":

            word = getInput("Enter the word to be translated: ")
            if word in english_spanish:
                print(word, "in Spanish is", english_spanish[word])
            elif word not in english_spanish:
                print("The word", word, "could not be found from the dictionary.")

        elif command == "A":

            englishWord = getInput("Give the word to be added in English: ")
            spanishWord = getInput("Give the word to be added in Spanish: ")

            english_spanish[englishWord] = spanishWord

            print("Dictionary contents:")
            print(", ".join(sorted(english_spanish)))

        elif command == "R":

            word = getInput("Give the word to be removed: ")
            if word in english_spanish:
                del english_spanish[word]

            else:
                print("The word", word, "could not be found from the dictionary.")

        elif command == "P":

            for item in sorted(english_spanish):
                print(f"{item} {english_spanish[item]}")


        elif command == "T":

            sentance = getInput("Enter the text to be translated into Spanish: ")
            words = sentance.split()
            answer = ""

            for word in words:

                if word in english_spanish:
                    answer += english_spanish[word] + " "

                elif word not in english_spanish:
                    answer += word + " "

            answer = answer.strip()
            print("The text, translated by the dictionary:")
            print(answer)

        elif command == "Q":
            print("Adios!")
            return

        else:
            print("Unknown command, enter W, A, R, P, T or Q!")

if __name__ == "__main__":
    main()

"""
COMP.CS.100 Ohjelmointi 1.
Tekijä: Karam Chafqane (TAMK ristiinopiskelu)

"""

def main():

    wordDictionary = {}

    print("Enter rows of text for word counting. Empty row to quit.")
    line = input().lower()
    while line:
        words = line.split()
        for word in words:
            if word not in wordDictionary:
                wordDictionary[word] = 1
            elif word in wordDictionary:
                wordDictionary[word] += 1
        line = input().lower()

    for item in sorted(wordDictionary):
        print(f"{item} : {wordDictionary[item]} times")




if __name__=="__main__":
    main()

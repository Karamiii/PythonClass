"""
COMP.CS.100 Ohjelmointi 1.
Tekijä: Karam Chafqane (TAMK ristiinopiskelu)

"""

def main():
    for i in range(1, 11):
        for j in range(1, 11):
            print(f"{i*j:4}", end="", sep="    ")
        print()

if __name__ == "__main__":
    main()

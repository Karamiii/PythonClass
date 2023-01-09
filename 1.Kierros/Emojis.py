def main():

    feels = int(input("How do you feel? (1-10) "))

    if feels <= 10 and feels > 0:

        if feels > 7 and feels < 10:
            print("A suitable smiley would be :-)")

        elif feels == 1:
            print("A suitable smiley would be :'(")

        elif feels < 4:
            print("A suitable smiley would be :-(")

        elif feels == 10:
            print("A suitable smiley would be :-D")

        else:
            print("A suitable smiley would be :-|")

    else:
        print("Bad input!")



if __name__=="__main__":
    main()

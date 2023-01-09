"""atesting"""

def main():

    price = int(input("Purchase price: "))
    paid = int(input("Paid amount of money: "))

    difference = price - paid

    tens = difference // 10
    fives = (difference - tens * 10) // 5
    twos = (difference - tens * 10 - fives * 5) // 2
    ones = (difference - tens * 10 - fives * 5 - twos * 2) // 1


    if tens > 0 or fives > 0 or twos > 0 or ones > 0:
        print("Offer change:")

        if tens > 0:
            print(tens, "ten-euro notes")
        if fives > 0:
            print(fives, "five-euro notes")
        if twos > 0:
            print(twos, "two-euro coins")
        if ones > 0:
            print(ones, "one-euro coins")
    else:
        print("No change")


if __name__=="__main__":
    main()
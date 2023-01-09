"""
COMP.CS.100 Programming 1
Template Song: Old MacDonald
"""

def print_verse(animal, sound):
    """
    print verse funciton prints the lyrics for a song with 2 parameters,
    that change depending the values that are sent from main.

    param animal: Recevies an anminal name from main
    param sound: Recevies a sound corresponding to the animal

    """
    print("Old MACDONALD had a farm")
    print("E-I-E-I-O")
    print(f"And on his farm he had a {animal}")
    print("E-I-E-I-O")
    print("With a", sound, sound, "here")
    print("And a", sound, sound, "there")
    print(f"Here a {sound}, there a {sound}")
    print("Everywhere a", sound, sound)
    print("Old MacDonald had a farm")
    print("E-I-E-I-O")
    

def main():
    print_verse("cow", "moo")
    print()
    print_verse("pig", "oink")
    print()
    print_verse("duck", "quack")
    print()
    print_verse("horse", "neigh")
    print()
    print_verse("lamb", "baa")


if __name__ == "__main__":
    main()

"""
COMP.CS.100 Programming 1
ROT13 program code template
"""


def row_encryption(text):
    """
    Encrypts its parameter letter by letter using ROT13 encryption technology.

    :param text: str,  string to be encrypted
    :return: str, <text> parameter encrypted using ROT13
    """
    encrypted_text = ""
    for char in text:
        encrypted_text += encrypt(char)
    return encrypted_text

def encrypt(char):
    """
    Encrypts its parameter using ROT13 encryption technology.

    :param char: str,  character to be encrypted
    :return: str, <char> parameter encrypted using ROT13
    """

    regular_chars   = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k",
                       "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v",
                       "w", "x", "y", "z"]

    encrypted_chars = ["n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x",
                       "y", "z", "a", "b", "c", "d", "e", "f", "g", "h", "i",
                       "j", "k", "l", "m"]

    if char.lower() in regular_chars:
        char_index = regular_chars.index(char.lower())
        if char.isupper():
            return encrypted_chars[char_index].upper()
        else:
            return encrypted_chars[char_index]
    else:
        return char

def main():
    result = row_encryption("Happy, happy, joy, joy!")
    print(result)

 


if __name__=="__main__":
    main()

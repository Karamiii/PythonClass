"""
COMP.CS.100 Programming 1
Code Template
"""

def read_message():
    """This function does this and this more than this jaada jaada"""
    message = []
    
    line = input()
    while line:
        message.append(line)
        line = input()
    return message

def main():
    print("Enter text rows to the message. Quit by entering an empty row.")
    message = read_message()
    print("ROT13:")
    for line in message:
        print(line.upper())

if __name__ == '__main__':
    main()

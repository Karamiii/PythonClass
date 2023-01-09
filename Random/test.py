def fibonacci(n):
    # Initialize the first two terms of the sequence
    a, b = 0, 1
    for i in range(n):
        # Print the current term
        
        # Calculate the next term
        a, b = b, a + b
        print(a)

def main():
    # Get the number of terms from the user
    num_terms = int(input("Enter the number of terms: "))

    # Call the fibonacci function
    fibonacci(num_terms)

if __name__ == "__main__":
    main()

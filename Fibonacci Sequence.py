def fibonacci_sequence(n):
    sequence = [0, 1]

    while len(sequence) < n:
        sequence.append(sequence[-1] + sequence[-2])

    return sequence[:n]

if __name__ == "__main__":

    try:
        numTerm = int(input("Enter the number of Fibonacci terms: "))

        if numTerm <= 0:
            print("Please enter a positive integer.")
        else:
            result = fibonacci_sequence(numTerm)
            print(f"Fibonacci sequence up to {numTerm} terms: {result}")
    except ValueError:
        print("Invalid input. Please enter a valid integer.")


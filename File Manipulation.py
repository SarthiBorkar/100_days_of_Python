import string

def count_word_occurrences(file_path):
    word_counts = {}

    try:
        with open(file_path, 'r') as file:
            # Read the file content
            content = file.read().lower()

            # Remove punctuation
            content = content.translate(str.maketrans("", "", string.punctuation))

            # Split the content into words
            words = content.split()

            # Count occurrences of each word
            for word in words:
                if word in word_counts:
                    word_counts[word] += 1
                else:
                    word_counts[word] = 1

            # Display results in alphabetical order
            sorted_word_counts = sorted(word_counts.items(), key=lambda x: x[0])

            for word, count in sorted_word_counts:
                print(f"{word}: {count}")

    except FileNotFoundError:
        print("File not found. Please provide a valid file path.")
    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    try:
        # Get user input for the file path
        file_path = input("Enter the path to the text file: ")

        # Count word occurrences and display results
        count_word_occurrences(file_path)
    except KeyboardInterrupt:
        print("\nProgram terminated by the user.")

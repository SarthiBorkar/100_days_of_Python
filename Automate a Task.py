import os

def rename_files(directory_path):
    try:
        os.chdir(directory_path)

        files = os.listdir()

        for index, file_name in enumerate(files):
            new_name = f"document_{index + 1}.txt"

            os.rename(file_name, new_name)

        print("Files have been successfully renamed.")

    except FileNotFoundError:
        print("Directory not found. Please provide a valid directory path.")
    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    try:
        directory_path = input("Enter the path to the directory containing files: ")

        rename_files(directory_path)
    except KeyboardInterrupt:
        print("\nProgram terminated by the user.")


def create_file():
    """Creates a new text file and writes three lines of text to it."""
    try:
        with open("my_file.txt", "w") as file:
            file.write("This is the first line.\n")
            file.write("Here is the second line with a number: 123.\n")
            file.write("Third line of text.\n")
        print("File created and initial content written successfully.")
    except (FileNotFoundError, PermissionError) as e:
        print(f"Error while creating file: {e}")
    finally:
        print("File creation block executed.")

def read_file():
    """Reads and displays the contents of the text file."""
    try:
        with open("my_file.txt", "r") as file:
            content = file.read()
            print("File content:")
            print(content)
    except (FileNotFoundError, PermissionError) as e:
        print(f"Error while reading file: {e}")
    finally:
        print("File reading block executed.")

def append_to_file():
    """Appends three additional lines of text to the existing file."""
    try:
        with open("my_file.txt", "a") as file:
            file.write("Appending the fourth line.\n")
            file.write("Fifth line added.\n")
            file.write("This is the sixth line.\n")
        print("Additional lines appended successfully.")
    except (FileNotFoundError, PermissionError) as e:
        print(f"Error while appending to file: {e}")
    finally:
        print("File appending block executed.")

def main():
    create_file()
    read_file()
    append_to_file()
    read_file()  # Read again to show appended content

if __name__ == "__main__":
    main()

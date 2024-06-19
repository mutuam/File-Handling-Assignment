

def create_file():
    try:
        # File Creation
        with open("my_file.txt", "w") as file:
            file.write("First line of text\n")
            file.write("Second line of text with number 123\n")
            file.write("Third line of text with another number 456\n")
        print("File created and initial content written successfully.")
    except Exception as e:
        print(f"An error occurred while creating the file: {e}")

def read_file():
    try:
        # File Reading and Display
        with open("my_file.txt", "r") as file:
            content = file.read()
            print("Content of 'my_file.txt':")
            print(content)
    except FileNotFoundError:
        print("File not found. Please ensure 'my_file.txt' exists.")
    except PermissionError:
        print("Permission denied. Please check your file permissions.")
    except Exception as e:
        print(f"An error occurred while reading the file: {e}")

def append_to_file():
    try:
        # File Appending
        with open("my_file.txt", "a") as file:
            file.write("Fourth line of text\n")
            file.write("Fifth line of text with number 789\n")
            file.write("Sixth line of text with another number 012\n")
        print("Additional content appended successfully.")
    except Exception as e:
        print(f"An error occurred while appending to the file: {e}")

def main():
    try:
        create_file()
        read_file()
        append_to_file()
        read_file()
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
    finally:
        print("File handling operations completed.")

if __name__ == "__main__":
    main()

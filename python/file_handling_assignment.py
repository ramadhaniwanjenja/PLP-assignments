def create_file():
    try:
        # Open the file in write mode
        with open("my_file.txt", "w") as file:
            # Write three lines of text to the file
            file.write("welcome to the world of python\n")
            file.write("you will have 100 chance to win if you write python\n")
            file.write("like 100 percent of people are now enjoying after learning python.\n")
        print("File created successfully.")
    except FileNotFoundError:
        print("File not found.")
    except PermissionError:
        print("Permission denied.")
    finally:
        print("File creation process completed.")

def read_file():
    try:
        # Open the file in read mode
        with open("my_file.txt", "r") as file:
            # Read and display the contents of the file
            print("File contents:")
            for line in file:
                print(line.strip())
    except FileNotFoundError:
        print("File not found.")
    except PermissionError:
        print("Permission denied.")
    finally:
        print("File reading process completed.")

def append_file():
    try:
        # Open the file in append mode
        with open("my_file.txt", "a") as file:
            # Append three more lines of text to the file
            file.write("new scenario\n")
            file.write("if you code python 2 times per day \n")
            file.write("you increase your python coding skills 70 percent\n")
        print("File appended successfully.")
    except FileNotFoundError:
        print("File not found.")
    except PermissionError:
        print("Permission denied.")
    finally:
        print("File appending process completed.")

# Create the file
create_file()

# Read and display the file contents
read_file()

# Append additional content to the file
append_file()

from pathlib import Path

# Get Input
user_input = input("Enter a line of text: ")
file_name = input("Please enter a filename - example.txt: ")

# Create File
try:
     with open(file_name, "w") as f:
        f.write(user_input)
        print("Text Successfully written to file.")
        print(f"Stored file path: {Path(file_name).resolve()}")

except Exception as e:
    print(f"Error: Failure to create or write to the file. ({e})")

# Read File
try:
    with open(file_name, "r") as f:
        content = f.read()
        print("Reading from file...")
        print(content)
except FileNotFoundError:
    print("Error: Failure to open the file - it does not exist.")
except Exception as e:
    print(f"Error: Failure to read from the file. ({e})")
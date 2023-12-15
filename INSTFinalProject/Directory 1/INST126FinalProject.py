import sys
import os

# Change the working directory to the specified path
os.chdir("/Users/annagalvin/Desktop/INSTFinalProject")

# Change the working directory to Directory 1
os.chdir("/Users/annagalvin/Desktop/INSTFinalProject/Directory 1")

# Change the working directory to Directory 2
os.chdir("/Users/annagalvin/Desktop/INSTFinalProject/Directory 1/Directory 2")

#Get the text file
file_path = ("/Users/annagalvin/Desktop/INSTFinalProject/Directory 1/Directory 2/Text_File_1")

# Print the current working directory
print(os.getcwd())

# The function takes a parameter for the file path
def process_file(file_path):
    try:
        with open(file_path, 'r') as file:
            content = file.read()
            # Use a string method to split the content into a list of words
            words = content.split()
            return len(words), content
    except FileNotFoundError:
        # Handle missing or incorrect file path
        raise FileNotFoundError(f"File not found: {file_path}")
    except Exception as e:
        # Handle other exceptions
        raise RuntimeError(f"Error processing file: {e}")

# This block checks that the script is used with exactly one command-line argument
if len(sys.argv) != 2:
    # Raise an error and provide a helpful error message to the user
    raise ValueError("Usage: python script.py <file_path>")

# Receive the file path from the command line argument
file_path = sys.argv[1]

# This returns the word count and the content of the file as a whole back to the user, calling two variables
# Use a tuple to return multiple values from a function
word_count, file_content = process_file(file_path)

# This script will print the word count and what is said in the file to the terminal
# Print the results
print(f"Word count: {word_count}")
print("File content:")
print(file_content)







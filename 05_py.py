"""
Zhaoyu Lin, Ishraq Mahid, Alejandro
SoftDev
A Program to Print a SoftDev Student's Name - Revamped
2021-09-27

#SUMMARY OF TRIO DISCUSSION 
Zhaoyu's code was the most effecient in terms of scalability and usage. By utilizing a text file as an input, it allows easier practical use
of the program. Furthermore, the integration of random and clean combination of lists allows for easy management of the two periods, allowing us to later shape
them as we wish if need be.

#DISCOVERIES
random.choice is a very simple and clean use of the Random module. There is a lot more we can do in terms of brushing up on Python and finding
quicker ways to code.

#QUESTIONS 
How could we more effectively gather the desired names of pd1 and pd2?

#COMMENTS
Overall, this seems like a simple assignment in terms of choosing a student name, but when incorporating how one would desire to change the program
it increases the complexity.
"""


import sys,random

def read_names(filename):
    """Reads a text file containing a list of names, where each line contains
    one name, and returns a list of the names."""
    file_contents = ""
    with open(filename, "r") as f:
        file_contents = f.read()
    namesList = file_contents.split("\n")
    
    # Remove empty lines based on if string is empty
    names = [name for name in namesList if name]
    return names

def main():
    """Prints a random student name given two files containing lists of names,
    where each line contains one name."""
    if len(sys.argv) != 3:
        print("Usage: python 05_py.py pd1_filename pd2_filename")
        return

    pd1 = read_names(sys.argv[1])
    pd2 = read_names(sys.argv[2])
    names = pd1 + pd2

    # Pick a random name from the list of pd1 and pd2 names
    print(random.choice(names))

if __name__ == "__main__":
    main()

import os

def append_to_file():
    f = open("newfile.txt", "a")
    f.write("Added Content to the file\n")
    f.close()

append_to_file()
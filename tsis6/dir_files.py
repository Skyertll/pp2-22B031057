#1
import string
import os

path = "C:\VScode_programs\CPP\Lab_11"

print("Directories in", path, ":")
for item in os.listdir(path):
    if os.path.isdir(os.path.join(path, item)):
        print(item)

print("Files in", path, ":")
for item in os.listdir(path):
    if os.path.isfile(os.path.join(path, item)):
        print(item)

print("Directories and files in", path, ":")
for item in os.listdir(path):
    print(item)

#2
if os.path.exists(path):
    print(path, "exists")
    if os.access(path, os.R_OK):
        print(path, "is readable")
    else:
        print(path, "is not readable")
    if os.access(path, os.W_OK):
        print(path, "is writable")
    else:
        print(path, "is not writable")
    if os.access(path, os.X_OK):
        print(path, "is executable")
    else:
        print(path, "is not executable")

else:
    print(path, "does not exist")

#3
path = "C:\VScode_programs\CPP\Lab_11\lab11_d.cpp"
if os.path.exists(path):
    print(path, "exists")
    filename = os.path.basename(path)
    directory = os.path.dirname(path)

    print("Filename:", filename)
    print("Directory:", directory)

else:
    print(path, "does not exist")

#4
filename = "blablabla.txt"

with open(filename, "r") as file:
    num_lines = sum(1 for line in file)

print("Number of lines in", filename, ":", num_lines)

#5
filename = "blablabla.txt"
mylist = ["i", "want", "pizza"]

with open(filename, "w") as file:
    for item in mylist:
        file.write("%s\n" % item)

#6
filenames = [f"{letter}.txt" for letter in string.ascii_uppercase]
for filename in filenames:
    with open(filename, "w") as file:
        file.write(f"This is the file {filename}")

#7
source_filename = "blablabla.txt"
destination_filename = "asdfsg.txt"

with open(source_filename, "r") as source_file:
    with open(destination_filename, "w") as destination_file:
        destination_file.write(source_file.read())

#8
file_path = "there/should/be/some/file.txt"

if os.access(file_path, os.F_OK):
    if os.access(file_path, os.W_OK):
        os.remove(file_path)
        print(f"{file_path} deleted.")
    else:
        print(f"No write access to {file_path}.")
else:
    print(f"{file_path} does not exist.")
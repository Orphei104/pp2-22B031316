import string
import os

letters = string.ascii_letters
folder = "sixth"
if not os.path.exists(folder):
    os.mkdir(folder)

for letter in letters:
    filename = os.path.join(folder, letter + ".txt")
    with open(filename, "w") as f:
        f.write("File " + filename)
    print(f"{filename} created")

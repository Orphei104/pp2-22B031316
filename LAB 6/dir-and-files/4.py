filename = "./dir1/text.txt"

with open(filename, "r") as f:
    lines = f.readlines()

print("Number of lines:", len(lines))

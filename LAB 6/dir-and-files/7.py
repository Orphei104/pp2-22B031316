source_file = "./seven/1.txt"
destination_file = "./seven/2.txt"

with open(source_file, "r") as f1, open(destination_file, "w") as f2:
    f2.write(f1.read())

print(f"{source_file} copied to {destination_file}")

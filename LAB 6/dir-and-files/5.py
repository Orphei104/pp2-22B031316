mylist = ["apple", "banana", "cherry"]
filename = "./dir1/list.txt"

with open(filename, "w") as f:
    for item in mylist:
        f.write(item + "\n")

print("written")

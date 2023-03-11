import os

path = "."

print("Exist?:", os.path.exists(path))
print("Read:", os.access(path, os.R_OK))
print("Write:", os.access(path, os.W_OK))
print("Execute:", os.access(path, os.X_OK))
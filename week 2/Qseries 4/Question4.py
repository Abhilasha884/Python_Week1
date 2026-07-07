import os

print("Current working directory ",os.getcwd())
with open("week 2/Qseries 4/list.txt","r") as file:
    lines=file.readlines()


file.close()
print("Contents of file: ")
print(lines)
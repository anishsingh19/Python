import os

folders = os.listdir("data")

print(folders)

for folder in folders:
    print(folder)

for folder in folders:
    print(os.listdir(f"data/{folder}"))

for folder in folders:
    print(folder)
    print(os.listdir(f"data/{folder}"))


print(os.getcwd())
# os.chdir("/Users") #to change directory 
# print(os.getcwd())





import os
os.system("cls")

file = open("nomedoaquivo.txt", "r+", encoding='uft8')
file.write('teste')
file.seek(0)
print(file.read())
file.close()
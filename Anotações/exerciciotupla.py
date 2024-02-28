import os
os.system('cls')

elementos_tupla = ('kauan', 'pedro', 'luiz', 'valter', 'ester')

for i in elementos_tupla:
    print(f'\nA palavra {i} tem as vogais:', end="")
    for letra in i:
        if(letra == 'a' or letra == 'e' or letra == 'i' or letra == 'o' or letra == 'u'):
            print(letra, end=" " )
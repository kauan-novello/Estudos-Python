import os
os.system('cls')
matriz = []

qtdLinhas = int(input(f"Digite a quantidade de linhas: "))
qtdColunas = int(input(f"Digite a quantidade de colunas: "))

for i in range(qtdLinhas):
    matriz.append([])

for linha in range(qtdLinhas):
    for coluna in range(qtdColunas):
        matriz[linha].append(int(input(f"Digite um valor para a posição [{linha}] [{coluna}]: ")))

for x in range(qtdLinhas):
    for y in range(qtdColunas):
        print(f"[{matriz[x][y]:}]", end="\t")
    print("")
import os
os.system('cls')

matriz = [[],[],[]]
soma = 0
somaColuna = 0

for linha in range(3):
    for coluna in range(3):
        matriz[linha].append(int(input(f"Digite um valor para a posição [{linha}] [{coluna}]: ")))

print("\n")

for linha in range(3):
    for coluna in range(3):
        print(f"[{matriz[linha][coluna]:^4}]", end="\t")
    print("")

for linha in range(3):
    for coluna in range(3):
        if matriz[linha][coluna]%2 != 0:
            soma += matriz[linha][coluna]
        if coluna == 0:
            somaColuna += matriz[linha][coluna]

print("\n")
print(f"Soma é igual a {soma}")   
print(f"A soma dos valores é igual a {somaColuna}")
print(f"O minimo é {min(matriz[2])}")
print("\n")
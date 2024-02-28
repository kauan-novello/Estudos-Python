""" 
Matriz 2x4
Exibir formato de tabela
Exibir o valor que está na primeira linha e segunda coluna
"""

#nome_matriz = [[tamanho_x],[tamanho_y],[...]]

matriz = [[],[]]

for linha in range(2):
    for coluna in range(4):
        matriz[linha].append(int(input(f"Digite um valor para a posição [{linha}] [{coluna}]: ")))

matriz[linha][coluna]

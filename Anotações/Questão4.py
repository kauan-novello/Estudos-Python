""""
[20 pontos – Matrizes] Aline está precisando de sua ajuda para poder passar na
cadeira de álgebra linear. Ela está pedindo para você desenvolver um programa
que recebe uma matriz 3x3 e retorne:
a) o produto dos elementos da diagonal principal (valores em vermelho);
b) a média de todos os elementos da matriz;
c) o maior valor lido da segunda coluna;
d) e exibir na tela os valores menores ou iguais a média.
"""
import os
os.system("cls")

matriz =[[],[],[]]
produto = 0
produtoDaDiagonal = 0
somaDeTodosOsValores = 0

for linhas in range(3):
    for colunas in range(3):
        matriz[linhas].append(int(input(f"Digite o valor de [{linhas}][{colunas}]: ")))
        somaDeTodosOsValores += matriz[linhas][colunas]

for linhas in range(3):
    for colunas in range(3):
        if(linhas==colunas):
            produtoDaDiagonal += matriz[linhas][colunas]
    produto *= matriz[linhas][0]
    print()


print(f'\nProduto da diagonal: {produtoDaDiagonal}')
print(f'\nMedia = {somaDeTodosOsValores/3}')

#infelizmente acabou o tempo da prova ;(

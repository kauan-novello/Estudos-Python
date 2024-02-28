""" 
[15 pontos – Laço de repetição e condicional] Escreva um programa que conte a
quantidade de curvas para a esquerda e para a direita indicadas por um GPS.
Tome cuidado que o GPS às vezes não é muito preciso e dá indicações incorretas.

Para uma curva à esquerda, o GPS pode indicar: E, Esq ou Esquerda. 
Para uma curva à direita, o GPS pode indicar D, Dir ou Direita. 

Qualquer outra indicação do GPS que não seja curva à esquerda ou à direita deve ser contada como incorreta.

Seu programa deve ler as indicações do GPS e contar quantas curvas foram à
esquerda, quantas à direita e quantas indicações incorretas foram dadas. O
programa encerra quando for digitado “Sair”.

"""
import os
os.system("cls")

curva_D = 0
curva_E = 0
incorretas = 0

verificador = "true"

while verificador == "true":
    comando = input("\nDigite um comando: ")

    if comando == "D" or comando == "Dir" or comando == "Direita":
        curva_D +=1
    elif comando == "E" or comando == "Esq" or comando == "Esquerda":
        curva_E +=1
    elif comando == "Sair":
        print(f"\nTotal de curvas a direita: {curva_D}")
        print(f"Total de curvas a esquerda: {curva_E}")
        print(f"Total de incorretas: {incorretas}")
        verificador = "false"
        #break
    else:
        print("Comando inválido")
        incorretas += 1

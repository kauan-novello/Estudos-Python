""" 
Escreva um programa que receba 3 números 
inteiros (A, B e N) e imprima todos os múltiplos de N no intervalo entre A e B. É 
interessante salientar que não necessariamente A<B, então você deve tratar isso 
também em seu código!
Exemplo: Entrada: 1 10 2
Saída: 2 4 6 8 10

"""
A = int(input())
B = int(input())
N = int(input())
vet = []
for i in range(A,B+1):
    if i%N==0:
        vet.append(i)
print(f'Múltiplos: {vet}')

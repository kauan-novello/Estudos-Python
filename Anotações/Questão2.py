"""
[20 pontos – Laço de repetição] Desenvolva um programa que pergunte ao
usuário quantos elementos da sequência de Fibonacci ele gostaria de visualizar.
Para quem não conhece, é uma sequência de números inteiros, começando
normalmente por 1 e 1, na qual cada termo seguinte corresponde à soma dos
dois anteriores. 
Então: 

Fib(0) = 1; 
Fib(1) = 1; 
Fib(2) = Fib(1) + Fib(0) = 2...


Exemplo: Entrada de dados: 9
Saída de dados: 1 1 2 3 5 8 13 21 34
"""
import os
os.system('cls')

qtdElementos = (int(input("Quantos elementos da sequência de Fibonacci você gostaria de visualizar? ")))
fib = [0, 1]
next = 0

for i in range(1, qtdElementos, 1):
    next = fib[i] + fib[i-1]
    fib.append(next)

#fib[0].remove 
print(fib[1:qtdElementos+1])
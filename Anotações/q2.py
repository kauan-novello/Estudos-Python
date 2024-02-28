""" 
Desenvolva um programa em que o usuário deverá inserir 
10 valores inteiros que serão armazenados no vetor A. 
Na sequência:

a) Crie um novo vetor B que irá conter todos os números ímpares 
do vetor A;

b) Crie um novo vetor C que irá conter todos os números pares do 
vetor A.
"""

num = []
imp = []
par = []

for i in range(10):
    a = int(input())
    num.append(a)
    if a%2==0:
        par.append(a)
    else:
        imp.append(a)
    
print(f'Vetor:{num}\nImpares:{imp}\nPares:{par}')
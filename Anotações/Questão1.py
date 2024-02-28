import os
os.system("cls")

vetor_A = []
vetor_B = []
vetor_Soma = []

n = int(input("Digite o tamanho dos vetores: "))
print("\t")

for i in range(1,n+1,1):
    #i +=1
    vetor_A.append(int(input(f"Digite o {i}° valor de A: ")))
    #vetor_B.append(int(input(f"Digite o {i}° valor de B: "))) poderia ter feito dessa forma mas preferir colocar em 2 for's os valores separados 
print("\t")

for i in range(1,n+1,1):
    #i +=1
    vetor_B.append(int(input(f"Digite o {i}° valor de B: ")))
print("\t")

for i in range(n):
    vetor_Soma.append(vetor_A[i] + vetor_B[i])

#print(f"A = {vetor_A}")
#print(f"B = {vetor_B}")
print(f"Soma = {vetor_Soma}")
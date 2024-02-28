""" 
Um número é considerado triangular se ele é produto de três números naturais consecutivos. 
Por exemplo: 120 é triangular, pois 4*5*6 = 120. O número 2730 é triangular, pois 
13*14*15 = 2730. Após o usuário digitar um número natural (inteiro não-negativo), 
verifique se ele é triangular ou não.
"""

num = int(input())
vet = []
for i in range(num):
    if(i*(i+1)*(i+2))==num:
        vet.append(i)
        vet.append(i+1)
        vet.append(i+2)
        break

print(f'Números:{vet}')
import os
os.system('cls')

def fatorial(n):
  if n == 1:
    return n
  elif n == 0:
    return 1
  elif n > 1:
    return n * fatorial(n-1)
  
n = int(input())
print(fatorial(n))

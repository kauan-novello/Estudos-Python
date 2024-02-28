import os
os.system("cls")

animais = [1,2,3] # Criando uma lista(array) chamada animais
animais = ["cachorro", "gato", 12345, 6.5] # Mudando elementos da lista

print(animais[0],'\n') # Imprimindo o primeiro elemento da lista
print(animais[3],'\n') # Imprimindo o 4 elemento da lista

animais[0] = "papagaio"# Substituindo o primeiro elemento da lista
print(animais[0],'\n')
print(animais, '\n')# O que antes era cachorro agora virou papagaio

animais.remove("gato")# Removendo gato da lista
print(animais, '\n')

print(len(animais), '\n')# Imprimindo a quantidade de elementos no array

print("gato" in animais, '\n')# Verificando se a palavra gato está no array

animais.append("leão")# Adicionar uma palavra dentro de uma lista

# Não será possivél ultilizar por ex: animais.append("leão", "Cachorro") pois o metodo append aceita apenas 1 atributo
# Para adiciionar mais de 1 atribruto o metodo mais apropriado seria o .extend
animais.append(["leão", "Cachorro"])# Caso adicione dessa forma ele criará uma alista dentro de uma lista, uma lista ninhada
print(animais, '\n')

animais.remove(["leão", "Cachorro"])# Removendo a lista ninhada

# Para ultilizar da maneira correta seria assim...
animais.extend(["leão", "Cachorro"])
print(animais, '\n')

print(animais.count("leão"))# Conta a quantidade de vezes que o atributo escolhido aparece no array
print('\n')                 # Obs: o metodo count não conta dentro de listas ninhadas

lista = [500, 30, 300, 80, 10]# Nova lista só com números

print(max(lista), '\n')# Printando o maior número
print(min(lista), '\n')# Printando o menor número

lista.sort()# Ordena a lista do maior para o menor
print(lista, '\n')
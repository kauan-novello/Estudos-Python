import os
os.system("cls")

nome_arquivo = 'arquivo.txt'
manipulador = open(nome_arquivo, 'r', encoding='utf8')

for linha in manipulador:
    if 'liberdade' in linha: 
        print(linha.strip())

manipulador.close()
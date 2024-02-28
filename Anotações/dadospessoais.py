# Deverá ser criado um arquivo .txt o qual irá conter seus dados pessoais 
# (nome completo, profissão, graduação, faculdade....).
# Na sequência, o arquivo deverá ser lido e as seguintes informações exibidas:

# a) Exibir todos os dados;
# b) Quantidade de palavras;
# c) Quantidade de caracteres.


arquivo = open("dados.txt", "r")
dados = arquivo.read()
palavras = dados.split()
print("Dados dos Arquivos: \n", dados)
print("\nQuantidade de caracteres: ", len(dados))
print("\nQuantidade de palavras: ", len (palavras))
arquivo.close()
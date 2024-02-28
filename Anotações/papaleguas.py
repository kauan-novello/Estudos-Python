# 2) A ACME Inc., uma empresa de 50 funcionários, 
# está tendo problemas deespaço em disco no seu servidor de arquivos (o HD tem tamanho de 500Gbytes). 
# As informações de utilização de HD dos usuários estão no arquivo"usuarios.txt" 
# que possui o seguinte formato (<nome>/<bytes>):Hortelino 45678653 Pernalonga 78545678 PapaLéguas 230943086....
# Você deve escrever um programa que lê este arquivo e gera um relatório,
# chamado "relatório.txt", no seguinte formato (<nome>/<Mbytes>/<% deuso de disco deste usuário>). 
# No fim do arquivo, escrever o total de espaçode disco ocupado em Megabytes e o “%” de uso total do disco

# R: usuario = open('usuarios.txt', 'r') 
# cria objeto de leitura relatorio = open('relatorio.txt', 'w') 
# cria objeto de escrita tamanho_HD = 500*1024 
# tamanho do disco em MBuso_total = 0 
# uso total em MB do disco for linha in usuario: 
# varre o arquivo usuarios.txt  linha = linha.split() 
# separa strings em lista  qtd_bytes = int(linha[1]) 
# quantidade de bytes em uso  qtd_MB = (qtd_bytes/1024)/1024 
# converte de bytes para MB  uso_total = uso_total + qtd_MB 
# incrementa uso total  perc_uso = qtd_MB/tamanho_HD 
# calcula percentual de uso  nome_str = linha[0] + " " 
# strin com nome e espaço  frelatorio.write(nome_str) 
# escreve no relatorio  qtd_MB_str = str( round(qtd_MB, 3) ) + "MB "   frelatorio.write(qtd_MB_str) 
# escreve uso do disco em MB  perc_uso_str = str( round(perc_uso, 5) ) + "%"   frelatorio.write(perc_uso_str) 
# escreve percentual de uso  frelatorio.write("\n") 
# quebra de linha frelatorio.write("\n") 
# quebra de linhauso_total_str = str( round(uso_total, 5) ) + "MB " frelatorio.write(uso_total_str) 
# escreve uso total do HD em MBperc_uso_total = uso_total/tamanho_HD 
# calcula percentual totalperc_uso_total_str = str( round(perc_uso_total, 5) ) + "%"frelatorio.write(perc_uso_total_str) 
# escreve percentual de uso totalfusuario.close() 
# encerrando a conexãofrelatorio.close() 
# com os arquivo
import os
os.system('cls')

usuario = open('usuarios.txt', 'r')
relatorio = open('relatorio.txt', 'w')
tamanho_HD = 500*1024 
MBuso_total = 0 

for linha in usuario:
    linha = linha.split()
    qtd_bytes = int(linha[1])
    qtd_MB = (qtd_bytes/1024)/1024
    uso_total = uso_total + qtd_MB
    perc_uso = qtd_MB/tamanho_HD
    nome_str = linha[0] + " "
    relatorio.write(nome_str)
    qtd_MB_str = str( round(qtd_MB, 3) ) + "MB "   
    relatorio.write(qtd_MB_str)
    relatorio.write("\n")
    MBperc_uso_total = uso_total/tamanho_HD
    totalperc_uso_total_str = str( round(uso_total, 5) ) + "%" 
    relatorio.write(uso_total)

usuario.close() 
relatorio.close() 

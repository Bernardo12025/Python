#Código2

with open('file_with_one_line_2.txt', 'a') as arquivo:
    linhas = arquivo.readlines()
    for linha in linhas:
        print(linha)
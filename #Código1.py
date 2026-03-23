#Código1

with open('file_with_one_line_2.txt', 'a') as arquivo:
    linha1 = arquivo.readline()
    print(linha1)

    linha2 = arquivo.readline()
    print(linha2)
#Manipulação de Ficheiros

with open('arquivo.txt', 'w') as file2:
    file2.write('Primeira linha de informação\n')


with open('arquivo.txt', 'r') as arquivo:
    linha1 = arquivo.readline()
    print(linha1)

    linha2 = arquivo.readline()
    print(linha2)

    linha3 = arquivo.readline()
    print(linha3)
    
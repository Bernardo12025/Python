#Mais Exercicios Chatos

with open('file_with_one_line_2.txt', 'w') as file1:
    file1.write('exemplo@dominio.com')

with open('file_with_one_line_2.txt', 'a') as arquivo:
    arquivo.write('\nLinha 4')
#Código3

with open('agenda.txt','r', encoding='utf=8') as ficheiro:
    for linha in ficheiro:
        if 'Ola' in linha:
            print(linha.rstrip())
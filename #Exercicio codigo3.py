#Exercicio codigo3

with open('Lista_idades.txt', 'w') as file1:
    file1.write('Nomes e Idades: ')

escolha = int(input("Escolha uma opção: 0-Sair 1-Cadastrar 2-Buscar ---> Opção Escolhida:"))

def nomes_e_idades():
    adicionar = input("Introduza o seu nome e idade para se cadastrar:")

    with open('Lista_idades.txt', 'a') as file1:
        file1.write(f'{adicionar}')

if escolha == 0:
    print("Obrigado por utilizar o programa!")
    
elif escolha == 1:
    nomes_e_idades()

elif escolha == 2:
    ficheiro_escolhido = input("Em que ficheiro deseja procurar?")

    buscar = input("Que palavra quer procurar nesse ficheiro?")
   
    with open(f'{ficheiro_escolhido}.txt','r', encoding='utf=8') as ficheiro:
     for linha in ficheiro:
        if f'{buscar}' in linha:
            print(linha.rstrip())

else:
    print("Opção Inválida!")
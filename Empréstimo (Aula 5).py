salario = int(input("Qual o seu salário?"))

anos = int(input("Em quantos anos pretende pagar a casa na totalidade?"))

totaldacasa = int(input("Qual o total da casa?"))

prestacao = (totaldacasa/(anos*12))

salariotrintaporcento = (salario*0.3)

print(f'A sua prestação é {prestacao}.')

if(prestacao>salariotrintaporcento):

    print("A prestação da casa é superior a 30% da casa.")

else:
    print("A prestação da casa é inferior a 30% da casa.")
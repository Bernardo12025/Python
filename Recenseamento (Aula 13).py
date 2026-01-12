from datetime import date
hoje = date.today().year
nascer = int(input("Introduz o teu ano de nascimento."))
idade = hoje - nascer
print(f'Você tem {idade} anos.')
if idade>=18 and idade<=21:
    print("Está no momento para o recenseamento.")
elif idade>21:
    print("Já passou o prazo para o recenseamento.")
elif idade<18:
    print("Ainda não tens idade para or recenseamento.")
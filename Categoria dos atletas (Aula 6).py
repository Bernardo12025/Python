from datetime import date

nascimento = int(input("Em que ano nasceste?"))

hoje = date.today().year

idade = (hoje - nascimento)

print(f'Tens {idade} anos.')

if idade <=9:

    print("És um Mirin.")

elif idade <=14:

    print("És um Infantil.")

elif idade <=19:

    print("És um Junior")

elif idade <=25:

    print("És um Senior.")

else:

    print("És um Master.")
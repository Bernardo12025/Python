ordenado = int(input("Qual o seu salário atual?"))

abaixo = (ordenado + (ordenado * 0.15))

meio = (ordenado + (ordenado * 0.10))

acima = (ordenado + (ordenado * 0.05))

if ordenado <500:

    print(f'O reajuste será de 15% e passará para {abaixo}.')

elif (ordenado >=500 and ordenado <=1000):

    print(f'O reajuste é de 10% e passará para {meio}.')

else:

    print(f'O reajuste é de 5% e passará para {acima}.')


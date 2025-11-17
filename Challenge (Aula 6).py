kWh = int(input("Qual a quantidade de kWh consumida?"))

print("R corresponde a residências, I corresponde a Indústrias e C corresponde a Comércios.")

tdi = input("Qual o tipo de instalação?")

if tdi == 'R':
    if kWh <= 500:

        print("O que o utilizador vai ter que pagar é", (kWh * 0.40) )

    else:
        print("O que o utilizador vai ter que pagar é", (kWh * 0.65))


elif tdi == 'I':
    if kWh <= 1000:

        print("O que o utilizador vai ter que pagar é", (kWh * 0.55))

    else:

        print("O que o utilizador vai ter que pagar é", (kWh * 0.60))

elif tdi == 'C':
    if kWh <= 5000:

        print("O que o utilizador vai ter que pagar é", (kWh * 0.55))

    else:

        print("O que o utilizador vai ter que pagar é", (kWh * 0.60))
else:
    print("dados incorretos")
marca = input("Diz uma marca de carro.")

if marca in ("Ford Chevrolet Dodge"):

    print(marca, "é Americana.")

elif marca in ("Honda Toyota Suzuki"):

    print(marca, "é Asiática.")

elif marca in ("BMW Peugeot Citroen"):

    print(marca, "é Europeia.")

else:

    print("Pedimos desculpa, essa marca não consta na nossa base de dados.")
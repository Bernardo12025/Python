velocidade = int(input("A que velocidade estava a andar?"))

if velocidade > 80:
	print("Estás acima do limite permitido. A multa foi gerada no valor de", ((velocidade - 80) * 2), "euros.")
else:10
	print("Dentro do limite. Boa viagem!")
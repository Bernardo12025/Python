import requests

print("=-=-=-=-=-=-=-=-=-=-")
print("")
print("Conversor de Moedas")
print("")
print("=-=-=-=-=-=-=-=-=-=-")

print("Qual a moeda de origem?")
print("0 - Euro")
print("1 - Dólar Americano")
print("2 - Real Brasileiro")
origem = int(input("Escolha a opção:"))

print("Para qual moeda deseja converter?")
print("0 - Euro")
print("1 - Dólar Americano")
print("2 - Real Brasileiro")
converter = int(input("Para qual moeda deseja converter?"))

valor = float(input("Que valor deseja converter?"))

if origem == 0 and converter == 1:
    url = requests.get('https://economia.awesomeapi.com.br/last/EUR-USD')
    cotacao = url.json()
    valor_conversao = float(cotacao['USDEUR']['bid'])
    conversao = valor/valor_conversao
    print(f'O seu valor convertido é {conversao}.')

elif origem == 0 and converter == 2:
    url = requests.get('https://economia.awesomeapi.com.br/last/EUR-BRL')
    cotacao = url.json()
    valor_conversao = float(cotacao['EURUSD']['bid'])
    conversao = valor/valor_conversao
    print(f'O seu valor convertido é {conversao}.')

elif origem == 1 and converter == 2:
    url = requests.get('https://economia.awesomeapi.com.br/last/USD-BRL')
    cotacao = url.json()
    valor_conversao = float(cotacao['EURUSD']['bid'])
    conversao = valor/valor_conversao
    print(f'O seu valor convertido é {conversao}.')    


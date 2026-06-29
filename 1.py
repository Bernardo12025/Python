import requests 

url = requests.get('https://economia.awesomeapi.com.br/last/EUR-USD')
cotacao = url.json()

cotacao_dolar = float(cotacao['EURUSD']['bid'])
quantidade = float(input("Quantos Dólares deseja converter?"))

conversao = quantidade/cotacao_dolar
print('O valor convertido é', (conversao))
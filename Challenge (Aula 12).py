import random

def sortear():
    lista_random = []
    for x in range(10):
        lista_random.append(random.randint(1,20))
    print("Os 10 valores sorteados foram:", lista_random)
    return lista_random

def somar_pares(lista_random):
    soma = 0
    for x in lista_random:
        if x % 2 == 0:
            soma += x
    print(f"A soma dos valores pares contidos na lista {lista_random} é {soma}.")

x = sortear()
somar_pares(x)
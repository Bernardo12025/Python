import random
x = random.randint(1,100)
y = int(input("Escolhe um número de 1 a 100."))
z = 0
while y != x:
    if y > x:
        print(f'O número está abaixo de {y}.')
    elif y < x:
        print(f'O número está acima de {y}.')
    y = int(input("Escolhe um número de 1 a 100."))
    z += 1
if y == x:
    z += 1
    print("Acertou!")
    print(f'Precisaste de {z} tentativas.')
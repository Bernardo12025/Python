import random

while True:
    dado1 = random.randint(1, 6)
    print(dado1)

    dado2 = random.randint(1, 6)
    print(dado2)

    if dado1 == dado2:
        print("Acabou!")
        break
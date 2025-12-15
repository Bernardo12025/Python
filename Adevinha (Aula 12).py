import random

adevinha = int(input("Introduz um número de 0 a 5."))

pensamento = random.randint(0, 5)
print(pensamento)

if adevinha == pensamento:
    print("Acertaste!")

else:
    print("Erraste!")
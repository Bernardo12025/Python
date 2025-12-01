a = int(input("Introduz um número."))
impar = 0
par = 0
while a != 0:
    if a % 2 != 0:
        impar += 1
        a = int(input("Introduz um número."))
    if a % 2 == 0:
        par += 1
        a = int(input("Introduz um número."))
print(f'Há {par} números pares e {impar} números impares.')
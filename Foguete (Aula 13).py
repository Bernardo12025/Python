from time import sleep

x = int(input("Introduz um número para começar a contagem decrescente."))
while x > 0:
    print(x)
    sleep(1)
    x-=1
    if x == 0:
        print("Descolou!")



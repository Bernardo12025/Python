conta = (input("Queres fazer uma adição, subtração, multiplicação ou divisão?"))
a = int(input("Introduz um valor."))
b = int(input("Introduz outro valor."))

def f1():
    r = a+b
    print(r)
def f2():
    r = a-b
    print(r)
def f3():
    r = a*b
    print(r)
def f4():
    r = a/b
    print(r)

if conta == 'adição':
    print(f1())

if conta == 'subtração':
    print(f2())

if conta == 'multiplicação':
    print(f3())

if conta == 'divisão':
    print(f4())
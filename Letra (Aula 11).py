frase = (input("Introduz uma frase."))
letra = (input("Introduz uma letra."))
y = 0
for x in frase:
    if x in letra:
            y += 1

print(f'A letra {letra} aparece {y} vezes na frase "{frase}"')



import random

ppt = ['Pedra', 'Papel', 'Tesoura']

player = (input("Pedra, Papel ou Tesoura?"))

jogo = random.choice(ppt)
print(jogo)

if jogo == player:
    print("Empate!")

elif jogo == "Pedra" and player == "Tesoura":
    print("Ganhou o PC!")

elif jogo == "Papel" and player == "Pedra":
    print("Ganhou o PC!")

elif jogo == "Tesoura" and player == "Papel":
    print("Ganhou o PC!")

elif jogo == "Papel" and player == "Tesoura":
    print("Ganhou o Player!")

elif jogo == "Pedra" and player == "Papel":
    print("Ganhou o Player!")

elif jogo == "Tesoura" and player == "Pedra":
    print("Ganhou o Player!")

while True:
    player = (input("Pedra, Papel ou Tesoura? (ou 'sair' para terminar): ").lower())

    if player == "sair":
        print("Obrigado por jogar!")
        break

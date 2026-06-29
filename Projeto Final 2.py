import tkinter as tk
import random

print("Que tema deseja jogar?")
print("A - Animais")
print("B - Meios de Transporte")
print("C - Jogadores")
tema = input("D - Países ")

if tema == "A":
    cartas_lista = ["Cão", "Gato", "Coelho", "Pássaro", "Peixe", "Porco", "Vaca", "Galinha"]

elif tema == "B":
    cartas_lista = ["Carro", "Mota", "Avião", "Barco", "Comboio", "Bicicleta", "Autocarro", "Helicóptero"]

elif tema == "C":
    cartas_lista = ["Ronaldo", "Messi", "Neymar", "Mbappé", "Haaland", "Salah", "Modric", "Vini Jr"]

elif tema == "D":
    cartas_lista = ["Portugal", "Espanha", "França", "Brasil", "Argentina", "Itália", "Alemanha", "Japão"]

else:
    print("Que tema deseja jogar?")
    print("A - Animais")
    print("B - Meios de Transporte")
    print("C - Jogadores")
    tema = input("D - Países ")
    

janela = tk.Tk()
janela.title("Jogo da Memória")

cartas = cartas_lista * 2
random.shuffle(cartas)

botoes = []
visiveis = [False] * 16

estado = {"primeiro": None, "bloqueado": False}

texto = tk.Label(janela, text="Encontra os pares!")
texto.grid(row=0, column=0, columnspan=4)


def esconder(carta1, carta2):
    botoes[carta1]["text"] = ""
    botoes[carta2]["text"] = ""

    estado["bloqueado"] = False
    texto["text"] = "Tenta novamente!"


def clicar(posicao):

    if estado["bloqueado"] or visiveis[posicao]:
        return

    botoes[posicao]["text"] = cartas[posicao]

    if estado["primeiro"] is None:
        estado["primeiro"] = posicao
        return

    if cartas[estado["primeiro"]] == cartas[posicao]:

        visiveis[estado["primeiro"]] = True
        visiveis[posicao] = True

        botoes[estado["primeiro"]]["state"] = "disabled"
        botoes[posicao]["state"] = "disabled"

        texto["text"] = "Par encontrado!"

        if all(visiveis):
            texto["text"] = "Ganhaste!"

    else:

        texto["text"] = "Erraste!"
        estado["bloqueado"] = True

        carta1 = estado["primeiro"]
        carta2 = posicao

        janela.after(1000, lambda: esconder(carta1, carta2))

    estado["primeiro"] = None


def recomecar():

    estado["primeiro"] = None
    estado["bloqueado"] = False

    for i in range(16):
        visiveis[i] = False
        botoes[i]["text"] = ""
        botoes[i]["state"] = "normal"

    texto["text"] = "Jogo reiniciado!"


def novo_tabuleiro():

    random.shuffle(cartas)
    recomecar()


for i in range(16):

    botao = tk.Button(janela, text="", width=12, height=4, command=lambda i=i: clicar(i))

    botao.grid(row=(i // 4) + 1, column=i % 4, padx=3, pady=3)

    botoes.append(botao)

tk.Button(janela, text="Recomeçar", command=recomecar).grid(row=5, column=0, columnspan=2)
tk.Button(janela, text="Novo Tabuleiro", command=novo_tabuleiro).grid(row=5, column=2, columnspan=2)

janela.mainloop()
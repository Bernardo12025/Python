import tkinter as tk
import random

janela = tk.Tk()
janela.title("Jogo da Memória")

cores_base = ["red", "blue", "green", "yellow", "orange", "purple", "cyan", "pink"]
cores = cores_base * 2
random.shuffle(cores)

botoes = []
visiveis = [False] * 16

estado = {"primeiro": None, "bloqueado": False}

texto = tk.Label(janela, text="Encontra os pares!")
texto.grid(row=0, column=0, columnspan=4)


def esconder(carta1, carta2):
    botoes[carta1]["bg"] = "lightgrey"
    botoes[carta2]["bg"] = "lightgrey"

    estado["bloqueado"] = False
    texto["text"] = "Tenta novamente!"


def clicar(posicao):

    if estado["bloqueado"] or visiveis[posicao]:
        return

    botoes[posicao]["bg"] = cores[posicao]

    if estado["primeiro"] is None:
        estado["primeiro"] = posicao
        return

    if estado["primeiro"] == posicao:
        return

    if cores[estado["primeiro"]] == cores[posicao]:

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

    for x in range(16):
        visiveis[x] = False
        botoes[x]["bg"] = "lightgrey"
        botoes[x]["state"] = "normal"

    texto["text"] = "Jogo reiniciado!"


def novo_tabuleiro():

    random.shuffle(cores)
    recomecar()


for x in range(16):

    botao = tk.Button(janela, width=8, height=4, bg="lightgrey", command=lambda x=x: clicar(x))

    botao.grid(row=(x // 4) + 1, column=x % 4, padx=3, pady=3)

    botoes.append(botao)

tk.Button(janela, text="Recomeçar", command=recomecar).grid(row=5, column=0, columnspan=2)
tk.Button(janela, text="Novo Tabuleiro", command=novo_tabuleiro).grid(row=5, column=2, columnspan=2)

janela.mainloop()

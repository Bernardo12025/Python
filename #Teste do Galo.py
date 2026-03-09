#Teste do Galo
# Jogo do Galo

import tkinter as tk
from tkinter import messagebox

def clicar(pos):
    global jogador_atual

    # Se o botão já estiver preenchido, não faz nada
    if board[pos] != '':
        return

    # Marca o botão
    board[pos] = jogador_atual
    buttons[pos].config(text=jogador_atual)

    # Verifica se há vencedor
    if verifica_vencedor():
        messagebox.showinfo("Fim do Jogo", f"O jogador {jogador_atual} venceu!")
        root.destroy()
        return

    # Verifica empate
    if '' not in board:
        messagebox.showinfo("Fim do Jogo", "Empate!")
        root.destroy()
        return

    # Troca de jogador
    jogador_atual = 'O' if jogador_atual == 'X' else 'X'


def verifica_vencedor():
    combinacoes = [
        [0,1,2], [3,4,5], [6,7,8],  # Linhas
        [0,3,6], [1,4,7], [2,5,8],  # Colunas
        [0,4,8], [2,4,6]            # Diagonais
    ]

    for comb in combinacoes:
        if board[comb[0]] == board[comb[1]] == board[comb[2]] != '':
            return True
    return False


# ---- Janela ----

root = tk.Tk()
root.title("Jogo do Galo")
root.geometry("475x475+400+100")
root.wm_resizable(width=False, height=False)

jogador_atual = 'X'
board = ['' for _ in range(9)]
buttons = []

for i in range(9):
    button = tk.Button(
        root,
        text='',
        font=('normal', 40),
        width=5,
        height=2,
        command=lambda i=i: clicar(i)
    )
    button.grid(row=i//3, column=i%3)
    buttons.append(button)

root.mainloop()
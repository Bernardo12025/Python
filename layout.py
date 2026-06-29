from tkinter import *
from tkinter import ttk

janela = Tk()
janela.title("Conversor")
janela.geometry("400x300")
janela.config(bg="white")

titulo = Label(
    janela,
    text="Conversor de Moedas",
    font=("Arial", 16),
    bg="white"
)

titulo.pack(pady=10)

lista_moedas = [
    "Euro",
    "Dólar Americano",
    "Real Brasileiro"
]

texto1 = Label(
    janela,
    text="Moeda de origem:",
    font=("Arial", 11),
    bg="white"
)

texto1.place(x=20, y=60)

origem = ttk.Combobox(
    janela,
    values=lista_moedas,
    width=20
)

origem.place(x=180, y=60)
origem.current(0)

texto2 = Label(
    janela,
    text="Converter para:",
    font=("Arial", 11),
    bg="white"
)

texto2.place(x=20, y=110)

destino = ttk.Combobox(
    janela,
    values=lista_moedas,
    width=20
)

destino.place(x=180, y=110)
destino.current(1)

texto3 = Label(
    janela,
    text="Valor:",
    font=("Arial", 11),
    bg="white"
)

texto3.place(x=20, y=160)

valor = Entry(
    janela,
    width=23
)

valor.place(x=180, y=160)

resultado = Label(
    janela,
    text="Resultado:",
    font=("Arial", 12),
    bg="white",
    fg="blue"
)

resultado.place(x=20, y=250)

botao = Button(
    janela,
    text="Converter",
    bg="lightblue"
)

botao.place(x=160, y=210)

janela.mainloop()
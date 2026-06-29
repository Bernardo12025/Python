from tkinter import *
from tkinter import ttk
import requests

janela = Tk()
janela.title("Conversor")
janela.geometry("400x300")
janela.config(bg="blue")

titulo = Label(janela, text="Conversor de Moedas", font=("Arial", 16), bg="blue")
titulo.pack(pady=10)

lista_moedas = ["EUR", "USD", "BRL"]

texto1 = Label(janela, text="Moeda de origem:",  bg="blue")
texto1.place(x=20, y=60)

origem = ttk.Combobox(janela, values=lista_moedas, width=20)
origem.place(x=180, y=60)
origem.current(0)

texto2 = Label(janela, text="Converter para:",  bg="blue")
texto2.place(x=20, y=110)

destino = ttk.Combobox(janela, values=lista_moedas, width=20)
destino.place(x=180, y=110)
destino.current(1)

texto3 = Label(janela, text="Valor:",  bg="blue")
texto3.place(x=20, y=160)

valor = Entry(janela, width=23)
valor.place(x=180, y=160)

resultado = Label(janela, text="Resultado:", bg="blue", fg="white")
resultado.place(x=20, y=250)

def converter():
    moeda1 = origem.get()
    moeda2 = destino.get()

    v = float(valor.get())

    codigos = {"Euro": "EUR", "Dólar Americano": "USD", "Real Brasileiro": "BRL"}

    codigo1 = codigos[moeda1]
    codigo2 = codigos[moeda2]

    link = f"https://economia.awesomeapi.com.br/last/{codigo1}-{codigo2}"

    pegar = requests.get(link)
    dados = pegar.json()

    chave = codigo1 + codigo2

    cotacao = float(dados[chave]["bid"])

    conta = v * cotacao

    resultado.config(text=f"Resultado: {conta} {codigo2}")

botao = Button(janela, text="Converter", command=converter, bg="white")
botao.place(x=160, y=210)

janela.mainloop()
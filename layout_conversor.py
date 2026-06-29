from tkinter import *
from tkinter import ttk
import requests

janela = Tk()
janela.title("Conversor")
janela.geometry("400x300")
janela.config(bg="white")

titulo = Label(janela, text="Conversor de Moedas", font=("Arial", 16), bg="white")
titulo.pack(pady=10)

lista_moedas = ["EUR", "USD", "BRL"]

Label(janela, text="Moeda de origem:", bg="white").place(x=20, y=60)

origem = ttk.Combobox(janela, values=lista_moedas, width=20)
origem.place(x=180, y=60)
origem.current(0)

Label(janela, text="Converter para:", bg="white").place(x=20, y=110)

destino = ttk.Combobox(janela, values=lista_moedas, width=20)
destino.place(x=180, y=110)
destino.current(1)

Label(janela, text="Valor:", bg="white").place(x=20, y=160)

valor = Entry(janela, width=23)
valor.place(x=180, y=160)

resultado = Label(janela, text="Resultado:", font=("Arial", 12), bg="white", fg="blue")
resultado.place(x=20, y=250)

def converter():
    try:
        codigo1 = origem.get()
        codigo2 = destino.get()

        v = float(valor.get())

        link = f"https://economia.awesomeapi.com.br/last/{codigo1}-{codigo2}"

        dados = requests.get(link).json()

        chave = f"{codigo1}{codigo2}"

        cotacao = float(dados[chave]["bid"])

        conta = v * cotacao

        resultado.config(text=f"Resultado: {conta} {codigo2}")

    except:
        resultado.config(text="Erro na conversão")

botao = Button(janela, text="Converter", command=converter, bg="lightblue")
botao.place(x=160, y=210)

janela.mainloop()
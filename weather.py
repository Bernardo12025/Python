from tkinter import *
import requests
from tkinter import messagebox
from datetime import datetime
from io import BytesIO
import tkinter as tk  

API_KEY = "3b3ddc5f98b8f6502b43eea92f40a73d"
BASE_URL = "http://api.openweathermap.org/data/2.5/weather"
ICON_URL = "http://openweathermap.org/img/wn/"

def obter_dados_meteorologicos(cidade):
   params = {
       'q': cidade,
       'appid': API_KEY,
       'units': 'metric',
       'lang': 'pt'
   }
   response = requests.get(BASE_URL, params=params)
   return response.json()

def guardar_histórico(cidade, temperatura):
   with open("Histórico.txt", "a") as ficheiro:
      data_hora = datetime.now()
      ficheiro.write({data_hora}, {cidade}, {temperatura})

def procurar_meterelogia():
    cidade = entrada_cidade.get()

    dados = obter_dados_meteorologicos(cidade)

    if dados:
        temperatura = dados["main"]["temp"]
        descricao = dados["weather"][0]["description"]
        humidade = dados["main"]["humidity"]
        vento = dados["wind"]["speed"]


janela = tk.Tk()
janela.title("App de Meteorologia")
janela.geometry("450x300")
janela.config(bg="#000000")

titulo = tk.Label(janela, text="Cidade/País:", font=(12), bg="#000000", fg="white")
titulo.pack(pady=20)

entrada_cidade = tk.Entry(janela, font=("Arial", 14), width=25,)
entrada_cidade.pack(pady=10)

botao = tk.Button(janela, text="Pesquisar", font=(12), bg="#ff6f00", fg="white", command=procurar_meterelogia)
botao.pack(pady=10)

janela.mainloop()
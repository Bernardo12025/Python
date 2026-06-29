import tkinter as tk
from PIL import Image, ImageTk


button2 = 7
button22 = 6
button23 = 6.5
button24 = 8
button25 = 7
button26 = 6.5
button27 = 5
button28 = 6
button29 = 6


button3 = 1
button31 = 3
button32 = 2.5
button33 = 2
button34 = 1.5
button35 = 1.5
button36 = 3.5
button37 = 3
button38 = 2.5
button39 = 2


imagens_sanduiches = {
    "Big Mac": "imagens/bigmac.png",
    "McVeggie": "imagens/mcveggie.png",
    "McCrispy": "imagens/mccrispy.png",
    "Big Arch": "imagens/bigarch.png",
    "McChicken": "imagens/mcchicken.png",
    "CBO": "imagens/cbo.png",
    "Cheeseburguer": "imagens/cheeseburger.png",
    "Big Tasty": "imagens/bigtasty.png",
    "McRoyal Bacon": "imagens/mcroyalbacon.png"
}

imagens_bebidas = {
    "Água": "imagens/agua.png",
    "Coca-Cola": "imagens/cocacola.png",
    "Fanta": "imagens/fanta.png",
    "Fuze Tea": "imagens/fuzetea.png",
    "Sumol": "imagens/sumol.png",
    "Bongo": "imagens/bongo.png",
    "Compal": "imagens/compal.png",
    "Cerveja": "imagens/cerveja.png",
    "Café": "imagens/cafe.png",
    "Chá": "imagens/cha.png"
}

pedido = {
    "sanduiche": "",
    "preco_sanduiche": 0,
    "bebida": "",
    "preco_bebida": 0
}


def pedido_final():
    return pedido["preco_sanduiche"] + pedido["preco_bebida"]


def escolher_sanduiche(nome, preco):
    pedido["sanduiche"] = nome
    pedido["preco_sanduiche"] = preco
    abrir_root3()


def escolher_bebida(nome, preco):
    pedido["bebida"] = nome
    pedido["preco_bebida"] = preco
    abrir_root4()



def abrir_root2():
    root2 = tk.Toplevel(root)
    root2.title("McMenu - Sanduíches")
    root2.geometry("1500x700")

    pastel = "#fdad6c"
    root2.configure(bg=pastel)

    tk.Button(
        root2,
        text="Big Mac",
        command=lambda: escolher_sanduiche("Big Mac", button2)
    ).place(x=120, y=100, width=300, height=75)

    tk.Button(
        root2,
        text="McVeggie",
        command=lambda: escolher_sanduiche("McVeggie", button22)
    ).place(x=120, y=250, width=300, height=75)

    tk.Button(
        root2,
        text="McCrispy",
        command=lambda: escolher_sanduiche("McCrispy", button23)
    ).place(x=120, y=400, width=300, height=75)

    tk.Button(
        root2,
        text="Big Arch",
        command=lambda: escolher_sanduiche("Big Arch", button24)
    ).place(x=500, y=100, width=300, height=75)

    tk.Button(
        root2,
        text="McChicken",
        command=lambda: escolher_sanduiche("McChicken", button25)
    ).place(x=500, y=250, width=300, height=75)

    tk.Button(
        root2,
        text="CBO",
        command=lambda: escolher_sanduiche("CBO", button26)
    ).place(x=500, y=400, width=300, height=75)

    tk.Button(
        root2,
        text="Cheeseburguer",
        command=lambda: escolher_sanduiche("Cheeseburguer", button27)
    ).place(x=880, y=100, width=300, height=75)

    tk.Button(
        root2,
        text="Big Tasty",
        command=lambda: escolher_sanduiche("Big Tasty", button28)
    ).place(x=880, y=250, width=300, height=75)

    tk.Button(
        root2,
        text="McRoyal Bacon",
        command=lambda: escolher_sanduiche("McRoyal Bacon", button29)
    ).place(x=880, y=400, width=300, height=75)


def abrir_root3():
    root3 = tk.Toplevel(root)
    root3.title("McMenu - Bebidas")
    root3.geometry("1500x700")

    light_brown = "#815a3a"
    root3.configure(bg=light_brown)

    tk.Button(
        root3,
        text="Proceder (Água) ->",
        command=lambda: escolher_bebida("Água", button3)
    ).place(x=1150, y=550, width=120, height=30)

    tk.Button(
        root3,
        text="Coca-Cola",
        command=lambda: escolher_bebida("Coca-Cola", button31)
    ).place(x=120, y=100, width=300, height=75)

    tk.Button(
        root3,
        text="Fanta",
        command=lambda: escolher_bebida("Fanta", button32)
    ).place(x=120, y=250, width=300, height=75)

    tk.Button(
        root3,
        text="Fuze Tea",
        command=lambda: escolher_bebida("Fuze Tea", button33)
    ).place(x=120, y=400, width=300, height=75)

    tk.Button(
        root3,
        text="Sumol",
        command=lambda: escolher_bebida("Sumol", button34)
    ).place(x=500, y=100, width=300, height=75)

    tk.Button(
        root3,
        text="Bongo",
        command=lambda: escolher_bebida("Bongo", button35)
    ).place(x=500, y=250, width=300, height=75)

    tk.Button(
        root3,
        text="Compal",
        command=lambda: escolher_bebida("Compal", button36)
    ).place(x=500, y=400, width=300, height=75)

    tk.Button(
        root3,
        text="Cerveja",
        command=lambda: escolher_bebida("Cerveja", button37)
    ).place(x=880, y=100, width=300, height=75)

    tk.Button(
        root3,
        text="Café",
        command=lambda: escolher_bebida("Café", button38)
    ).place(x=880, y=250, width=300, height=75)

    tk.Button(
        root3,
        text="Chá",
        command=lambda: escolher_bebida("Chá", button39)
    ).place(x=880, y=400, width=300, height=75)


def abrir_root4():
    root4 = tk.Toplevel(root)
    root4.title("Pagamento")
    root4.geometry("1500x700")

    blue = "#0084ff"
    root4.configure(bg=blue)

    tk.Label(
        root4,
        text="Sanduíche: " + pedido["sanduiche"],
        font=("Arial", 20),
        bg=blue,
        fg="white"
    ).place(x=550, y=180)

    tk.Label(
        root4,
        text="Bebida: " + pedido["bebida"],
        font=("Arial", 20),
        bg=blue,
        fg="white"
    ).place(x=550, y=250)

    tk.Label(
        root4,
        text="Total: " + str(pedido_final()) + " €",
        font=("Arial", 24),
        bg=blue,
        fg="white"
    ).place(x=550, y=330)

    try:
        img_sanduiche = Image.open(
            imagens_sanduiches[pedido["sanduiche"]]
        )

        img_sanduiche = img_sanduiche.resize((250, 200))

        foto_sanduiche = ImageTk.PhotoImage(img_sanduiche)

        lbl_sanduiche = tk.Label(
            root4,
            image=foto_sanduiche,
            bg=blue
        )

        lbl_sanduiche.image = foto_sanduiche
        lbl_sanduiche.place(x=120, y=180)

    except:
        pass

    try:
        img_bebida = Image.open(
            imagens_bebidas[pedido["bebida"]]
        )

        img_bebida = img_bebida.resize((180, 220))

        foto_bebida = ImageTk.PhotoImage(img_bebida)

        lbl_bebida = tk.Label(
            root4,
            image=foto_bebida,
            bg=blue
        )

        lbl_bebida.image = foto_bebida
        lbl_bebida.place(x=1100, y=180)

    except:
        pass

    tk.Button( root4, text="Finalizar ->", command=abrir_root5).place(x=1150,  y=550,  width=100,  height=25)


def abrir_root5():
    root5 = tk.Toplevel(root)
    root5.title("Até à Próxima!")
    root5.geometry("1500x700")

    white = "#F1F1F1"
    root5.configure(bg=white)

    tk.Label(root5, text="Finalizado, obrigado!", font=("Arial", 20)).place(x=525, y=250, width=250, height=75)


root = tk.Tk()
root.title("McDonald's")
root.geometry("1500x700")

bright_red = "#fd6c6c"
root.configure(bg=bright_red)

tk.Label(root, text="Bem Vindo!", font=("Arial", 20), bg=bright_red).place(x=525, y=150, width=250, height=75)

tk.Button(root, text="McMenu", command=abrir_root2).place(x=520, y=250, width=250, height=75)

root.mainloop()
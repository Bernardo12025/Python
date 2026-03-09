import tkinter as tk  

def mudar_para_cinzento_claro():
    root.configure(bg="#d1d1d1")
    label.config(text="Cinzento Claro", bg="#d1d1d1", fg="black")
   
def mudar_para_cinzento_escuro():
    root.configure(bg="#3f3f3f")
    label.config(text="Cinzento Escuro", bg="#3f3f3f", fg="white")

def mudar_para_cinzento():
    root.configure(bg="grey")
    label.config(text="Cinzento", bg="grey", fg="black")
   
def mudar_para_preto():
    root.configure(bg="black")
    label.config(text="Preto", bg="black", fg="white")
   
root = tk.Tk()
root.title("Cores")
root.geometry("500x400+400+100")
root.wm_resizable(width=False, height=False)

button1 = tk.Button(root, text="Cinzento Claro", command=mudar_para_cinzento_claro)
button1.place(width=200, height=160, x=140, y=100, anchor="center")

button2 = tk.Button(root, text="Cinzento Escuro", command=mudar_para_cinzento_escuro)
button2.place(width=200, height=160, x=140, y=300, anchor="center")

button3 = tk.Button(root, text="Cinzento", command=mudar_para_cinzento)
button3.place(width=200, height=160, x=360, y=100, anchor="center")

button4 = tk.Button(root, text="Preto", command=mudar_para_preto)
button4.place(width=200, height=160, x=360, y=300, anchor="center")

label = tk.Label(root, text="", font=("Arial", 14))
label.place(x=250, y=200, anchor="c")

root.mainloop()
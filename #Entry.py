#Código Lista telefónica
from tkinter import *

from tkinter import messagebox
 
 
# -------------------------------------------------------------
 
# cor
 
branco = '#ffffff'

azul = '#364a85'

vermelho = '#b53128'

amarelo = '#ffef08'
 
 
# -------------------------------------------------------------
 
# tela

tela1 = Tk()

tela1.title('Agenda')

tela1.geometry('380x500+500+100')

tela1.wm_resizable(width=False, height=False)
 
# labels e entrys
 
lb_agenda = Label(tela1, text='Sharkcoders Python', font='Time 20 bold', bg=amarelo, fg=vermelho, anchor='w', padx=10)

lb_agenda.place(width=380, height=50, x=0, y=0, )
 
lb_nome = Label(tela1, text='Nome', font='Time 10', anchor='w')

lb_nome.place(width=60, height=20, x=10, y=70)

input_nome = Entry(tela1, font='Time 10')

input_nome.place(width=250, height=20, x=100, y=70)
 
lb_tel = Label(tela1, text='Telemóvel', font='Time 10', anchor='w')

lb_tel.place(width=60, height=20, x=10, y=110)

input_tel = Entry(tela1, font='Time 10')

input_tel.place(width=250, height=20, x=100, y=110)
 
lb_end = Label(tela1, text='Endereço', font='Time 10', anchor='w')

lb_end.place(width=60, height=20, x=10, y=170)

input_end = Entry(tela1, font='Time 10')

input_end.place(width=250, height=20, x=100, y=170)
 
lb_dist = Label(tela1, text='Distrito', font='Time 10', anchor='w')

lb_dist.place(width=60, height=20, x=10, y=210)

input_dist = Entry(tela1, font='Time 10')

input_dist.place(width=80, height=20, x=100, y=210)
 
lb_pais = Label(tela1, text='País', font='Time 10', anchor='w')

lb_pais.place(width=60, height=20, x=210, y=210)

input_pais = Entry(tela1, font='Time 10')

input_pais.place(width=80, height=20, x=270, y=210)
 
lb_email = Label(tela1, text='Email', font='Time 10', anchor='w')

lb_email.place(width=60, height=20, x=10, y=270)

input_email = Entry(tela1, font='Time 10')

input_email.place(width=250, height=20, x=100, y=270)
 
# -------------------------------------------------------------
 
# funções
 
 
def adicionar():
 
    nome = input_nome.get()

    tel = input_tel.get()

    end = input_end.get()

    dist = input_dist.get()

    pais = input_pais.get()

    email = input_email.get()
 
    with open('agenda.txt', 'a') as arquivo:

        arquivo.write(nome + '\n' + tel + '\n' + end + '\n' + dist + '\n' + pais + '\n' + email + '\n')
 
    messagebox.showinfo('Agenda','Cadastro Efetuado com Sucesso!')
 
    input_nome.delete('0', 'end')

    input_tel.delete('0', 'end')

    input_end.delete('0', 'end')

    input_dist.delete('0', 'end')

    input_pais.delete('0', 'end')

    input_email.delete('0', 'end')
 
 
def procurar():
 
    nome = input_nome.get()
 
    with open('agenda.txt', 'r') as arquivo:

        for linha in arquivo:

            if nome in linha:

                a_tel = (arquivo.readline())

                b_end = (arquivo.readline())

                c_dist = (arquivo.readline())

                d_pais = (arquivo.readline())

                e_email = (arquivo.readline())
 
                l_nome_busca = Label(tela1, text=linha, font='Times 10', anchor='w')

                l_nome_busca.place(width=250, height=30, x=20, y=360)

                l_tel_busca = Label(tela1, text=a_tel, font='Times 10', anchor='w')

                l_tel_busca.place(width=250, height=30, x=20, y=380)

                l_end_busca = Label(tela1, text=b_end, font='Times 10', anchor='w')

                l_end_busca.place(width=250, height=30, x=20, y=400)

                l_dist_busca = Label(tela1, text=c_dist, font='Times 10', anchor='w')

                l_dist_busca.place(width=100, height=30, x=20, y=420)

                l_pais_busca = Label(tela1, text=d_pais, font='Times 10', anchor='w')

                l_pais_busca.place(width=250, height=30, x=20, y=440)

                l_email_busca = Label(tela1, text=e_email, font='Times 10', anchor='w')

                l_email_busca.place(width=250, height=30, x=20, y=460)

            else:

                messagebox.showerror('Agenda', 'Cadastro não encontrado!')

                break
 
 
# -------------------------------------------------------------

# botões
 
b_adicionar = Button(tela1, text='Adicionar', command=adicionar, font='Time 10 bold', bg=azul, fg=branco)

b_adicionar.place(width=80, height=30, x=70, y=310)
 
b_procurar = Button(tela1, text='Pesquisar', command=procurar, font='Time 10 bold', bg=azul, fg=branco)

b_procurar.place(width=80, height=30, x=240, y=310)
 
# -------------------------------------------------------------

tela1.mainloop()
 
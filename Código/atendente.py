from tkinter import *
from tkinter.ttk import *

def show_frame():
    frame = Tk()

    title = Label(frame, text="Venda de Ingressos", font=("Arial", 24))
    title.grid(row=0, column=0, columnspan=3, padx=100, pady=30)

    filme = Label(frame, text="Filme:", font=("Arial", 14))
    filme.grid(row=1, column=0,)

    sessao = Label(frame, text="Sessão:", font=("Arial", 14))
    sessao.grid(row=1, column=1)

    poltronas = Label(frame, text="Poltronas:", font=("Arial", 14))
    poltronas.grid(row=1, column=2)

    scroll = Scrollbar(frame, orient='vertical')

    list_filmes = Listbox(frame, font=("Arial",14), width=10, height=5, selectmode='BROWSE', yscrollcommand=scroll.set)
    list_filmes.grid(row=2, column=0)

    scroll.config(command=list_filmes.yview)
    scroll.grid(row=2, column=1)


    frame.title("Cinema 1.0")
    frame.geometry("500x500+500+300")

    frame.mainloop()
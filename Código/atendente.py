from tkinter import *
from functools import partial
import sqlite3

def plot_filmes(list):
    conn = sqlite3.connect('dados/database.db')
    c = conn.cursor()
    c.execute('SELECT * FROM filmes')
    filmes = c.fetchall()

    for item in filmes:
        list.insert(END, item[0])

def on_select(list_filmes, sessao, sala, poltronas, event):
    sessao['text'] = ""
    sala['text'] = ""

    sel = str((list_filmes.get(list_filmes.curselection())))
    conn = sqlite3.connect('dados/database.db')
    c = conn.cursor()
    c.execute('SELECT * FROM filmes WHERE titulo=?', (sel,))
    result = c.fetchone()
    sessao["text"] = result[3]
    sala["text"] = result[4]

    c.execute('SELECT livres FROM poltronas WHERE sala=?', (result[4],))
    result = c.fetchone()
    poltronas["text"] = result

def show_frame():
    frame = Tk()

    title = Label(frame, text="Venda de Ingressos", font=("Arial", 24))
    title.grid(row=0, column=0, columnspan=4, padx=110, pady=30)

    # Filme
    filme_label = Label(frame, text="Filme", font=("Arial", 12))
    filme_label.grid(row=1, column=0, pady=5, columnspan=3)

    # Sessão
    sessao_label = Label(frame, text="Sessão", font=("Arial", 12))
    sessao_label.grid(row=5, column=0, padx=30, pady=(15,0))
    sessao = Label(frame, text="", font=("Arial", 12, "bold"))
    sessao.grid(row=6, column=0, sticky=N)

    # Sala
    sala_label = Label(frame, text="Sala", font=("Arial", 12))
    sala_label.grid(row=5, column=1, padx=80, pady=(15,0))
    sala = Label(frame, text="", font=("Arial", 12, "bold"))
    sala.grid(row=6, column=1, sticky=N)

    # Poltronas
    poltronas_label = Label(frame, text="Poltronas Livres", font=("Arial", 12))
    poltronas_label.grid(row=5, column=2, pady=(15,0))
    poltronas = Label(frame, text="", font=("Arial", 12, "bold"))
    poltronas.grid(row=6, column=2, sticky=N)

    # Scroll Lista Filmes
    scroll = Scrollbar(frame)
    scroll.grid(row=2, column=3, rowspan=2, padx=0, sticky=N+S+W)

    # Lista Filmes
    list_filmes = Listbox(frame, font=("Arial", 12, "bold"), width=50, height=5, activestyle='dotbox')
    list_filmes.grid(row=2, column=0, rowspan=2, columnspan=3, sticky=E)
    plot_filmes(list_filmes)

    list_filmes.config(yscrollcommand=scroll.set)
    scroll.config(command=list_filmes.yview)

    list_filmes.bind("<<ListboxSelect>>", partial(on_select, list_filmes, sessao, sala, poltronas))

    # Poltrona Selecionada
    selecionada_label = Label(frame, text="Poltrona", font=("Arial", 12))
    selecionada_label.grid(row=7, column=2, pady=(15,0), sticky=N)
    selecionada = Label(frame, text="--", font=("Arial", 12))
    selecionada.grid(row=8, column=2, sticky=N)

    # Botão Selecionar Poltrona
    poltrona_sel = Button(frame, text="Selecionar Poltrona", font=("Arial", 12))
    poltrona_sel.grid(row=9, column=2)

    frame.title("Gerenciamento de Cinema")
    frame.geometry("510x500+500+300")

    frame.mainloop()
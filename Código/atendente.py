from tkinter import *
from functools import partial
from tkinter import messagebox
import sqlite3

def sair_click(frame, selecionada, sala):
    if selecionada["text"] == "Não Selecionada":
        frame.destroy()
    else:
        conn = sqlite3.connect('dados/database.db')
        c = conn.cursor()
        poltrona = "poltrona"+selecionada["text"]
        c.execute('UPDATE poltronas SET {}=? WHERE sala=?'.format(poltrona), (0, sala["text"]))
        conn.commit()
        frame.destroy()

def confirmar_selecao(frame, conn, sel, selecionada):
    selecionada["text"] = sel["text"]
    if sel["text"] == "":
        selecionada["text"] = "Não Selecionada"
    conn.commit()
    frame.destroy()

def plot_filmes(list):
    conn = sqlite3.connect('dados/database.db')
    c = conn.cursor()
    c.execute('SELECT * FROM filmes')
    filmes = c.fetchall()

    for item in filmes:
        list.insert(END, item[0])

def set_valor(opt, valor):
    if opt.get() == "Inteira":
        valor["text"] = "R$ 20,00"
    elif opt.get() == "Meia":
        valor["text"] = "R$ 10,00"
    else:
        valor["text"] = "R$ 00,00"


def on_select(list_filmes, sessao, sala, poltronas, poltrona_sel, event):
    sessao['text'] = ""
    sala['text'] = ""
    poltrona_sel["state"] = NORMAL

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

def sel_poltrona(frame, sala, selecionada):
    conn = sqlite3.connect('dados/database.db')
    action = Toplevel(frame)
    #frame.iconify()
    Label(action, text="Selecionar Poltrona", font=("Arial", 24)).grid(row=0, column=0, columnspan=50, pady=(20,0))
    Label(action, text="Sala: "+sala["text"], font=("Arial", 14)).grid(row=1, column=0, columnspan=50, pady=(10,30))
    Label(action, text="TELA", bg="gray75", font=("Arial", 12, "bold")).grid(row=2, column=0, columnspan=50)

    sel_label = Label(action, text="Poltrona Selecionada", font=("Arial", 12))
    sel_label.grid(row=8, column=3, columnspan=4, pady=(20, 0))
    sel = Label(action, text=selecionada["text"], font=("Arial", 12, "bold"))
    sel.grid(row=9, column=4, columnspan=2)

    line=3
    col=0
    for index in range(1,51):
        pol = Button(action, text=str(index), font=("Arial", 12, "bold"))
        verifica_poltrona(conn, sala, pol)
        pol["command"] = partial(situacao, conn, sala, pol, sel, action)
        pol.grid(row=line, column=col, ipadx=7, ipady=5, padx=10, pady=10, sticky=W + E)
        if index%10==0:
            line = line+1
            col = 0
        else:
            col = col+1

    confirmar = Button(action, bg="gray75", text="Confirmar", font=("Arial", 14, "bold"))
    confirmar["command"] = partial(confirmar_selecao, action, conn, sel, selecionada)
    confirmar.grid(row=10, column=3, columnspan=2, padx=3, pady=(20, 0), sticky=E)

    cancelar = Button(action, bg="gray75", text="Cancelar", font=("Arial", 14), command=action.destroy)
    cancelar.grid(row=10, column=5, columnspan=2, padx=3, pady=(20, 0), ipadx=10, sticky=W)

    action.geometry("670x610+500+210")
    action.iconbitmap(r'icon.ico')

def verifica_poltrona(conn, sala, pol):
    c = conn.cursor()
    poltrona = "poltrona" + pol["text"]
    c.execute('SELECT {} FROM poltronas WHERE sala=?'.format(poltrona), (sala["text"],))
    result = c.fetchone()

    if result[0] == 0:
        pol["bg"] = "green"
    elif result[0] == 1:
        pol["bg"] = "red"
    elif result[0] == 2:
        pol["bg"] = "blue"

def situacao(conn, sala, pol, sel, action):
    c = conn.cursor()
    poltrona = "poltrona"+pol["text"]
    c.execute('SELECT {} FROM poltronas WHERE sala=?'.format(poltrona), (sala["text"],))
    result = c.fetchone()

    if result[0]==0:
        if sel["text"] != "Não Selecionada":
            messagebox.showinfo("Seleção de Poltrona", "Desmarque a poltrona já selecionada! (Apenas uma poltrona por venda)", parent=action)
        else:
            c.execute('UPDATE poltronas SET {} = ? WHERE sala=?'.format(poltrona), (2, sala["text"]))
            pol["bg"] = "blue"
            sel["text"] = pol["text"]
    elif result[0]==2:
        c.execute('UPDATE poltronas SET {} = ? WHERE sala=?'.format(poltrona), (0, sala["text"]))
        pol["bg"] = "green"
        sel["text"] = "Não Selecionada"

def venda_ingresso(frame, list_filmes, sessao, sala, selecionada, opt, poltronas):
    if opt.get() == "NULL" or selecionada["text"] == "Não Selecionada":
        messagebox.showinfo("Erro", "Preencha todas as informações!")
    else:
        conn = sqlite3.connect('dados/database.db')
        c = conn.cursor()
        sel = str(list_filmes.get(list_filmes.curselection()))
        c.execute('INSERT INTO vendas (filme, sessao, sala, poltrona, ingresso) VALUES(?, ?, ?, ?, ?)',
                  (sel, sessao["text"], sala["text"], selecionada["text"], opt.get()))

        poltrona = "poltrona"+selecionada["text"]
        livres = int(poltronas["text"])
        livres = livres-1
        c.execute('UPDATE poltronas SET {} = ? WHERE sala = ?'.format(poltrona), (1, sala["text"]))
        c.execute('UPDATE poltronas SET livres = ? WHERE sala = ?', (livres, sala["text"]))
        conn.commit()
        ingresso = open("ingresso/ingresso.txt", "w+")
        ingresso.write("FILME: "+sel+"\n"+"SESSÃO: "+sessao["text"]+"\n"+"SALA: "+sala["text"]+"\n"+
                       "POLTRONA: "+selecionada["text"]+"\n"+"INGRESSO: "+opt.get())
        ingresso.close()
        messagebox.showinfo("Venda Finalizada", "Ingresso Emitido")
        frame.destroy()
        show_frame()

def show_frame():
    frame = Tk()

    title = Label(frame, text="Venda de Ingressos", font=("Arial", 24))
    title.grid(row=0, column=0, columnspan=4, padx=110, pady=30)

    # Filme
    filme_label = Label(frame, text="Selecione um Filme", font=("Arial", 12))
    filme_label.grid(row=1, column=0, pady=5, columnspan=3)

    # Sessão
    sessao_label = Label(frame, text="Sessão", font=("Arial", 12))
    sessao_label.grid(row=5, column=0, padx=20, pady=(15,0))
    sessao = Label(frame, text="", font=("Arial", 12, "bold"))
    sessao.grid(row=6, column=0, sticky=N, pady=(0,20))

    # Sala
    sala_label = Label(frame, text="Sala", font=("Arial", 12))
    sala_label.grid(row=5, column=1, padx=80, pady=(15,0))
    sala = Label(frame, text="", font=("Arial", 12, "bold"))
    sala.grid(row=6, column=1, sticky=N, pady=(0,20))

    # Poltronas
    poltronas_label = Label(frame, text="Poltronas Livres", font=("Arial", 12))
    poltronas_label.grid(row=5, column=2, padx=15, pady=(15,0))
    poltronas = Label(frame, text="", font=("Arial", 12, "bold"))
    poltronas.grid(row=6, column=2, sticky=N, pady=(0,20))

    # Scroll Lista Filmes
    scroll = Scrollbar(frame)
    scroll.grid(row=2, column=3, rowspan=2, padx=0, sticky=N+S+W)

    # Lista Filmes
    list_filmes = Listbox(frame, font=("Arial", 12, "bold"), width=56, height=5, activestyle='dotbox')
    list_filmes.grid(row=2, column=0, rowspan=2, columnspan=3, sticky=E)
    plot_filmes(list_filmes)

    # Poltrona Selecionada
    selecionada_label = Label(frame, text="Poltrona", font=("Arial", 12))
    selecionada_label.grid(row=7, column=1, sticky=N)
    selecionada = Label(frame, text="Não Selecionada", font=("Arial", 12, "bold"))
    selecionada.grid(row=8, column=1, sticky=N)

    # Botão Selecionar Poltrona
    poltrona_sel = Button(frame, bg="gray75", text="Selecionar Poltrona", font=("Arial", 12), state=DISABLED)
    poltrona_sel["command"] = partial(sel_poltrona, frame, sala, selecionada)
    poltrona_sel.grid(row=9, column=1)

    # Finalização da Venda
    valor_label = Label(frame, text="Valor", font=("Arial", 12))
    valor_label.grid(row=7, column=2, sticky=N)
    valor = Label(frame, text="R$ 00,00", font=("Arial", 12, "bold"))
    valor.grid(row=8, column=2, sticky=N)

    # Opção de Ingresso
    opt = StringVar()
    opt.set("NULL")
    inteira = Radiobutton(frame, text="Inteira", font=("Arial", 12, "bold"), variable=opt, value="Inteira")
    inteira["command"] = partial(set_valor, opt, valor)
    inteira.grid(row=7, column=0, ipadx=30, sticky=W+S)
    meia = Radiobutton(frame, text="Meia", font=("Arial", 12, "bold"), variable=opt, value="Meia")
    meia["command"] = partial(set_valor, opt, valor)
    meia.grid(row=8, column=0, ipadx=30, sticky=W)
    npagante = Radiobutton(frame, text="Não-Pagante", font=("Arial", 12, "bold"), variable=opt, value="Não-Pagante")
    npagante["command"] = partial(set_valor, opt, valor)
    npagante.grid(row=9, column=0, ipadx=30, sticky=W)

    # Botão Confirmar Venda
    confirmar_venda = Button(frame, bg="gray75", text="Confirmar", font=("Arial", 12, "bold"))
    confirmar_venda["command"] = partial(venda_ingresso, frame, list_filmes, sessao, sala, selecionada, opt, poltronas)
    confirmar_venda.grid(row=9, column=2, ipadx=10, sticky=N)

    # Botão Sair
    sair = Button(frame, text="Sair", font=("Arial", 12))
    sair["command"] = partial(sair_click, frame, selecionada, sala)
    sair.grid(row=10, column=2, sticky=N, ipadx=35, pady=(15,0))

    # Configurações do Scroll da Lista de Filmes
    list_filmes.config(yscrollcommand=scroll.set)
    scroll.config(command=list_filmes.yview)

    list_filmes.bind("<<ListboxSelect>>", partial(on_select, list_filmes, sessao, sala, poltronas, poltrona_sel))

    frame.title("Gerenciamento de Cinema")
    frame.geometry("580x480+500+200")
    frame.iconbitmap(r'icon.ico')

    frame.mainloop()
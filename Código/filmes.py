from tkinter import *
from functools import partial
from tkinter import messagebox
import gestor
import sqlite3

def voltar_click(frame, ctrl):
    frame.destroy()

    if ctrl==0:
        gestor.show_frame()
    else:
        show_frame()

def registrar(frame, titulo, genero, clas, hora_h, hora_min, sala):
    hora = hora_h.get()+":"+hora_min.get()

    conn = sqlite3.connect('dados/database.db')
    c = conn.cursor()
    c.execute('SELECT * FROM salas WHERE sala=?', (sala.get()))
    result = c.fetchone()

    if result is not None and result[1]=="Livre":
        c.execute('INSERT INTO filmes (titulo, genero, classificacao, horario, sala) VALUES(?, ?, ?, ?, ?)',
                 (titulo.get(), genero.get(), clas.get(), hora, sala.get()))

        c.execute('UPDATE salas SET status=?, filme=? WHERE sala=?', ("Em uso", titulo.get(), sala.get()))

        conn.commit()
        messagebox.showinfo("Cadastro de Filmes", "Filme cadastrado com sucesso!")
        voltar_click(frame, 1)
    else:
        messagebox.showinfo("Erro", "Sala em uso ou inexistente!")

def consultar(titulo, genero, clas, horario, sala):
    genero["text"] = ""
    clas["text"] = ""
    horario["text"] = ""
    sala["text"] = ""

    conn = sqlite3.connect('dados/database.db')
    c = conn.cursor()
    c.execute('SELECT * FROM filmes WHERE titulo=?', (titulo.get(),))
    result = c.fetchone()
    if result is not None:
        genero["text"] = result[1]
        clas["text"] = result[2]
        horario["text"] = result[3]
        sala["text"] = result[4]
        return 1
    else:
        messagebox.showinfo("Consulta de filmes", "Nenhum filme encontrado!")
        return 0

def encontrar(titulo, genero, clas, horario, sala, excluir):
    if consultar(titulo, genero, clas, horario, sala) == 1:
        excluir["state"] = NORMAL
    else:
        excluir["state"] = DISABLED

def deletar(titulo, genero, clas, horario, sala, excluir):
    conn = sqlite3.connect('dados/database.db')
    c = conn.cursor()

    result = messagebox.askyesno("Exclusão de Filmes", "Confirmar exclusão do filme?")
    if result:
        c.execute('UPDATE salas SET status=?, filme=? WHERE sala=?', ("Livre", None, sala["text"]))
        c.execute('DELETE FROM filmes WHERE titulo=?', (titulo.get(),))
        conn.commit()

        messagebox.showinfo("Exclusão de filmes", "Filme excluído com sucesso!")
    else:
        messagebox.showinfo("Exclusão de Filmes", "Exclusão cancelada")

    titulo["text"] = ""
    genero["text"] = ""
    clas["text"] = ""
    horario["text"] = ""
    sala["text"] = ""
    excluir["state"] = DISABLED

def cadastrar_click(frame):
    frame.destroy()
    action = Tk()
    Label(action, text="Cadastrar Filme", font=("Arial", 24)).grid(row=0, column=1, columnspan=3, ipadx=80, pady=20)

    #Título do filme
    titulo_label = Label(action, text="Título:", font=("Arial", 12))
    titulo_label.grid(row=1, column=0, pady=5)
    titulo = Entry(action, font=("Arial", 12))
    titulo.grid(row=1, column=1, columnspan=3, sticky=W+E)

    #Gênero do filme
    genero_label = Label(action, text="Gênero:", font=("Arial", 12))
    genero_label.grid(row=2, column=0, pady=(5,10))
    genero = Entry(action, font=("Arial", 12))
    genero.grid(row=2, column=1, columnspan=3, sticky=W+E)

    #Opções de Classificação
    clas_label = Label(action, text="Idade:", font=("Arial", 12))
    clas_label.grid(row=3, column=0)
    opt = StringVar()
    opt.set(" ")
    clas_livre = Radiobutton(action, text="Livre", variable=opt, value="Livre")
    clas_livre.grid(row=3, column=1, sticky=W)
    clas_10 = Radiobutton(action, text="10 anos", variable=opt, value="10 anos")
    clas_10.grid(row=4, column=1, sticky=W)
    clas_12 = Radiobutton(action, text="12 anos", variable=opt, value="12 anos")
    clas_12.grid(row=5, column=1, sticky=W)
    clas_16 = Radiobutton(action, text="16 anos", variable=opt, value="16 anos")
    clas_16.grid(row=6, column=1, sticky=W)
    clas_18 = Radiobutton(action, text="18 anos", variable=opt, value="18 anos")
    clas_18.grid(row=7, column=1, sticky=W)

    #Horário de exibição
    hora_label = Label(action, text="Horário:", font=("Arial", 12))
    hora_label.grid(row=8, column=0, pady=5)
    hora_h = Spinbox(action, font=("Arial", 12), from_=0, to=23, format="%02.0f", state="readonly", width=2)
    hora_h.grid(row=8, column=1, sticky=W)
    hora_min = Spinbox(action, font=("Arial", 12), from_=0, to=59, format="%02.0f", state="readonly", width=2)
    hora_min.grid(row=8, column=1)

    #Sala de Exibição
    sala_label = Label(action, text="Sala:", font=("Arial", 12))
    sala_label.grid(row=9, column=0, pady=(10,5))
    sala = Entry(action, font=("Arial", 12))
    sala.grid(row=9, column=1, columnspan=3, sticky=W)

    #Botão confirmar
    confirmar = Button(action, bg="gray75", text="Confirmar", font=("Arial", 12))
    confirmar["command"] = partial(registrar, action, titulo, genero, opt, hora_h, hora_min, sala)
    confirmar.grid(row=10, column=1, pady=5, sticky=W)

    #Botão voltar
    voltar = Button(action, bg="gray75", text="Cancelar", font=("Arial", 12))
    voltar["command"] = partial(voltar_click, action, 1)
    voltar.grid(row=11, column=1, sticky=W, ipadx=3)

    action.title("Gerenciamento de Cinema")
    action.geometry("490x430+500+150")
    action.iconbitmap(r'icon.ico')
    action.mainloop()

def consultar_click(frame):
    frame.destroy()
    action = Tk()
    Label(action, text="Consultar Filme", font=("Arial", 24)).grid(row=0, column=1, padx=90, pady=20)

    #Campo de Titulo
    titulo_label = Label(action, text="Título:", font=("Arial", 12))
    titulo_label.grid(row=1, column=0, pady=5, sticky=E)
    titulo = Entry(action, font=("Arial", 12))
    titulo.grid(row=1, column=1, sticky=W+E)

    #Genero
    genero_label = Label(action, text="Gênero:", font=("Arial", 12))
    genero_label.grid(row=2, column=0, pady=5, sticky=E)
    genero = Label(action, text="", font=("Arial", 12))
    genero.grid(row=2, column=1, sticky=W)

    #Classificacao
    clas_label = Label(action, text="Idade:", font=("Arial", 12))
    clas_label.grid(row=3, column=0, pady=5, sticky=E)
    clas = Label(action, text="", font=("Arial", 12))
    clas.grid(row=3, column=1, sticky=W)

    #Horario
    hora_label = Label(action, text="Horário:", font=("Arial", 12))
    hora_label.grid(row=4, column=0, pady=5, sticky=E)
    hora = Label(action, text="", font=("Arial", 12))
    hora.grid(row=4, column=1, sticky=W)

    #Sala
    sala_label = Label(action, text="Sala:", font=("Arial", 12))
    sala_label.grid(row=5, column=0, pady=5, sticky=E)
    sala = Label(action, text="", font=("Arial", 12))
    sala.grid(row=5, column=1, pady=5, sticky=W)

    #Botão Consultar
    consultar_bt = Button(action, bg="gray75", text="Consultar", font=("Arial", 12))
    consultar_bt["command"] = partial(consultar, titulo, genero, clas, hora, sala)
    consultar_bt.grid(row=6, column=1, pady=10, sticky=W)

    # Botão Voltar
    voltar = Button(action, bg="gray75", text="Voltar", font=("Arial", 12))
    voltar["command"] = partial(voltar_click, action, 1)
    voltar.grid(row=7, column=1, sticky=W, ipadx=12)

    action.title("Gerenciamento de Cinema")
    action.geometry("490x340+500+150")
    action.iconbitmap(r'icon.ico')
    action.mainloop()

def excluir_click(frame):
    frame.destroy()
    action = Tk()

    Label(action, text="Excluir Filme", font=("Arial", 24)).grid(row=0, column=1, padx=80, pady=20)

    # Campo de Titulo
    titulo_label = Label(action, text="Título:", font=("Arial", 12))
    titulo_label.grid(row=1, column=0, pady=5, sticky=E)
    titulo = Entry(action, font=("Arial", 12))
    titulo.grid(row=1, column=1, sticky=W+E)

    # Genero
    genero_label = Label(action, text="Gênero:", font=("Arial", 12))
    genero_label.grid(row=2, column=0, pady=5, sticky=E)
    genero = Label(action, text="", font=("Arial", 12))
    genero.grid(row=2, column=1, sticky=W)

    # Classificacao
    clas_label = Label(action, text="Idade:", font=("Arial", 12))
    clas_label.grid(row=3, column=0, pady=5, sticky=E)
    clas = Label(action, text="", font=("Arial", 12))
    clas.grid(row=3, column=1, sticky=W)

    # Horario
    hora_label = Label(action, text="Horário:", font=("Arial", 12))
    hora_label.grid(row=4, column=0, pady=5, sticky=E)
    hora = Label(action, text="", font=("Arial", 12))
    hora.grid(row=4, column=1, sticky=W)

    # Sala
    sala_label = Label(action, text="Sala:", font=("Arial", 12))
    sala_label.grid(row=5, column=0, pady=5, sticky=E)
    sala = Label(action, text="", font=("Arial", 12))
    sala.grid(row=5, column=1, pady=5, sticky=W)

    # Botão Excluir
    excluir = Button(action, bg="gray75", text="Excluir", font=("Arial", 12), state=DISABLED)
    excluir["command"] = partial(deletar, titulo, genero, clas, hora, sala, excluir)
    excluir.grid(row=6, column=1, pady=10, sticky=W, ipadx=6)

    # Botão Encontrar
    encontrar_bt = Button(action, bg="gray75", text="Encontrar", font=("Arial", 12))
    encontrar_bt["command"] = partial(encontrar, titulo, genero, clas, hora, sala, excluir)
    encontrar_bt.grid(row=1, column=2, padx=5)

    # Botão Voltar
    voltar = Button(action, bg="gray75", text="Voltar", font=("Arial", 12))
    voltar["command"] = partial(voltar_click, action, 1)
    voltar.grid(row=7, column=1, sticky=W, ipadx=8)

    action.title("Gerenciamento de Cinema")
    action.geometry("520x340+500+150")
    action.iconbitmap(r'icon.ico')
    action.mainloop()

def show_frame():
    frame = Tk()

    Label(frame, text="Filmes", font=("Arial", 24)).grid(row=0, column=0, padx=200, pady=25)

    #Botão Cadastrar
    cadastrar = Button(frame, text="Cadastrar", font=("Arial", 14))
    cadastrar["command"] = partial(cadastrar_click, frame)
    cadastrar.grid(row=1, column=0, pady=20, sticky=W+E)

    #Botão Consultar
    consultar = Button(frame, text="Consultar", font=("Arial", 14))
    consultar["command"] = partial(consultar_click, frame)
    consultar.grid(row=2, column=0, pady=20, sticky=W+E)

    #Botão Excluir
    excluir = Button(frame, text="Excluir", font=("Arial", 14))
    excluir["command"] = partial(excluir_click, frame)
    excluir.grid(row=3, column=0, pady=25, sticky=W+E)

    #Botão Voltar
    voltar = Button(frame, bg="gray75", text="Voltar", font=("Arial", 14))
    voltar["command"] = partial(voltar_click, frame, 0)
    voltar.grid(row=4, column=0, pady=15)

    #Botão Sair
    sair = Button(frame, bg="gray75", text="Sair", font=("Arial", 14), command=frame.destroy)
    sair.grid(row=5, column=0, ipadx=8)

    frame.title("Gerenciamento de Cinema")
    frame.geometry("490x450+500+150")
    frame.iconbitmap(r'icon.ico')
    frame.mainloop()
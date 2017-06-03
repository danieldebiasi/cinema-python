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

def registrar(frame, numero):
    conn = sqlite3.connect('dados/database.db')
    c = conn.cursor()
    c.execute('INSERT INTO salas (sala, status) VALUES(?, ?)', (numero.get(), "Livre"))
    c.execute('INSERT INTO poltronas (sala) VALUES(?)', (numero.get(),))

    for index in range(1, 51):
        poltrona = "poltrona" + str(index)
        c.execute('UPDATE poltronas SET {} = ? WHERE sala = ?'.format(poltrona), (0, numero.get()))

    conn.commit()
    messagebox.showinfo("Cadastro de Salas", "Sala cadastrada com sucesso!")
    voltar_click(frame, 1)

def consultar(numero, status):
    status["text"] = ""

    conn = sqlite3.connect('dados/database.db')
    c = conn.cursor()
    c.execute('SELECT * FROM salas WHERE sala=?', (numero.get(),))
    result = c.fetchone()

    if result is not None:
        status["text"] = result[1]
        return 1
    else:
        messagebox.showinfo("Consulta de Salas", "Nenhuma sala encontrada!")
        return 0

def deletar(numero, status, excluir):
    conn = sqlite3.connect('dados/database.db')
    c = conn.cursor()
    c.execute('DELETE FROM salas WHERE sala=?', (numero.get(),))
    conn.commit()

    messagebox.showinfo("Exclusão de Salas", "Sala excluída com sucesso!")
    status["text"] = ""
    excluir["state"] = DISABLED

def encontrar(numero, status, excluir):
    if consultar(numero, status) == 1:
        excluir["state"] = NORMAL
    else:
        excluir["state"] = DISABLED

def cadastrar_click(frame):
    frame.destroy()
    action = Tk()

    Label(action, text="Cadastrar Sala", font=("Arial", 24)).grid(row=0, column=1, pady=20)

    # Número da sala
    numero_label = Label(action, text="Número:", font=("Arial", 12))
    numero_label.grid(row=1, column=0, pady=5, sticky=E)
    numero = Entry(action, font=("Arial", 12))
    numero.grid(row=1, column=1, sticky=W)

    # Informação Capacidade
    Label(action, text="Capacidade:", font=("Arial", 12)).grid(row=2, column=0, pady=5, sticky=E)
    Label(action, text="50 pessoas (padrão)", font=("Arial", 12)).grid(row=2, column=1, sticky=W)

    # Botão Confirmar
    confirmar = Button(action, bg="gray75", text="Confirmar", font=("Arial", 12))
    confirmar["command"] = partial(registrar, action, numero)
    confirmar.grid(row=3, column=1, pady=10, sticky=W)

    # Botão Voltar
    voltar = Button(action, bg="gray75", text="Cancelar", font=("Arial", 12))
    voltar["command"] = partial(voltar_click, action, 1)
    voltar.grid(row=4, column=1, sticky=W, ipadx=3)

    action.title("Gerenciamento de Cinema")
    action.geometry("400x250+500+150")
    action.mainloop()

def consultar_click(frame):
    frame.destroy()
    action = Tk()

    Label(action, text="Consultar Salas", font=("Arial", 24)).grid(row=0, column=1, pady=20)

    # Número
    numero_label = Label(action, text="Número:", font=("Arial", 12))
    numero_label.grid(row=1, column=0, pady=5, sticky=E)
    numero = Entry(action, font=("Arial", 12))
    numero.grid(row=1, column=1, sticky=W)

    # Status
    status_label = Label(action, text="Status:", font=("Arial", 12))
    status_label.grid(row=2, column=0, pady=5, sticky=E)
    status = Label(action, text="", font=("Arial", 12))
    status.grid(row=2, column=1, sticky=W)

    # Botão Consultar
    consultar_bt = Button(action, bg="gray75", text="Consultar", font=("Arial", 12))
    consultar_bt["command"] = partial(consultar, numero, status)
    consultar_bt.grid(row=5, column=1, pady=10, sticky=W)

    # Botão Voltar
    voltar = Button(action, bg="gray75", text="Voltar", font=("Arial", 12))
    voltar["command"] = partial(voltar_click, action, 1)
    voltar.grid(row=6, column=1, sticky=W, ipadx=12)

    action.title("Gerenciamento de Cinema")
    action.geometry("360x250+500+150")
    action.mainloop()

def excluir_click(frame):
    frame.destroy()
    action = Tk()

    Label(action, text="Excluir Salas", font=("Arial", 24)).grid(row=0, column=1, pady=20)

    # Número
    numero_label = Label(action, text="Número:", font=("Arial", 12))
    numero_label.grid(row=1, column=0, pady=5, sticky=E)
    numero = Entry(action, font=("Arial", 12))
    numero.grid(row=1, column=1, sticky=W)

    # Status
    status_label = Label(action, text="Status:", font=("Arial", 12))
    status_label.grid(row=2, column=0, pady=5, sticky=E)
    status = Label(action, text="", font=("Arial", 12))
    status.grid(row=2, column=1, sticky=W)

    # Botão Excluir
    excluir = Button(action, bg="gray75", text="Excluir", font=("Arial", 12), state=DISABLED)
    excluir["command"] = partial(deletar, numero, status, excluir)
    excluir.grid(row=3, column=1, pady=10, sticky=W, ipadx=6)

    # Botão Encontrar
    encontrar_bt = Button(action, bg="gray75", text="Encontrar", font=("Arial", 12))
    encontrar_bt["command"] = partial(encontrar, numero, status, excluir)
    encontrar_bt.grid(row=1, column=2, padx=5)

    # Botão Voltar
    voltar = Button(action, bg="gray75", text="Voltar", font=("Arial", 12))
    voltar["command"] = partial(voltar_click, action, 1)
    voltar.grid(row=4, column=1, sticky=W, ipadx=8)

    action.title("Gerenciamento de Cinema")
    action.geometry("360x250+500+150")
    action.mainloop()

def show_frame():
    frame = Tk()

    Label(frame, text="Salas", font=("Arial", 24)).grid(row=0, column=0, padx=200, pady=25)

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
    excluir.grid(row=3, column=0, pady=20, sticky=W+E)

    #Botão Voltar
    voltar = Button(frame, bg="gray75", text="Voltar", font=("Arial", 14))
    voltar["command"] = partial(voltar_click, frame, 0)
    voltar.grid(row=4, column=0, pady=15)

    #Botão Sair
    sair = Button(frame, bg="gray75", text="Sair", font=("Arial", 14), command=frame.destroy)
    sair.grid(row=5, column=0, ipadx=8)

    frame.title("Gerenciamento de Cinema")
    frame.geometry("490x450+500+150")
    frame.mainloop()
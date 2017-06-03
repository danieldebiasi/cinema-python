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

def registrar(frame, nome, rg, entrada, saida, user, pwd):
    conn = sqlite3.connect('dados/database.db')
    c = conn.cursor()
    c.execute('INSERT INTO funcionarios (nome, rg, entrada, saida) VALUES(?, ?, ?, ?)',
              (nome.get(), rg.get(), entrada.get(), saida.get()))
    conn.commit()

    c.execute('INSERT INTO usuarios (user, password, acesso, rg) VALUES(?, ?, ?, ?)',
              (user.get(), pwd.get(), 0, rg.get()))
    conn.commit()

    messagebox.showinfo("Cadastro de Funcionários", "Funcionário cadastrado com sucesso!")
    voltar_click(frame, 1)

def consultar(rg, nome, entrada, saida):
    nome["text"] = ""
    entrada["text"] =""
    saida["text"] = ""

    conn = sqlite3.connect('dados/database.db')
    c = conn.cursor()
    c.execute('SELECT * FROM funcionarios WHERE rg=?', (rg.get(),))
    result = c.fetchone()
    if result is not None:
        nome["text"] = result[0]
        entrada["text"] = result[2]
        saida["text"] = result[3]
        return 1
    else:
        messagebox.showinfo("Consulta de Funcionários", "Nenhum funcionário encontrado!")
        return 0

def deletar(rg, nome, entrada, saida, excluir):
    conn = sqlite3.connect('dados/database.db')
    c = conn.cursor()
    c.execute('DELETE FROM funcionarios WHERE rg=?', (rg.get(),))
    conn.commit()

    c.execute('DELETE FROM usuarios WHERE rg=?', (rg.get(),))
    conn.commit()

    messagebox.showinfo("Exclusão de funcionários", "Funcionário excluído com sucesso!")
    rg["text"] = ""
    nome["text"] = ""
    entrada["text"] = ""
    saida["text"] = ""
    excluir["state"] = DISABLED

def encontrar(rg, nome, entrada, saida, excluir):
    if consultar(rg, nome, entrada, saida) == 1:
        excluir["state"] = NORMAL
    else:
        excluir["state"] = DISABLED

def cadastrar_click(frame):
    frame.destroy()
    action = Tk()
    Label(action, text="Cadastrar Funcionário", font=("Arial", 24)).grid(row=0, column=1, padx=30, pady=20)

    # Nome
    nome_label = Label(action, text="Nome:", font=("Arial", 12))
    nome_label.grid(row=1, column=0, pady=5, sticky=E)
    nome = Entry(action, font=("Arial", 12))
    nome.grid(row=1, column=1, sticky=W + E)

    # RG
    rg_label = Label(action, text="RG:", font=("Arial", 12))
    rg_label.grid(row=2, column=0, pady=(5, 10), sticky=E)
    rg = Entry(action, font=("Arial", 12))
    rg.grid(row=2, column=1, sticky=W + E)

    # Horário de Entrada
    entrada_label = Label(action, text="Entrada:", font=("Arial", 12))
    entrada_label.grid(row=8, column=0, pady=5, sticky=E)
    entrada = Entry(action, font=("Arial", 12))
    entrada.grid(row=8, column=1, sticky=W)

    # Horário de Saída
    saida_label = Label(action, text="Saída:", font=("Arial", 12))
    saida_label.grid(row=9, column=0, pady=5, sticky=E)
    saida = Entry(action, font=("Arial", 12))
    saida.grid(row=9, column=1, sticky=W)

    # Usuario
    user_label = Label(action, text="Usuário:", font=("Arial", 12))
    user_label.grid(row=10, column=0, pady=5, sticky=E)
    user = Entry(action, font=("Arial", 12))
    user.grid(row=10, column=1, sticky=W)

    # Senha
    pwd_label = Label(action, text="Senha:", font=("Arial", 12))
    pwd_label.grid(row=11, column=0, pady=(10, 5), sticky=E)
    pwd = Entry(action, font=("Arial", 12))
    pwd.grid(row=11, column=1, sticky=W)

    # Botão confirmar
    confirmar = Button(action, bg="gray75", text="Confirmar", font=("Arial", 12))
    confirmar["command"] = partial(registrar, action, nome, rg, entrada, saida, user, pwd)
    confirmar.grid(row=12, column=1, pady=5, sticky=W)

    # Botão Voltar
    voltar = Button(action, bg="gray75", text="Cancelar", font=("Arial", 12))
    voltar["command"] = partial(voltar_click, action, 1)
    voltar.grid(row=13, column=1, sticky=W, ipadx=3)

    action.title("Gerenciamento de Cinema")
    action.geometry("490x370+500+150")
    action.mainloop()

def consultar_click(frame):
    frame.destroy()
    action = Tk()

    Label(action, text="Consultar Funcionário", font=("Arial", 24)).grid(row=0, column=1, padx=30, pady=20)

    # RG
    rg_label = Label(action, text="RG:", font=("Arial", 12))
    rg_label.grid(row=1, column=0, pady=5, sticky=E)
    rg = Entry(action, font=("Arial", 12))
    rg.grid(row=1, column=1, sticky=W+E)

    # Nome
    nome_label = Label(action, text="Nome:", font=("Arial", 12))
    nome_label.grid(row=2, column=0, pady=5, sticky=E)
    nome = Label(action, text="", font=("Arial", 12))
    nome.grid(row=2, column=1, sticky=W)

    # Horário de Entrada
    entrada_label = Label(action, text="Entrada:", font=("Arial", 12))
    entrada_label.grid(row=3, column=0, pady=5, sticky=E)
    entrada = Label(action, text="", font=("Arial", 12))
    entrada.grid(row=3, column=1, sticky=W)

    # Horário de Saída
    saida_label = Label(action, text="Saída:", font=("Arial", 12))
    saida_label.grid(row=4, column=0, pady=5, sticky=E)
    saida = Label(action, text="", font=("Arial", 12))
    saida.grid(row=4, column=1, sticky=W)

    # Botão Consultar
    consultar_bt = Button(action, bg="gray75", text="Consultar", font=("Arial", 12))
    consultar_bt["command"] = partial(consultar, rg, nome, entrada, saida)
    consultar_bt.grid(row=5, column=1, pady=10, sticky=W)

    #Botão Voltar
    voltar = Button(action, bg="gray75", text="Voltar", font=("Arial", 12))
    voltar["command"] = partial(voltar_click, action, 1)
    voltar.grid(row=6, column=1, sticky=W, ipadx=12)

    action.title("Gerenciamento de Cinema")
    action.geometry("490x300+500+150")
    action.mainloop()

def excluir_click(frame):
    frame.destroy()
    action = Tk()

    Label(action, text="Excluir Funcionário", font=("Arial", 24)).grid(row=0, column=1, padx=35, pady=20)

    # RG
    rg_label = Label(action, text="RG:", font=("Arial", 12))
    rg_label.grid(row=1, column=0, sticky=E)
    rg = Entry(action, font=("Arial",12))
    rg.grid(row=1, column=1, sticky=W+E)

    # Nome
    nome_label = Label(action, text="Nome:", font=("Arial", 12))
    nome_label.grid(row=2, column=0, sticky=E)
    nome = Label(action, text="", font=("Arial", 12))
    nome.grid(row=2, column=1, sticky=W)

    # Entrada
    entrada_label = Label(action, text="Entrada:", font=("Arial", 12))
    entrada_label.grid(row=3, column=0, sticky=E)
    entrada = Label(action, text="", font=("Arial", 12))
    entrada.grid(row=3, column=1, sticky=W)

    # Saida
    saida_label = Label(action, text="Saida:", font=("Arial", 12))
    saida_label.grid(row=4, column=0, sticky=E)
    saida = Label(action, text="", font=("Arial", 12))
    saida.grid(row=4, column=1, sticky=W)

    # Botão Excluir
    excluir = Button(action, bg="gray75", text="Excluir", font=("Arial", 12), state=DISABLED)
    excluir["command"] = partial(deletar, rg, nome, entrada, saida, excluir)
    excluir.grid(row=6, column=1, pady=10, sticky=W, ipadx=6)

    # Botão Encontrar
    encontrar_bt = Button(action, bg="gray75", text="Encontrar", font=("Arial", 12))
    encontrar_bt["command"] = partial(encontrar, rg, nome, entrada, saida, excluir)
    encontrar_bt.grid(row=1, column=2, padx=5)

    # Botão Voltar
    voltar = Button(action, bg="gray75", text="Voltar", font=("Arial", 12))
    voltar["command"] = partial(voltar_click, action, 1)
    voltar.grid(row=7, column=1, sticky=W, ipadx=8)

    action.title("Gerenciamento de Cinema")
    action.geometry("520x280+500+150")
    action.mainloop()

def show_frame():
    frame = Tk()

    Label(frame, text="Funcionários", font=("Arial", 24)).grid(row=0, column=0, padx=150, pady=25)

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
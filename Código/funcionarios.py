from tkinter import *
from functools import partial
import gestor

def voltar_click(frame):
    frame.destroy()
    gestor.show_frame()

def cadastrar_click(frame):
    frame.destroy()
    action = Tk()
    Label(action, text="Cadastrar Funcionário", font=("Arial", 24)).grid(row=0, column=1, padx=80, pady=20)

    # Nome
    nome_label = Label(action, text="Nome:", font=("Arial", 12))
    nome_label.grid(row=1, column=0, pady=5)
    nome = Entry(action, font=("Arial", 12))
    nome.grid(row=1, column=1, sticky=W + E)

    # RG
    rg_label = Label(action, text="RG:", font=("Arial", 12))
    rg_label.grid(row=2, column=0, pady=(5, 10))
    rg = Entry(action, font=("Arial", 12))
    rg.grid(row=2, column=1, sticky=W + E)

    # Horário de Entrada
    entrada_label = Label(action, text="Entrada:", font=("Arial", 12))
    entrada_label.grid(row=8, column=0, pady=5)
    entrada = Entry(action, font=("Arial", 12))
    entrada.grid(row=8, column=1, sticky=W)

    # Horário de Saída
    saida_label = Label(action, text="Saída:", font=("Arial", 12))
    saida_label.grid(row=9, column=0, pady=(10, 5))
    saida = Entry(action, font=("Arial", 12))
    saida.grid(row=9, column=1, sticky=W)

    # Botão confirmar
    confirmar = Button(action, bg="gray75", text="Confirmar", font=("Arial", 12))
    confirmar["command"] = partial(registrar, action, titulo, genero, opt, hora)
    confirmar.grid(row=10, column=1, pady=5, sticky=W)

    # Botão voltar
    voltar = Button(action, bg="gray75", text="Cancelar", font=("Arial", 12))
    voltar["command"] = partial(voltar_click, action)
    voltar.grid(row=11, column=1, sticky=W, ipadx=3)

    action.title("Cinema 1.0")
    action.geometry("490x430+500+150")
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
    consultar.grid(row=2, column=0, pady=20, sticky=W+E)

    #Botão Excluir
    excluir = Button(frame, text="Excluir", font=("Arial", 14))
    excluir.grid(row=3, column=0, pady=20, sticky=W+E)

    #Botão Voltar
    voltar = Button(frame, bg="gray75", text="Voltar", font=("Arial", 14))
    voltar["command"] = partial(voltar_click, frame)
    voltar.grid(row=4, column=0, pady=15)

    #Botão Sair
    sair = Button(frame, bg="gray75", text="Sair", font=("Arial", 14), command=frame.destroy)
    sair.grid(row=5, column=0, ipadx=8)

    frame.title("Cinema 1.0")
    frame.geometry("490x450+500+150")
    frame.mainloop()
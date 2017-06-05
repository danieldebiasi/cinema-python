from tkinter import *
from functools import partial
import filmes
import funcionarios
import salas

def filmes_click(frame):
    frame.destroy()
    filmes.show_frame()

def funcionarios_click(frame):
    frame.destroy()
    funcionarios.show_frame()

def salas_click(frame):
    frame.destroy()
    salas.show_frame()

def show_frame():
    frame = Tk()

    Label(frame, text="Gerenciamento Cinema", font=("Arial", 24)).grid(row=0, column=0, padx=75, pady=25)

    #Botão Filmes
    filmes = Button(frame, text="Filmes", font=("Arial", 14))
    filmes["command"] = partial(filmes_click, frame)
    filmes.grid(row=1, column=0, pady=20, sticky=W+E)

    #Botão Funcionários
    funcionarios = Button(frame, text="Funcionários", font=("Arial", 14))
    funcionarios["command"] = partial(funcionarios_click, frame)
    funcionarios.grid(row=2, column=0, pady=20, sticky=W+E)

    #Botão Salas
    salas = Button(frame, text="Salas", font=("Arial", 14))
    salas["command"] = partial(salas_click, frame)
    salas.grid(row=3, column=0, pady=20, sticky=W+E)

    #Botão Sair
    sair = Button(frame, bg="gray75", text="Sair", font=("Arial", 14), command=frame.destroy)
    sair.grid(row=4, column=0, pady=15, ipadx=8)

    #Loop
    frame.title("Gerenciamento de Cinema")
    frame.geometry("490x400+500+150")
    frame.iconbitmap(r'icon.ico')

    frame.mainloop()
from tkinter import *

def show_frame():
    frame_gestor = Tk()

    #Botão Filmes
    filmes = Button(frame_gestor, text="Gerenciamento de Filmes", font=("Arial", 14))
    filmes.grid(row=0, column=0, padx=100, pady=50)

    #Botão Funcionários
    funcionarios = Button(frame_gestor, text="Gerenciamento de Funcionários", font=("Arial", 14))
    funcionarios.grid(row=1, column=0, padx=100, pady=50)

    #Botão Salas
    salas = Button(frame_gestor, text="Gerenciamento de Salas", font=("Arial", 14))
    salas.grid(row=2, column=0, padx=100, pady=50)

    #Loop
    frame_gestor.title("Cinema 1.0")
    frame_gestor.geometry("500x500+500+300")

    frame_gestor.mainloop()
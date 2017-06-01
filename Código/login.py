from functools import partial
from tkinter import *
import login_events as events

def show_frame(frame):
    #Label Título
    Label(frame, text="Login", font=("Arial", 24)).grid(row=0, column=1, pady=10)

    #Comando tecla Enter
    frame.bind("<Return>", (lambda event: events.login(frame, username, password)))

    #Label Usuário
    user_label = Label(frame, text="Usuário:", font=("Arial", 12))
    user_label.grid(row=1, column=0, pady=2)

    #Campo Usuário
    username = Entry(frame, font=("Arial", 12))
    username.grid(row=1, column=1, pady=2, sticky=W+E)

    #Label Senha
    password_label = Label(frame, text="Senha:", font=("Arial", 12))
    password_label.grid(row=2, column=0, sticky=E, pady=2)

    #Campo Senha
    password = Entry(frame, show="*", font=("Arial", 12))
    password.grid(row=2, column=1, pady=2, sticky=W+E)

    #Botão Entrar
    login_button = Button(frame, text="Entrar", font=("Arial", 12, "bold"))
    login_button["command"] = partial(events.login, frame, username, password)
    login_button.grid(row=3, column=1, sticky=W+E)

    #Botão Sair
    sair = Button(frame, text="Sair", font=("Arial", 12), command=frame.destroy)
    sair.grid(row=4, column=1, sticky=W+E)

#Mainloop
frame = Tk()
frame.title("Gerenciamento de Cinema")
frame.geometry("300x250+500+150")
show_frame(frame)

Label(frame, text="Para fins de teste (user:password)\ngestor:gestor\natendente:atendente").grid(row=5, column=1)

frame.mainloop()
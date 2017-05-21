from functools import partial
from tkinter import *
import login_events as events

def show_frame(frame_login):
    #Label Título
    Label(frame_login, text="Login", font=("Arial", 24)).grid(row=0, column=0, columnspan=2, pady=5)

    #Comando tecla Enter
    frame_login.bind("<Return>", (lambda event: events.login(frame_login, username, password)))

    #Label Usuário
    user_label = Label(frame_login, text="Usuário:", font=("Arial", 11))
    user_label.grid(row=1, column=0, pady=2)

    #Campo Usuário
    username = Entry(frame_login, font=("Arial", 12))
    username.grid(row=1, column=1, pady=2)

    #Label Senha
    password_label = Label(frame_login, text="Senha:", font=("Arial", 12))
    password_label.grid(row=2, column=0, sticky=E, pady=2)

    #Campo Senha
    password = Entry(frame_login, show="*", font=("Arial", 12))
    password.grid(row=2, column=1, pady=2)

    #Botão Entrar
    login_button = Button(frame_login, text="Entrar", font=("Arial", 12), height=2, width=10)
    login_button["command"] = partial(events.login, frame_login, username, password)
    login_button.grid(row=3, column=1, pady=10, sticky=W)

#Mainloop
frame_login = Tk()
frame_login.title("Cinema 1.0")
frame_login.geometry("300x250+600+300")
show_frame(frame_login)

Label(frame_login, text="Para fins de teste (user:password)\ngestor:gestor\natendente:atendente").grid(row=4, column=1)

frame_login.mainloop()
from tkinter import messagebox
import gestor
import atendente

"""
Comportamento dos botões da tela de login

arg[0] = sinal de exclusão lógica
    > arg[0] == 1 - Presente
    > arg[0] == 0 - Excluído

arg[1] = nível de acesso
    > arg[1] == 1 - Acesso Gestor
    > arg[1] == 0 - Acesso Atendente

arg[2] = nome de usuário

arg[3] = senha

"""

def login(frame_login, username, pwd):
    data = open("dados/usuarios.txt", "r")

    for line in data:
        arg = line.split()
        if(arg[0] == "1" and username.get() == arg[2] and pwd.get() == arg[3]):
            if(arg[1] == "1"):
                messagebox.showinfo("Login", "Bem-vindo(a)!\n" + "Acesso: Gestor")
                frame_login.destroy()
                gestor.show_frame()
            else:
                messagebox.showinfo("Login", "Bem-vindo(a)!\n" + "Acesso: Atendente")
                frame_login.destroy()
                atendente.show_frame()
            data.close()
            return

    data.close()
    messagebox.showinfo("Login", "Usuário ou senha inválido!")
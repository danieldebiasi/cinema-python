from tkinter import messagebox
import gestor
import atendente
import sqlite3

def login(frame, username, pwd):
    conn = sqlite3.connect('dados/database.db')
    c = conn.cursor()

    c.execute('SELECT * FROM usuarios WHERE user=? AND password=?', (username.get(), pwd.get()))
    if c.fetchone() is not None:
        c.execute('SELECT * FROM usuarios WHERE user=? AND password=? AND acesso=1', (username.get(), pwd.get()))
        if c.fetchone() is not None:
            messagebox.showinfo("Login", "Bem-vindo(a)!\n" + "Acesso: Gestor")
            c.close()
            conn.close()
            frame.destroy()
            gestor.show_frame()
        else:
            messagebox.showinfo("Login", "Bem-vindo(a)!\n" + "Acesso: Atendente")
            c.close()
            conn.close()
            frame.destroy()
            atendente.show_frame()
    else:
        messagebox.showinfo("Login", "Usuário ou senha inválido!")
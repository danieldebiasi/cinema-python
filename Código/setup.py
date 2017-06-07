import os
import sys

os.environ['TCL_LIBRARY'] = "C:\\Users\\danie\\AppData\\Local\\Programs\\Python\\Python36-32\\tcl\\tcl8.6"
os.environ['TK_LIBRARY'] = "C:\\Users\\danie\\AppData\\Local\\Programs\\Python\\Python36-32\\tcl\\tk8.6"

from cx_Freeze import setup, Executable

setup(
name = "Cinema",
version = "0.3",
description = "Sistema de Gerenciamento de Cinema",
options = {"build_exe": {
    'packages': ["functools","sqlite3","tkinter", "atendente", "filmes", "funcionarios", "gestor", "login_events", "salas"],
    'include_files':[r"C:\Users\danie\AppData\Local\Programs\Python\Python36-32\DLLs\tcl86t.dll",
                     r"C:\Users\danie\AppData\Local\Programs\Python\Python36-32\DLLs\tk86t.dll",
                     r"C:\Users\danie\AppData\Local\Programs\Python\Python36-32\DLLs\sqlite3.dll",
                     r"dados", r"ingresso", r"icones"],
    'include_msvcr': True,
}},
executables = [Executable("login.py", base="win32GUI", icon='icones/icon.ico')]
)
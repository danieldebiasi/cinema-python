from tkinter import *

def show_frame():
    frame_atendente = Tk()

    Label(frame_atendente, text="Venda de Ingressos", font=("Arial", 24)).grid(row=0, column=0, padx=100, pady=20)

    """

    Venda de Ingressos


    """

    frame_atendente.title("Cinema 1.0")
    frame_atendente.geometry("500x500+500+300")

    frame_atendente.mainloop()
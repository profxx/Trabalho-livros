from tkinter import *
import app_login

class App():
    # Cores
    cor_1 = "#212529"
    cor_2 = "#6c757d"
    cor_3 = "#adb5bd"
    cor_4 = "#dee2e6"

    def __init__(self):
        self.root = root
        self.telaconfig()
        self.widgets()

        root.mainloop()

    def telaconfig(self):
        self.root.title("App de comida")
        self.root.geometry("390x656+955+10")
        self.root.configure(background = self.cor_3)
        self.root.resizable(False, False)
    
    def widgets(self):
        Label(
            self.root,
            text = "Nome do App",
            background = self.cor_3,
            foreground = self.cor_1,
            font = ("Verdana", 20)
        ).place(
            relheight = 0.10,
            relwidth = 0.50,
            relx = 0.25,
            rely = 0.30
        )

        self.botao_telaLogin = Button(
            self.root,
            text = "Ir para tela de login",
            background = self.cor_1,
            activebackground = self.cor_1,
            foreground = self.cor_4,
            activeforeground = self.cor_4,
            font = ("Verdana", 12),
            relief = FLAT
        )
        self.botao_telaLogin.place(
            relheight = 0.06,
            relwidth = 0.50,
            relx = 0.25,
            rely = 0.84
        )

# Programa Principal
root = Tk()
App()
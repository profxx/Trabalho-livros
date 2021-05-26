from tkinter import *

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
        # Texto
        Label(
            self.root,
            text = "App de comida",
            background = self.cor_3,
            foreground = self.cor_1,
            font = ("Verdana", 20)
        ).place(
            relheight = 0.10,
            relwidth = 0.52,
            relx = 0.24,
            rely = 0.20
        )

        Label(
            self.root,
            text = "Faça o login ou registre-se",
            background = self.cor_3,
            foreground = self.cor_1,
            font = ("Verdana", 14)
        ).place(
            relheight = 0.10,
            relwidth = 0.80,
            relx = 0.10,
            rely = 0.75
        )

        # Botões
        self.botao_login = Button(
            self.root,
            text = "Login",
            background = self.cor_1,
            activebackground = self.cor_1,
            foreground = self.cor_4,
            activeforeground = self.cor_4,
            font = ("Verdana", 12),
            relief = FLAT
        )
        self.botao_login.place(
            relheight = 0.06,
            relwidth = 0.38,
            relx = 0.10,
            rely = 0.84
        )

        self.botao_registrar = Button(
            self.root,
            text = "Registrar",
            background = self.cor_1,
            activebackground = self.cor_1,
            foreground = self.cor_4,
            activeforeground = self.cor_4,
            font = ("Verdana", 12),
            relief = FLAT
        )
        self.botao_registrar.place(
            relheight = 0.06,
            relwidth = 0.38,
            relx = 0.52,
            rely = 0.84
        )

        self.imagem = PhotoImage(file = "imagem.png")
        self.image = Label(self.root, image = self.imagem, background = self.cor_1)
        self.image.place(
            relheight =0.31,
            relwidth =0.52,
            relx =0.24,
            rely = 0.34
        )


# Programa Principal
root = Tk()
App()

from tkinter import *

class App():
    # Cores
    cor_1 = "#264653"
    cor_2 = "#2a9d8f"
    cor_3 = "#e9c46a"
    cor_4 = "#f4a261"
    cor_5 = "#e76f51"

    # Método construtor
    def __init__(self):
        self.root = root
        self.telaconfig()
        self.widgets()

        root.mainloop()

    # Configurações padrões da janela
    def telaconfig(self):
        self.root.title("EMMT")
        self.root.geometry("390x656+955+10")
        self.root.resizable(False, False)
        self.root.configure(background = self.cor_2)

    def widgets(self):
        # Texto
        Label(
            self.root,
            text = "EMMT",
            background = self.cor_2,
            foreground = self.cor_4,
            font = ("Verdana", 30)
        ).place(
            relheight = 0.10,
            relwidth = 0.40,
            relx = 0.30,
            rely = 0.20
        )

        Label(
            self.root,
            text = "EMMT\n Faça o registrou ou entre\n em sua conta\npara salvar seus livros!",
            background = self.cor_2,
            foreground = self.cor_4,
            font = ("Verdana", 14)
        ).place(
            relheight = 0.16,
            relwidth = 0.80,
            relx = 0.10,
            rely = 0.60
        )        

        # Imagem
        self.imagem = PhotoImage(file = "imagem_livro.png")
        self.image = Label(self.root, image = self.imagem, background = self.cor_1)
        self.image.place(
            relheight =0.28,
            relwidth =0.76,
            relx =0.12,
            rely = 0.30
        )

        # Botão
        self.botao_entrar = Button(
            self.root,
            text = "Entrar",
            background = self.cor_3,
            activebackground = self.cor_3,
            foreground = self.cor_2,
            activeforeground = self.cor_2,
            font = ("Verdana", 14),
            relief = FLAT
        )
        self.botao_entrar.place(
            relheight = 0.06,
            relwidth = 0.34,
            relx = 0.15,
            rely = 0.82
        )

        self.botao_registrar = Button(
            self.root,
            text = "Registrar",
            background = self.cor_3,
            activebackground = self.cor_3,
            foreground = self.cor_2,
            activeforeground = self.cor_2,
            font = ("Verdana", 14),
            relief = FLAT
        )
        self.botao_registrar.place(
            relheight = 0.06,
            relwidth = 0.30,
            relx = 0.55,
            rely = 0.82
        )




root = Tk()
App()
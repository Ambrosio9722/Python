import tkinter as tk
from tkinter import messagebox
#============== EXIBIR MENSAGENS NA TELA USANDO TELINAHS =============================

root = tk.Tk()
root.withdraw() # Esconde a janela principal
messagebox.showinfo("Título", "Esta é uma mensagem de informação!")
resposta = messagebox.askyesno("Confirmação", "Você tem certeza?")
if resposta:
        print("Usuário escolheu Sim")
else:
            print("Usuário escolheu Não")
messagebox.showerror("Erro", "Ocorreu um erro!")

#======== whindos ===========
from win10toast import ToastNotifier

# notificação do windows (telinha do lado)
toaster = ToastNotifier()
toaster.show_toast(
        "Título da Notificação",
        "Esta é uma notificação de desktop!",
        duration=10 # Duração em segundos
    )
import tkinter as tk
import sqlite3
from tkinter import messagebox

class CRUDApp:
    # __init__ é um método especial de construtor
    # parâmetro root é a janela principal do tk
    def __init__(self, root):
        self.root = root  # esse é o parametro
        self.root.title("CRUD APP")

        # conexao com o banco de dados
        self.conexao = sqlite3.connect("crud.db")
        self.cursor = self.conexao.cursor()

        # cria a tabela se não existir:
        self.cursor.execute("""
            CREATE TABLE IF NOT EXISTS usuarios (
                id INTEGER PRIMARY KEY,
                nome TEXT,
                email
                )
            """)
        # confirmar e salvar alterações no banco de dados:
        self.conexao.commit()

        # interface grafica:
        self.label_id = tk.Label(root, text="ID:")
        self.label_id.pack() # o pack organiza automaticamente os widgets em um layout de bloco
        self.entry_id = tk.Entry(root)
        self.entry_id.pack()

        self.label_nome = tk.Label(root, text="nome:")
        self.label_nome.pack()
        self.entry_nome = tk.Entry(root)
        self.entry_nome.pack()

        self.label_email = tk.Label(root, text="Email:")
        self.label_email.pack()
        self.entry_email = tk.Entry(root)
        self.entry_email.pack()

        self.botao_criar = tk.Button(root, text="Criar", command=self.criar_usuario)
        self.botao_criar.pack()

        self.botao_ler = tk.Button(root, text="Ler", command=self.ler_usuarios)
        self.botao_ler.pack()

        self.botao_atualizar = tk.Button(root, text="Atualizar", command=self.atualizar_usuario)
        self.botao_atualizar.pack()

        self.botao_deletar = tk.Button(root, text="Deletar", command=self.deletar_usuario)
        self.botao_deletar.pack()

    def criar_usuario(self):
        nome = self.entry_nome.get()
        email = self.entry_email.get()

        self.cursor.execute("INSERT INTO usuarios (nome, email) VALUES (?, ?)", (nome, email))
        self.conexao.commit()

        messagebox.showinfo("Sucesso", "O cadastro do usuário foi criado.")

        self.entry_nome.delete(0, tk.END)
        self.entry_email.delete(0, tk.END)

    def ler_usuarios(self):
        self.cursor.execute("SELECT * FROM usuarios")
        # usuarios contém uma lista com os dados do banco
        usuarios = self.cursor.fetchall()

        if usuarios:
            usuarios_lista = "\n".join([f"ID: {usuario[0]}, nome: {usuario[1]}, Email: {usuario[2]}" for usuario in usuarios])
            messagebox.showinfo("usuarios", usuarios_lista)
        else:
            messagebox.showinfo("usuarios", "No usuarios found.")

    def atualizar_usuario(self):
        usuario_id = int(self.entry_id.get())
        novo_usuario = self.entry_nome.get()
        novo_email = self.entry_email.get()

        self.cursor.execute("UPDATE usuarios SET nome=?, email=? WHERE id=?", (novo_usuario, novo_email, usuario_id))
        self.conexao.commit()

        messagebox.showinfo("Sucesso", "O cadastro do usuário foi atualizado.")

    def deletar_usuario(self):
        usuario_id = int(self.entry_id.get())

        self.cursor.execute("DELETE FROM usuarios WHERE id=?", (usuario_id,))
        self.conexao.commit()

        messagebox.showinfo("Sucesso", "O cadastro do usuário foi deletado.")


if __name__ == "__main__":
    root = tk.Tk()
    root.geometry('300x250')
    root.resizable(width=False, height=False)
    app = CRUDApp(root)
    root.mainloop()

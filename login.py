import tkinter as tk
from tkinter import messagebox
import db  

def abrir_crud(user):
    login.destroy()

    crud = tk.Tk()
    crud.title(f"CRUD - {user}")
    crud.geometry("350x420")

    def carregar():
        lista.delete(0, tk.END)
        for i, u in db.listar_usuarios():
            lista.insert(tk.END, f"{i} - {u}")

    def selecionar():
        try:
            item = lista.get(lista.curselection())
            i, u = item.split(" - ")
            e_id.delete(0, tk.END)
            e_user.delete(0, tk.END)
            e_id.insert(0, i)
            e_user.insert(0, u)
        except:
            pass

    def adicionar():
        try:
            db.adicionar_usuario(e_user.get(), e_pass.get())
            carregar()
        except:
            messagebox.showerror("Erro", "Usuário já existe")

    def atualizar():
        db.atualizar_usuario(e_id.get(), e_user.get(), e_pass.get())
        carregar()

    def excluir():
        db.excluir_usuario(e_id.get())
        carregar()

    tk.Label(crud, text="ID").pack()
    e_id = tk.Entry(crud)
    e_id.pack()

    tk.Label(crud, text="Usuário").pack()
    e_user = tk.Entry(crud)
    e_user.pack()

    tk.Label(crud, text="Senha").pack()
    e_pass = tk.Entry(crud, show="*")
    e_pass.pack()

    tk.Button(crud, text="Adicionar", command=adicionar).pack(pady=4)
    tk.Button(crud, text="Atualizar", command=atualizar).pack(pady=4)
    tk.Button(crud, text="Excluir", command=excluir).pack(pady=4)

    lista = tk.Listbox(crud, width=30)
    lista.pack(pady=10)
    lista.bind("<<ListboxSelect>>", lambda e: selecionar())

    carregar()
    crud.mainloop()

def validar_login():
    if db.buscar_usuario(e_login_user.get(), e_login_pass.get()):
        abrir_crud(e_login_user.get())
    else:
        messagebox.showerror("Erro", "Usuário ou senha incorretos")

login = tk.Tk()
login.title("Login")
login.geometry("300x200")

tk.Label(login, text="Usuário").pack()
e_login_user = tk.Entry(login)
e_login_user.pack()

tk.Label(login, text="Senha").pack()
e_login_pass = tk.Entry(login, show="*")
e_login_pass.pack()

tk.Button(login, text="Entrar", command=validar_login).pack(pady=15)

login.mainloop()

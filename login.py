import tkinter as tk

def login():
    username = entry_username.get()
    password = entry_password.get()

    # ver se ta certo
    if username == "admin" and password == "admin":
        label_result.config(text="Login bem-sucedido!")
    else:
        label_result.config(text="Nome de usuário ou senha incorretos")

root = tk.Tk()
root.title("Login")

label_username = tk.Label(root, text="Nome de usuário:")
label_password = tk.Label(root, text="Senha:")
entry_username = tk.Entry(root)
entry_password = tk.Entry(root, show="*")  # esconder lol
button_login = tk.Button(root, text="Login", command=login)
label_result = tk.Label(root, text="")

label_username.grid(row=0, column=0, sticky="e")
label_password.grid(row=1, column=0, sticky="e")
entry_username.grid(row=0, column=1)
entry_password.grid(row=1, column=1)
button_login.grid(row=2, columnspan=2)
label_result.grid(row=3, columnspan=2)

root.mainloop()

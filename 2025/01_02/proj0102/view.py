"""
Claudinei de Oliveira - UTF8 - pt-br
- Tkinter: view.py
JSON - JavaScript Object Notation
"""

from tkinter import *
import tkinter as tk
from tkinter import ttk

# Configurações iniciais do aplicativo
def configurar_app(app):
    app.title("Análise e Desenvolvimento de Sistemas")
    app.geometry("1024x600")
    app.configure(background="#F8F8FF")
    app.resizable(True, True)
    app.maxsize(width=1024, height=600)

# Criação do frame principal
def criar_frame(app):
    frame = LabelFrame(app, text="Cadastro", borderwidth=1, relief="solid")
    frame.place(x=10, y=10, width=1000, height=200)
    return frame

# Criação dos rótulos de texto
def criar_labels(frame):
    lb_1 = Label(frame, text="Contatos:", fg="red", font=("Arial", 14, "italic", "bold"))
    lb_1.place(x=15, y=10, width=70, height=20)
    lb_nome = Label(frame, text="Digite um nome:", font=("Arial", 14))
    lb_nome.place(x=20, y=35, width=120, height=20)
    lb_sobrenome = Label(frame, text="Digite um sobrenome:", font=("Arial", 14))
    lb_sobrenome.place(x=20, y=65, width=180, height=20)

# Criação dos campos de entrada de texto
def criar_entry(frame):
    nome = Entry(frame, font=("Arial", 14))
    nome.place(x=200, y=35, width=400, height=20)
    sobrenome = Entry(frame, font=("Arial", 14))
    sobrenome.place(x=200, y=65, width=400, height=20)
    return nome, sobrenome

# Criação dos botões de seleção de gênero
def criar_checkbutton(frame, genero_var):
    generos = ["Masculino", "Feminino", "Outros"]
    y_pos = 95
    for gen in generos:
        Radiobutton(frame, text=gen, variable=genero_var, value=gen, font=("Arial", 14)).place(x=200, y=y_pos)
        y_pos += 30  

# Criação dos botões de ação
def criar_botao(app, capturar, mostrar_campo_pesquisa, salvar_edicao, excluir_registro, app_quit):
    style = ttk.Style()
    style.configure("TButton", font=("Arial", 14, "bold"))

    ttk.Button(app, text="Inserir dados", command=capturar).place(x=20, y=220, width=155, height=40)
    ttk.Button(app, text="Pesquisar dados", command=mostrar_campo_pesquisa).place(x=185, y=220, width=155, height=40)
    ttk.Button(app, text="Atualizar dados", command=salvar_edicao).place(x=350, y=220, width=155, height=40)
    ttk.Button(app, text="Apagar registro", command=excluir_registro).place(x=515, y=220, width=155, height=40)
    ttk.Button(app, text="Sair", command=app_quit).place(x=685, y=220, width=155, height=40)


# Criação do campo de pesquisa
def criar_campo_pesquisa(app, campo_pesquisa_var, filtrar_dados, fechar_pesquisa):
    lb_pesquisar = Label(app, text="Digite o nome a pesquisar:", font=("Arial", 14), bg="white")
    lb_pesquisar.place(x=10, y=270, width=220, height=20)
    
    campo_pesquisa = Entry(app, font=("Arial", 14), textvariable=campo_pesquisa_var)
    campo_pesquisa.place(x=230, y=270, width=370, height=20)
    campo_pesquisa.bind("<KeyRelease>", filtrar_dados)

    btn_fechar_pesquisa = ttk.Button(app, text="Fechar pesquisa", command=fechar_pesquisa)
    btn_fechar_pesquisa.place(x=610, y=265, width=155, height=30)

    # Mantemos a referência da label, do campo e do botão para escondê-los depois
    app.lb_pesquisar = lb_pesquisar
    app.campo_pesquisa = campo_pesquisa
    app.btn_fechar_pesquisa = btn_fechar_pesquisa

# Criação da TreeView
def criar_treeview(app, on_item_double_click):
    colunas = ("nome", "sobrenome", "genero")
    tree = ttk.Treeview(app, columns=colunas, show="headings")

    tree.heading("nome", text="Nome")
    tree.heading("sobrenome", text="Sobrenome")
    tree.heading("genero", text="Gênero")

    tree.column("nome", minwidth=0, width=250)
    tree.column("sobrenome", minwidth=0, width=250)
    tree.column("genero", minwidth=0, width=100)

    tree.place(x=10, y=300, width=1000, height=290)

    tree.bind("<Double-1>", on_item_double_click)

    return tree

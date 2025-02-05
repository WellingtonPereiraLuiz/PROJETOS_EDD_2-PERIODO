"""
Claudinei de Oliveira - UTF8 - pt-br
- Tkinter: controller.py
JSON - JavaScript Object Notation
"""

from tkinter import Tk, StringVar, messagebox, END, Entry  
import tkinter.ttk as ttk   
import view
import model

# Função principal que inicia a aplicação e conecta a View ao Controller
def iniciar_app():
    global app  
    app = Tk()

    app.mensagem_var = StringVar()
    app.genero_var = StringVar()
    app.campo_pesquisa_var = StringVar()

    view.configurar_app(app)
    frame = view.criar_frame(app)
    view.criar_labels(frame)
    app.nome_entry, app.sobrenome_entry = view.criar_entry(frame)
    view.criar_checkbutton(frame, app.genero_var)

    view.criar_botao(
    app,
    capturar,
    mostrar_campo_pesquisa,
    salvar_edicao,
    excluir_registro,
    app.quit
)


    app.tree = view.criar_treeview(app, on_item_double_click)
    carregar_dados_iniciais(app.tree)

    app.mainloop()

# Carrega os dados iniciais na TreeView
def carregar_dados_iniciais(tree):
    tree.delete(*tree.get_children())  # Limpa a TreeView antes de recarregar os dados

    dados = model.carregar_dados_arquivo()  # Carrega os dados do JSON

    if not isinstance(dados, list):
        messagebox.showerror("Erro", "Formato de dados inválido.")
        return

    for pessoa in dados:
        if isinstance(pessoa, dict) and "nome" in pessoa and "sobrenome" in pessoa and "genero" in pessoa:
            tree.insert('', 'end', values=(pessoa["nome"], pessoa["sobrenome"], pessoa["genero"]))


# Fecha a pesquisa e recarrega todos os dados na TreeView
def fechar_pesquisa():
    app.campo_pesquisa_var.set("")  # Limpa o campo de pesquisa
    app.tree.delete(*app.tree.get_children())  # Remove os itens da TreeView
    carregar_dados_iniciais(app.tree)  # Recarrega os dados do JSON corretamente

    # Esconde a label, o campo de pesquisa e o botão "Fechar pesquisa"
    if hasattr(app, "lb_pesquisar"):
        app.lb_pesquisar.place_forget()
    if hasattr(app, "campo_pesquisa"):
        app.campo_pesquisa.place_forget()
    if hasattr(app, "btn_fechar_pesquisa"):
        app.btn_fechar_pesquisa.place_forget()


# Mostra o campo de pesquisa e configura o botão para fechar a pesquisa
def mostrar_campo_pesquisa():
    view.criar_campo_pesquisa(
        app, 
        app.campo_pesquisa_var, 
        filtrar_dados,
        fechar_pesquisa
    )

# Função que filtra os dados com base no termo de pesquisa
def filtrar_dados(event):
    termo_pesquisa = app.campo_pesquisa_var.get().strip().lower()

    # Se o campo de pesquisa estiver vazio, recarrega todos os dados e mantém os elementos visíveis
    if not termo_pesquisa:
        app.tree.delete(*app.tree.get_children())  # Limpa a TreeView
        carregar_dados_iniciais(app.tree)  # Recarrega todos os registros

        # Mantém os elementos visíveis mesmo se o campo estiver vazio
        if hasattr(app, "lb_pesquisar"):
            app.lb_pesquisar.place(x=10, y=270, width=220, height=20)
        if hasattr(app, "campo_pesquisa"):
            app.campo_pesquisa.place(x=230, y=270, width=370, height=20)
        if hasattr(app, "btn_fechar_pesquisa"):
            app.btn_fechar_pesquisa.place(x=610, y=265, width=155, height=30)
        return

    # Limpa os itens da TreeView antes de exibir os filtrados
    app.tree.delete(*app.tree.get_children())

    for pessoa in model.carregar_dados_arquivo():
        if isinstance(pessoa, dict) and "nome" in pessoa and "sobrenome" in pessoa:
            if termo_pesquisa in pessoa["nome"].lower() or termo_pesquisa in pessoa["sobrenome"].lower():
                app.tree.insert('', 'end', values=(pessoa["nome"], pessoa["sobrenome"], pessoa["genero"]))


# Captura e valida os dados inseridos pelo usuário antes de gravar no arquivo
def capturar():
    nome = model.valida_campo(app.nome_entry.get(), "Nome")
    sobrenome = model.valida_campo(app.sobrenome_entry.get(), "Sobrenome")
    genero_selecionado = app.genero_var.get()

    if not nome or not sobrenome or not genero_selecionado:
        messagebox.showwarning("Aviso", "Todos os campos devem ser preenchidos.")
        return

    pessoa = {"nome": nome, "sobrenome": sobrenome, "genero": genero_selecionado}
    dados = model.carregar_dados_arquivo()
    dados.append(pessoa)
    model.salvar_dados_arquivo(dados)

    app.tree.insert('', 'end', values=(pessoa["nome"], pessoa["sobrenome"], pessoa["genero"]))

    app.nome_entry.delete(0, END)
    app.sobrenome_entry.delete(0, END)
    app.genero_var.set("")  # Agora a variável é resetada corretamente


# Função chamada ao clicar duas vezes em um item da TreeView
def on_item_double_click(event):
    selection = app.tree.selection()
    if selection:
        item = app.tree.item(selection)
        nome, sobrenome, genero = item['values']

        app.nome_entry.delete(0, END)
        app.nome_entry.insert(0, nome)
        app.sobrenome_entry.delete(0, END)
        app.sobrenome_entry.insert(0, sobrenome)
        app.genero_var.set(genero)

# Salva as edições feitas no registro selecionado
def salvar_edicao():
    selection = app.tree.selection()
    if not selection:
        messagebox.showinfo("Aviso", "Nenhum registro selecionado para edição.")
        return

    item = app.tree.item(selection)
    nome_antigo, sobrenome_antigo, genero_antigo = item['values']

    entrada_nome = model.valida_campo(app.nome_entry.get(), "Nome")
    entrada_sobrenome = model.valida_campo(app.sobrenome_entry.get(), "Sobrenome")
    genero_selecionado = app.genero_var.get()

    if not entrada_nome or not entrada_sobrenome or not genero_selecionado:
        return

    nova_pessoa = {"nome": entrada_nome, "sobrenome": entrada_sobrenome, "genero": genero_selecionado}

    # Carrega os dados atuais do JSON
    dados = model.carregar_dados_arquivo()

    if not isinstance(dados, list):
        messagebox.showerror("Erro", "Formato de dados inválido.")
        return

    # Atualiza o registro correspondente sem apagar os outros
    for i, pessoa in enumerate(dados):
        if isinstance(pessoa, dict) and pessoa.get("nome") == nome_antigo and pessoa.get("sobrenome") == sobrenome_antigo and pessoa.get("genero") == genero_antigo:
            dados[i] = nova_pessoa
            break

    model.salvar_dados_arquivo(dados)

    # Atualiza a TreeView
    app.tree.delete(*app.tree.get_children())
    carregar_dados_iniciais(app.tree)

    # Limpa os campos após a edição
    app.nome_entry.delete(0, END)
    app.sobrenome_entry.delete(0, END)
    app.genero_var.set(None)

# Exclui o registro selecionado e o remove do arquivo JSON
def excluir_registro():
    selection = app.tree.selection()
    if not selection:
        messagebox.showwarning("Aviso", "Selecione um registro para excluir.")
        return

    confirm = messagebox.askyesno("Confirmar Exclusão", "Tem certeza que deseja excluir este registro?")
    if confirm:
        item = app.tree.item(selection)
        nome, sobrenome, genero = item['values']

        dados = model.carregar_dados_arquivo()
        dados = [pessoa for pessoa in dados if pessoa["nome"] != nome or pessoa["sobrenome"] != sobrenome or pessoa["genero"] != genero]
        model.salvar_dados_arquivo(dados)

        app.tree.delete(selection)

# Inicia a aplicação
if __name__ == "__main__":
    iniciar_app()


"""
Wellington pereira Luiz
"""
# Verifica o path – módulo os função getcwd() 
# import os
# root_dir = os.getcwd()
# print(f'\nO Path é: {root_dir} \n')

# #  Cria os sub path  clientes e produtos módulo os função mkdir()
# import os
# os.mkdir('clientes')
# os.mkdir('produtos')

# # lista todos os path e arquivos relativos
# import os
# print(f'\nOs paths e arquivos são: {os.listdir(".")} \n')

# # Mostra somente todos os paths 
# import os
# root_dir = os.getcwd()
# print(f'\nDiretorio inicial do projeto: {root_dir} \n')   

# def directory_list(radix):
#     for radix, directories, _ in os.walk(radix):
#         for directory in directories:
#             print(f'\nDiretorios do projeto: {os.path.join(radix, directory)} \n')

# directory_list(root_dir)

# # Mostra os paths em forma de àrvore
# import os

# root_dir = os.getcwd()
# print(f'\n{root_dir}')

# def build_tree(root_dir, prefix=""):
#     files = os.listdir(root_dir)
#     files.sort()

#     for i, filename in enumerate(files):
#         path = os.path.join(root_dir, filename)
#         is_last = i == (len(files) - 1)

#         if os.path.isdir(path):  # Mostra o diretório
#             print(prefix + "└── " + filename if is_last else prefix + "├── " + filename)
#             # Se não for o último item, adicione uma linha vertical abaixo deste diretório
#             extension = "    " if is_last else "│   "
#             build_tree(path, prefix=prefix + extension)
#         else:  # Mostra o arquivo
#             print(prefix + "└── " + filename if is_last else prefix + "├── " + filename)


# build_tree(root_dir)
# print()


# #  Abrindo um sub path - módulo os função chdir()
# import os
# os.chdir('clientes')
# print(f'\nO Path é {os.getcwd()} \n')


# # retornando ao subdiretório pai - módulo os função chdir('.')
# import os
# os.chdir('..')
# print(f'\nO Path é: {os.getcwd()}')

# # Renomeando clientes para cli
# import os
# os.rename('clientes', 'cli')
# print(f'\nO novo nome é: {os.listdir(".")}')

# # Apagando cli
# import os
# os.rmdir('cli')
# print(os.listdir('.'))

# # Cria os path’s teste e o path relativo a teste chamado test_cliente  
# import os
# os.makedirs('teste/test_client')

# root_dir = os.getcwd()
# print(f'\n{root_dir}')

# def build_tree(root_dir, prefix=""):
#     files = os.listdir(root_dir)
#     files.sort()  # ordena arquivos e diretórios

#     for i, filename in enumerate(files):
#         path = os.path.join(root_dir, filename)
#         is_last = i == (len(files) - 1)

#         if os.path.isdir(path):  # Mostra o diretório
#             print(prefix + "└── " + filename if is_last else prefix + "├── " + filename)
#             # Se não for o último item, adicione uma linha vertical abaixo deste diretório
#             extension = "    " if is_last else "│   "
#             build_tree(path, prefix=prefix + extension)
#         else:  # Mostra o arquivo
#             print(prefix + "└── " + filename if is_last else prefix + "├── " + filename)

# build_tree(root_dir)
# print()



# # Verifica subdiretórios existentes módulo os função path.isdir()
# import os
# import os.path
# for subdiretorio in os.listdir('.'):
#     if os.path.isdir(subdiretorio):
#         print(f'{subdiretorio}')



# # Verifica se um subdiretório existe módulo os função path.exists()
# import os.path
# if os.path.exists('cli'):
#     print('O diretório existe')
# else:
#     print('O diretório não existe')



# # Identifica o sistema operacional - modo os função name() – Linux/IOS/Windows
# import os
# print(os.name)



# # Identifica detalhes no sistema operacional – Linux/IOS
# import os
# print(os.uname())


# # Identifica detalhes no sistema operacional Windows
# import sys
# print(sys.platform)




# # # Tkinter Listbox()
# from tkinter import *
# from tkinter import ttk

# # Constantes para configuração
# FONT = ('Arial', 12)
# FG_COLOR = '#FA0404'

# def imprimir_estado_civil():
#     estado_civil = lb_es_civil.get(ACTIVE)
#     # Atualiza o texto do rótulo com o estado civil selecionado
#     lb_2.config(text=f'Estado Civil selecionado = {estado_civil}')

# # Configuração da janela principal
# janela = Tk()
# janela.title('IFRO - Campus Ariquemes - ADS - Estrutura de Dados')
# janela.geometry('500x500')

# # Lista de estados civis
# lista_estado_civil = ['Nenhum', 'Solteiro(a)', 'Casado(a)', 'União estável',
#                       'Divorciado(a)', 'Desquitado(a)', 'Viúvo(a)']

# # Rótulo para estado civil
# Label(janela, text='Estado civil:', fg=FG_COLOR, font=FONT).place(x=15, y=45)

# # Listbox para seleção do estado civil
# lb_es_civil = Listbox(janela)
# for estadocivil in lista_estado_civil:
#     lb_es_civil.insert(END, estadocivil)
# lb_es_civil.place(x=110, y=45, width=150)

# # Botão para confirmar a seleção do estado civil
# btn_estado_civil = Button(janela, text='Clique para ver o estado civil selecionado',
#                           command=imprimir_estado_civil)
# btn_estado_civil.place(x=110, y=200, width=350)

# # Rótulo que mostra o estado civil selecionado, inicialmente vazio
# lb_2 = Label(janela, text="", font=FONT)
# lb_2.place(x=150, y=350)

# # Inicia a interface
# janela.mainloop()




# # Tkinter Combobox()

# from tkinter import *
# from tkinter import ttk

# # Constantes para configuração
# FONT = ('Arial', 12)
# FG_COLOR = '#FA0404'

# def imprimir_estado_civil():
#     estado_civil = cb_es_civil.get()
#     # Atualiza o texto do rótulo com o estado civil selecionado
#     lb_2.config(text=f'Estado Civil selecionado = {estado_civil}')

# # Configuração da janela principal
# janela = Tk()
# janela.title('IFRO - Campus Ariquemes - ADS - Estrutura de Dados')
# janela.geometry('500x500')

# # Lista de estados civis
# lista_estado_civil = ['Nenhum', 'Solteiro(a)', 'Casado(a)', 'União estável',
#                       'Divorciado(a)', 'Desquitado(a)', 'Viúvo(a)']

# # Rótulo para estado civil
# Label(janela, text='Estado civil:', fg=FG_COLOR, font=FONT).place(x=15, y=45)

# # Combobox para seleção do estado civil
# cb_es_civil = ttk.Combobox(janela, values=lista_estado_civil, font=FONT)
# cb_es_civil.place(x=110, y=45, width=150)
# cb_es_civil.set(lista_estado_civil[0])  # Define o valor padrão como o primeiro da lista

# # Botão para confirmar a seleção do estado civil
# btn_estado_civil = Button(janela, text='Clique para ver o estado civil selecionado',
#                           command=imprimir_estado_civil)
# btn_estado_civil.place(x=110, y=200, width=350)

# # Rótulo que mostra o estado civil selecionado, inicialmente vazio
# lb_2 = Label(janela, text="", font=FONT)
# lb_2.place(x=150, y=350)

# # Inicia o loop principal da interface
# janela.mainloop()






# # Tkinter Checkbox() com Json

# import json
# from tkinter import *
# from tkinter import messagebox

# # Constantes para configuração
# FONT = ('Arial', 12)
# JSON_FILENAME = 'esportes_selecionados.json'

# # Função para imprimir e salvar os esportes selecionados
# def salvar_esportes_selecionados():
#     esportes_selecionados = {esporte: var.get() for esporte, var in esportes_vars.items()}
#     with open(JSON_FILENAME, 'w', encoding='utf-8') as json_file:
#         json.dump(esportes_selecionados, json_file, ensure_ascii=False, indent=4)
#     messagebox.showinfo('Informação', 'Esportes salvos com sucesso!')

# # Configuração da janela principal
# janela = Tk()
# janela.title('Seleção de Esportes')
# janela.geometry('500x500')

# # Esportes disponíveis e suas respectivas variáveis de estado
# esportes = ['Futebol', 'Vôlei', 'Basquete', 'Natação', 'Atletismo']
# esportes_vars = {esporte: IntVar() for esporte in esportes}

# # Carrega as seleções existentes do arquivo JSON
# try:
#     with open(JSON_FILENAME, 'r', encoding='utf-8') as json_file:
#         esportes_selecionados_existente = json.load(json_file)
#     # Atualiza as variáveis de estado com os valores existentes
#     for esporte, var in esportes_vars.items():
#         var.set(esportes_selecionados_existente.get(esporte, 0))
# except FileNotFoundError:
#     # Arquivo JSON não existe, então não há seleções prévias
#     pass

# # Rótulos e caixas de seleção para cada esporte
# for i, (esporte, var) in enumerate(esportes_vars.items()):
#     Checkbutton(janela, text=esporte, variable=var, font=FONT).place(x=15, y=45 + i*30)

# # Botão para salvar a seleção dos esportes
# btn_salvar = Button(janela, text='Salvar seleção', command=salvar_esportes_selecionados)
# btn_salvar.place(x=15, y=200, width=200)

# # Inicia o loop principal da interface
# janela.mainloop()

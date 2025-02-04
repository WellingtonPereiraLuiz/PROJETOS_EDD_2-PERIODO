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

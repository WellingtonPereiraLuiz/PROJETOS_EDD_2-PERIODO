# Função que cria um nó
def create_node(dados):
    return {'dados': dados, 'proximo': None, 'anterior': None}  # Retorna um novo nó com dados fornecidos e referências nulas para os nós anterior e próximo

# Função que obtém os dados armazenados em um nó
def get_data(node):
    return node['dados']  # Retorna o valor armazenado na chave 'dados' do nó

# Função que obtém a referência ao próximo nó de um nó
def get_next(node):
    return node['proximo']  # Retorna a referência ao próximo nó armazenada na chave 'proximo' do nó

# Função que obtém a referência ao nó anterior de um nó
def get_previous(node):
    return node['anterior']  # Retorna a referência ao nó anterior armazenada na chave 'anterior' do nó

# Função que define a referência ao próximo nó de um nó
def set_next(node, new_next):
    node['proximo'] = new_next  # Define a nova referência ao próximo nó na chave 'proximo' do nó

# Função que define a referência ao nó anterior de um nó
def set_previous(node, new_previous):
    node['anterior'] = new_previous  # Define a nova referência ao nó anterior na chave 'anterior' do nó

# Exemplo de uso das funções

# Criando três nós
node1 = create_node('Nó 1')  # Cria um novo nó com dados "Nó 1" e atribui à variável node1
node2 = create_node('Nó 2')  # Cria um novo nó com dados "Nó 2" e atribui à variável node2
node3 = create_node('Nó 3')  # Cria um novo nó com dados "Nó 3" e atribui à variável node3

# Ligando os nós em uma lista duplamente encadeada
set_next(node1, node2)  # Define o próximo nó de node1 como node2, conectando node1 a node2
set_previous(node2, node1)  # Define o nó anterior de node2 como node1, estabelecendo a ligação de volta de node2 a node1
set_next(node2, node3)  # Define o próximo nó de node2 como node3, conectando node2 a node3
set_previous(node3, node2)  # Define o nó anterior de node3 como node2, estabelecendo a ligação de volta de node3 a node2

print(f'\nImprimindo os dados de cada nó')
print(f'Dados do node1: {get_data(node1)}')  # Imprime os dados armazenados no nó node1
print(f'Dados do node2: {get_data(node2)}')  # Imprime os dados armazenados no nó node2
print(f'Dados do node3: {get_data(node3)} \n')  # Imprime os dados armazenados no nó node3

print(f'\nImprimindo as referências ao próximo e ao anterior de cada nó')
print(f'Próximo ao node1: {get_data(get_next(node1))}')  # Obtém o próximo nó de node1, pega seus dados e imprime
print(f'Anterior ao node2: {get_data(get_previous(node2))}')  # Obtém o nó anterior de node2, pega seus dados e imprime
print(f'Próximo ao node2: {get_data(get_next(node2))}')  # Obtém o próximo nó de node2, pega seus dados e imprime
print(f'Anterior ao node3: {get_data(get_previous(node3))} \n')  # Obtém o nó anterior de node3, pega seus dados e imprime

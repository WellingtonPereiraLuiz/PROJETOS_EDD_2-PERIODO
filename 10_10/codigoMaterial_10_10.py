"""
import numpy as np


vetor_alunos = np.empty (10, dtype = bytearray)

print(f'\nvetor_alunos: {vetor_alunos}')
print(f'\nTipo de estrutura do vetor alunos: {type(vetor_alunos)}')

for n in range(3):
    vetor_alunos[n] = input(f'\n Nome do aluno {str(n+1)}° aluno(a): ')

print(f'\nOs alunos(as) que entraram na sala são: {vetor_alunos} \n')

aluno = input('\nInforme o nome do aluno(a) a pesquisar:')

for n in range(10):
    if aluno == vetor_alunos[n]:
        print(f'\nAluno(a) encontrado(a): índice: {str(n)} - nome {vetor_alunos[n]} \n')

if vetor_alunos[n] != aluno:
    print(f'\nAluno(a) não encontrado(a)!!! \n')


aluno = input('\nInforme o nome do aluno(a) a pesquisar para alterar seu nome:')

for n in range(3):
    if aluno == vetor_alunos[n]:

        print(f'\nAluno(a) encontrado(a): índice: {str(n)} - nome: {vetor_alunos(n)} \n')
        aluno_alterar = input('\nDigite as alterações: ')

        if aluno == aluno_alterar:
            print('\nVocê digitou o mersmo nome que pesquisou... ')
        else:
            vetor_alunos[n] = aluno_alterar
        break
    else:
        print('Aluno(a) não encontrado(a)!!!')
    
print(f'\nNome dos alunos(as): {vetor_alunos} \n')


aluno = input('\nInforme o nome do aluno(a) a pesquisar para excluir seu nome:')

for n in range(len(vetor_alunos)):
    if aluno == vetor_alunos[n]:

        print(f'\nAluno(a) encontrado(a): índice: {str(n)} - nome: {vetor_alunos[n]} \n')
        deseja_excluir = input(f'\nDeseja excluir esse aluno(a) do vetor: (Sim/Não)').upper()

        if deseja_excluir == 'SIM':
            vetor_alunos = np.delete(vetor_alunos, n)
            print('\nAluno excluído(a) com sucesso!')
        else:
            print('\nOperação cancelada pelo usuário.')
        break
    else:
        print(f'\nAluno(a) não encontrado(a)!!!')


print(f'\nNome dos alunos(as): {vetor_alunos}')



def custom_sort(item):
    return item if item is not None else "zzzz"

vetor_alunos[:] = sorted(vetor_alunos, key=custom_sort)

print(f'\nNome dos alunos(as) após ordenação>: {vetor_alunos} \n')

vetor_alunos = np.array(['Zen', 'Marga', 'Al', 'Bru', 'Car', 'Dia', 'Ev', 'Fab', 'Gab', 'Hel'], dtype=object)

print(f'\nNome dos alunos(as) Após ordenação: {sorted(vetor_alunos)} \n')

print(f'\nNome dos alunos(as) Após ordenação descendente: {sorted(vetor_alunos, reverse=True)} \n')




import numpy as np

vetor_nomes = np.empty(3, dtype=object)
nomes_inseridos = 0

while nomes_inseridos < 3:
    nome = input(f'\nDigite o {nomes_inseridos + 1}° nome:')

    if nome not in vetor_nomes:
        vetor_nomes[nomes_inseridos] = nome
        nomes_inseridos += 1
    else:
        print('Esse nome ja foi inserido. Por favor, diogite um nome diferente.')

nomes_ordenados = sorted([nome for nome in vetor_nomes if nome is not None], reverse=True)

print()
for nome in nomes_ordenados: 
    print(f'Nomes em ordem reversa: {nome}')
print()
"""

# Função para criar um novo nó na lista encadeada
def create_node(initdata): # initdata é o valor inicial que o novo nó vai armazenar
    # Cria e retorna um dicionário que representa um nó
    # 'data' armazena o valor do nó e 'next' que é uma referência ao próximo nó,
    # inicialmente definida como None (nulo)
    return {'data': initdata, 'next': None} # Retorna o novo nó criado com o valor inicial e referência nula ao próximo nó

# Função para obter o valor armazenado em um nó
def get_data(node): # node é o nó cujo valor armazenado queremos obter
    # Retorna o valor armazenado na chave 'data' do dicionário que representa o nó
    return node['data'] # Retorna o valor armazenado no nó

# Função para obter a referência ao próximo nó de um nó
def get_next(node): # node é o nó cuja referência ao próximo nó queremos obter
    # Retorna o valor armazenado na chave 'next' do dicionário que representa o nó
    # Isso fornece uma referência ao próximo nó na lista encadeada
    return node['next'] # Retorna a referência ao próximo nó

# Função para definir (ou alterar) o valor armazenado em um nó
def set_data(node, newdata): # node é o nó cujo valor queremos definir ou alterar; newdata é o novo valor a ser armazenado
    # Define o valor na chave 'data' do dicionário que representa o nó com o novo valor fornecido
    node['data'] = newdata # Define o novo valor para o nó

# Função para definir (ou alterar) a referência ao próximo nó de um nó
def set_next(node, newnext): # node é o nó cuja referência ao próximo nó queremos definir ou alterar; newnext é a nova referência
    # Define o valor na chave 'next' do dicionário que representa o nó com a nova referência fornecida
    # Isso é usado para alterar a referência ao próximo nó na lista encadeada
    node['next'] = newnext # Define a nova referência ao próximo nó

# Criando um nó com o valor "primeiro"
# Neste momento, o nó não tem referência para um próximo nó
node1 = create_node('Abacate')

# Criando outro nó com o valor "segundo". Da mesma forma, esse
# nó também não tem uma referência para um próximo nó
node2 = create_node('Abobrinha')

# Conectando o primeiro nó ao segundo. Estamos definindo que o
# próximo nó após "node1" é "node2"
set_next(node1, node2)

# Imprimindo os dados armazenados no primeiro nó.
print(f'\nO primeiro nó é: {get_data(node1)}')

# Imprimindo os dados armazenados no nó que vem após
# "node1", que é "node2".
print(f'\nO segundo nó é: {get_data(get_next(node1))} \n')



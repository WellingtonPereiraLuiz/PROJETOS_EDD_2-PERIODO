'Wellington Pereira Luiz'

# Implementando fila em Python - abordagem por funções - lista encadeada com extremidade dupla 
'''def criaNo(valor):
    return {
        'valor':valor,
        'proximo': None
    }

def mostraNo(no):
    print(f'\nValor do nó -> {no['valor']}\n')

primeiro_no = criaNo(53)
mostraNo(primeiro_no)'''

# Implementação completa de  FILA em Python - abordagem por funções - lista encadeada com extremidade dupla
'''
def criaNo(valor):
    return {
        'valor': valor,
        'proximo': None
    }

def criaLista():
    return {
        'primeiro': None,
        'ultimo': None
    }
def listaVazia(lista):
    return lista['primeiro'] == None

def insereFinal(lista, valor):
    novo = criaNo(valor)
    if listaVazia(lista):
        lista['primeiro'] = novo
    else:
        lista['ultimo']['proximo'] = novo
    lista['ultimo'] = novo

def excluiInicio(lista):
    if listaVazia(lista):

        print(f'\nA lista está vazia\n')
        return
    
    temp = lista['primeiro']

    if lista['primeiro']['proximo'] == None:
        lista['ultimo'] = None
    lista['primeiro'] = lista['primeiro']['proximo']
    return temp

def criaFila():
    return {
        'lista': criaLista()
        }

def filaVazia(fila):
    return listaVazia(fila['lista'])

def enfileirar(fila, valor):
    insereFinal(fila['lista'], valor)

def desenfileirar(fila):
    return excluiInicio(fila['lista'])

def mostraInicio(fila):
    if fila['lista']['primeiro'] == None:
        return 'A fila está vazia'
    return fila['lista']['primeiro']['valor']

#A função abaixo foi criada para exibir os elementos da lista sem a necessidade da redundancia de comandos escritos em excesso.
def mostraFila(fila):
    este_no = fila['lista']['primeiro']
    print(f'\nFila atual')
    while este_no:
        print(este_no['valor'])
        este_no = este_no['proximo']
    print()

fila = criaFila()

print(f'\nA fila está vazia? {filaVazia(fila)}\n')

enfileirar(fila, 15)
enfileirar(fila, 26)
enfileirar(fila, 49)

#Este conjunto de instruções se repete desta linha até a linha 92
# este_no = fila['lista']['primeiro']
# print()
# while este_no:                  
#     print(este_no['valor'])
#     este_no = este_no['proximo']
mostraFila(fila) #Esta linha chama a função que otimiza a operação de exibir os elementos é chamada

print(f'\nInício da fila: {mostraInicio(fila)}\n')
dsnflrado = desenfileirar(fila)

print(f'\nDesinfileirado: {dsnflrado["valor"]}\n')
print(f'\nNovo início da fila é: {mostraInicio(fila)}\n')

# Este conjunto de instruções também se repete desta linha té a linha 108
# este_no = fila['lista']['primeiro']
# print(f'\nFila atual')
# while este_no:
#     print(este_no['valor'])
#     este_no = este_no['proximo']
# print()
mostraFila(fila) #Esta linha chama a função que otimiza a operação de exibir os elementos é chamada
'''

"""
#Exercício de Otimização e Justificação de Código
# Identificando e resolvendo repeticoes no codigo de Fila com lista encadeada

import numpy as np

# Funcao pra criar um No
def CriaNo(valor):
    return {
        'anterior': None,
        'valor': valor,
        'proximo': None
    }

# Funcao pra criar a Fila
def Queue():
    return {
        'inicio': None,
        'fim': None
    }

# Verifica se a Fila ta vazia
def IsEmpty(fila):
    return fila['inicio'] is None

# Adiciona um valor na fila
def Enqueue(fila, valor):
    novo_no = CriaNo(valor)

    if IsEmpty(fila):
        fila['inicio'] = novo_no
        fila['fim'] = novo_no
    else:
        novo_no['anterior'] = fila['fim']
        fila['fim']['proximo'] = novo_no

    fila['fim'] = novo_no

# Remove um valor da fila
def Dequeue(fila):
    if IsEmpty(fila):
        print("\nFila ta vazia\n")
        return None

    temp = fila['inicio']

    if fila['inicio']['proximo'] == None:
        fila['fim'] = None

    fila['inicio'] = fila['inicio']['proximo']
    return temp

# Exibe os elementos da fila de forma clara
def MostraFila(fila):
    if IsEmpty(fila):
        print("\nA fila ta vazia...\n")
        return

    print("\nFila atual:")
    atual = fila['inicio']
    while atual:
        print(atual['valor'])
        atual = atual['proximo']
    print()

# Fila pra testar
fila = Queue()

print(f"\nFila ta vazia? {IsEmpty(fila)}\n")

Enqueue(fila, 15)
Enqueue(fila, 26)
Enqueue(fila, 49)

MostraFila(fila)

print(f"\nInicio da fila: {fila['inicio']['valor']}\n")
removido = Dequeue(fila)

print(f"\nElemento removido: {removido['valor']}\n")
MostraFila(fila)

# Explicando as repeticoes e solucoes
# As repeticoes no codigo eram trechos que mostravam os elementos da fila em duas partes diferentes.
# Resolvi isso criando a funcao MostraFila que deixa tudo mais facil de entender e reduz o trabalho de escrever o mesmo trecho varias vezes.
"""
# Exercícios – Filas – abordagem por funções - queue(), enqueue(), dequeue() e isEmpty(). 
# Enunciado: Sistema de Chamados de Atendimento 
# Você foi contratado para desenvolver um sistema para um call center. O 
# sistema tem como principal objetivo gerenciar chamados de clientes que 
# desejam suporte técnico. Os chamados devem ser processados na ordem em 
# que foram recebidos. 
#Funcionalidades esperadas:

#Gerenciar uma lista de espera para atendimento técnico.
#Adicionar solicitações à lista de espera.
#Atualizar a prioridade de um chamado existente.
#Excluir chamados atendidos da lista.
#Critérios:
# Utilizar as funções queue(), enqueue(), dequeue(), e isEmpty().
# Solicitar entrada do usuário para adicionar ou modificar chamados.
# Permitir a visualização completa da lista de espera.
# Implementar a exclusão de chamados finalizados da fila.

# Gerenciamento de fila para atendimento técnico

# Função para criar um Nó
def CriaNo(valor):
    return {
        'anterior': None,
        'valor': valor,
        'proximo': None
    }

# Função para criar a Fila
def Queue():
    return {
        'inicio': None,
        'fim': None
    }

# Verifica se a Fila está vazia
def IsEmpty(fila):
    return fila['inicio'] is None

# Adiciona um chamado na fila
def Enqueue(fila, valor):
    novo_no = CriaNo(valor)

    if IsEmpty(fila):
        fila['inicio'] = novo_no
        fila['fim'] = novo_no
    else:
        novo_no['anterior'] = fila['fim']
        fila['fim']['proximo'] = novo_no

    fila['fim'] = novo_no

# Remove um chamado da fila (finalizado)
def Dequeue(fila):
    if IsEmpty(fila):
        print("\nA fila está vazia\n")
        return None

    temp = fila['inicio']

    if fila['inicio']['proximo'] == None:
        fila['fim'] = None

    fila['inicio'] = fila['inicio']['proximo']
    return temp

# Atualiza a prioridade de um chamado
def AtualizaPrioridade(fila, chamado):
    atual = fila['inicio']

    while atual:
        if atual['valor'] == chamado:
            if atual == fila['inicio']:
                print("\nO chamado já está no início da fila\n")
                return

            anterior = atual['anterior']
            proximo = atual['proximo']

            if anterior:
                anterior['proximo'] = proximo
            if proximo:
                proximo['anterior'] = anterior
            if atual == fila['fim']:
                fila['fim'] = anterior

            atual['anterior'] = None
            atual['proximo'] = fila['inicio']
            fila['inicio']['anterior'] = atual
            fila['inicio'] = atual
            print(f"\nChamado '{chamado}' movido para o início da fila\n")
            return
        atual = atual['proximo']

    print(f"\nChamado '{chamado}' não encontrado\n")

# Exibe os elementos da fila
def MostraFila(fila):
    if IsEmpty(fila):
        print("\nA fila está vazia...\n")
        return

    print("\nFila atual:")
    atual = fila['inicio']
    while atual:
        print(atual['valor'])
        atual = atual['proximo']
    print()

# Simulação do gerenciamento de fila
fila = Queue()

print(f"\nFila está vazia? {IsEmpty(fila)}\n")

# Adicionando chamados
Enqueue(fila, "Suporte ao sistema")
Enqueue(fila, "Reinstalação de software")
Enqueue(fila, "Problema de conectividade")

MostraFila(fila)

# Atualizando a prioridade de um chamado
AtualizaPrioridade(fila, "Reinstalação de software")
MostraFila(fila)

# Removendo chamados finalizados
removido = Dequeue(fila)
print(f"\nChamado removido: {removido['valor']}\n")
MostraFila(fila)

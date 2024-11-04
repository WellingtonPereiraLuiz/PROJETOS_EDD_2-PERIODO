# Criando o modelo da lista encadeada – abordagem por funções
'''EXEMPLO 1
def create_node(dados):
    return {'dados': dados, 'proximo': None, 'anterior': None}

def get_data(node):
    return node['dados']

def get_next(node):
    return node['proximo']

def get_previous(node):
    return node['anterior']

def set_next(node, new_next):
    node['proximo'] = new_next

def set_previous(node, new_previous):
    node['anterior'] = new_previous

# Exemplo de uso das funções

# Criando três nós
node1 = create_node("Nó 1")
node2 = create_node("Nó 2")
node3 = create_node("Nó 3")

# Ligando os nós em uma lista duplamente encadeada
set_next(node1, node2)
set_previous(node2, node1)

set_next(node2, node3)
set_previous(node3, node2)

print('\nImprimindo os dados de cada nó')
print(f'Dados do node1: {get_data(node1)}')
print(f'Dados do node2: {get_data(node2)}')
print(f'Dados do node3: {get_data(node3)} \n')

print('\nImprimindo as referências ao próximo e ao anterior de cada nó')
print(f'Próximo ao node1: {get_data(get_next(node1))}')
print(f'Anterior ao node2: {get_data(get_previous(node2))}')
print(f'Próximo ao node2: {get_data(get_next(node2))}')
print(f'Anterior ao node3: {get_data(get_previous(node3))} \n')
'''

# Desenvolvendo a função search()
'''EXEMPLO 2
def search(self, item):
    current = self.head
    found = False

    while current is not None and not found:

        if current.getData() == item:
            found = True
        else:
            current = current.getNext()

    return found
'''

# Caso de uso da função search()
'''EXEMPLO 3
# Função que cria um nó
def create_node(intidata):
    return {'data': intidata, 'next': None}

# Função para obter a referência ao próximo nó de um nó
def get_next(node):
    return node['next']

# Função para definir (ou alterar) a referência ao próximo
def set_next(node, newnext):
    node['next'] = newnext

# Função para buscar um valor específico na lista encadeada
def search(head, item):
    current = head
    found = False

    while current is not None and not found:
        if get_data(current) == item:
            found = True
        else:
            current = get_next(current)

    return found

# Função para obter o valor armazenado em um nó
def get_data(node):
    return node['data']

# Criando nós
node1 = create_node('Abacate')
node2 = create_node('Banana')
node3 = create_node('Caju')

# Conectando os nós
set_next(node1, node2)
set_next(node2, node3)

set_next(node2, node3)

head = node1

print(f'\nProcurando por "Banana: " {search(head, "Banana")} \n')

print(f'\nProcurando por "Laranja: " {search(head, "Laranja")} \n')
'''

# Removendo um item - função remove()
'''EXEMPLO 4
def remove(self, item):
    current = self.head
    previous = None
    found = False

    while not found:
        if current.getData() == item:
            found = True
        else:
            previous = current
            current = current.getNext()

    if previous == None:
        self.head = current.getNext()
    else:
        previous.setNext(current.getNext())
'''
# Caso de uso da função remove() em listas simplesmente encadeadas ordenadas
''' EXEMPLO 5
def create_node(data):
    return {'data': data, 'next': None}

def add(head, value):
    new_node = create_node(value)
    if head is None:
        return new_node
    else:
        current = head
        while current['next'] is not None:
            current = current['next']
        current['next'] = new_node
        return head

def remove(head, item):
    current = head
    previous = None
    found = False

    while current is not None and not found:
        if current['data'] == item:
            found = True
        else:
            previous = current
            current = current['next']

    if found:
        if previous is None:
            head = current['next']
        else:
            previous['next'] = current['next']
        return head, "Item encontrado e removido"
    else:
        return head, "Item NÃO encontrado"

def display(head):
    current = head
    while current is not None:
        print(current['data'])
        current = current['next']

def size(head):
    current = head
    count = 0
    while current is not None:
        count += 1
        current = current['next']
    return count

head = None
head = add(head, 'A')
head = add(head, 'B')
head = add(head, 'C')

print(f'\nLista inicial:')
display(head)

print(f'\nTamanho da Lista: {size(head)}')

head, message = remove(head, 'B')

print(f'\n{message}')

print(f'\nLista após remoção:')
display(head)

print(f'\nTamanho da Lista: {size(head)}\n')
'''

# Pesquisa um item na lista simplesmente encadeada ordenada
'''EXEMPLO 6
def search(self, item):
    current = self.head
    found = False
    stop = False

    while current is not None and not found and not stop:
        if current.getData() == item:
            found = True
        else:
            if current.getData() > item:
                stop = True
            else:
                current = current.getNext()
    return found
'''

# Caso de uso da função search() em listas simplesmente encadeadas ordenadas.
'''
def createNode(dados):
    return {'data': dados, 'next': None}

def getData(node):
    return node['data']

def getNext(node):
    return node['next']

def set_data(node, newdata):
    node['data'] = newdata

def setNext(node, newnext):
    node['next'] = newnext

def add_ordered(head, item):
    current = head
    previous = None
    stop = False

    while current is not None and not stop:

        if current['data'] > item:
            stop = True
        else:
            previous = current
            current = current['next']
        
        temp = createNode(item)

    if previous is None:
        temp['next'] = head
        head = temp
    else:
        temp['next'] = current
        previous['next'] = temp

    return head
    
def search(head, item):
    current = head
    found = False
    stop = False

    while current is not None and not found and not stop:
        if current['data'] == item:
            found = True
        else:
            if current['data'] > item:
                stop = True
            else:
                current = current['next']
    return found

head = createNode(10)
head = add_ordered(head, 5)
head = add_ordered(head, 15)
head = add_ordered(head, 20)
head = add_ordered(head, 25)

print(f'\nO número 15 está na lista? {search(head, 10)}')
print(f'\nO número 30 está na lista? {search(head, 30)}\n')
'''

# Exercício c)

def create_node(dados):
    return {'data': dados, 'next': None}

def get_data(node):
    return node['data']

def get_next(node):
    return node['next']

def set_next(node, newnext):
    node['next'] = newnext

def add_ordered(head, item):
    current = head
    previous = None
    stop = False

    while current is not None and not stop:
        if get_data(current) > item:
            stop = True
        else:
            previous = current
            current = get_next(current)
        
    temp = create_node(item)

    if previous is None:
        set_next(temp, head)
        head = temp
    else:
        set_next(temp, current)
        set_next(previous, temp)

    return head
    
def search(head, item):
    current = head
    found = False
    stop = False

    while current is not None and not found and not stop:
        if get_data(current) == item:
            found = True
        else:
            if get_data(current)> item:
                stop = True
            else:
                current = get_next(current)
    if found:
        return f'Item encontrado {item}'
    else: 
        return 'Item NÃO encontrado'


def remove(head, item):
    current = head
    previous = None
    found = False

    while not found and current is not None:
        if get_data(current) == item:
            found = True
        else:
            previous = current
            current = get_next(current)
    if found:
        if previous == None:
            head = get_next(current)
        else:
            set_next(previous, get_next(current))
        
    if found:
        return f'Item encontrado e removido'
    else: 
        return 'Item NÃO encontrado'

def display(head):
    current = head
    
    while current is not None:
        print(get_data(current), end=', ')
        current = get_next(current)
    
    print()

def menu():
    print("\nOpções:")
    print("1. Inserir um número na lista")
    print("2. Remover um número da lista")
    print("3. Procurar um número na lista")
    print("4. Apresentar lista")
    print("5. Sair")

def main():
    head = None
    while True:
        menu()
        escolha = int(input("\nDigite sua escolha: "))
        
        if escolha == 1:
            item = int(input("\nDigite o número que deseja inserir: "))
            head = add_ordered(head, item)
            print(f"\nO número {item} foi inserido com sucesso!")
        
        elif escolha == 2:
            item = int(input("\nDigite o número que deseja remover: "))
            message = remove(head, item)
            print(f"\n{message}")
            if message == "Item encontrado e removido":
                print("\nLista atualizada:")
                display(head)

        elif escolha == 3:
            item = int(input("\nDigite o número que deseja procurar: "))
            print(f"\n{search(head, item)}")
        
        elif escolha == 4:
            print("\nLista atual:")
            display(head)
        
        elif escolha == 5:
            print("\nSaindo...")
            break

        else:
            print("\nEscolha inválida! Tente novamente.")

main()

"""

def create_node(data):
    return{'data': data, 'next': None}

def append(head, data):
    new_node = create_node(data)

    if not head:
        new_node['next'] = new_node
        return new_node
    
    else: 
        temp = head
        while temp['next']  != head:
            temp= temp['next']
        temp['next'] = new_node

        new_node['next'] = head

        return head
    
def search(head, key):
    current = head
    index = 0
    while current:
        if current:
            if current['data'] == key:
                print(f'Elemento encontrado: {current["data"]} na posição {index}')
                return index, current
        
        current = current['next']
        index += 1

        if current == head:
            break
    print('Elemento não encontrado')
    return None, None

def update(head, key, new_data):
    _, node = search(head, key)
    if node:
        node["data"] = new_data

def remove(head, key):
    _, node_to_remove = search(head, key)
    if not node_to_remove:
        return head
    
    prev = None
    current = head

    while current:
        if current["data"] == key:
            if prev:
                prev["next"] = current["next"]

                if current == head:
                    head = current["next"]
            
            else:
                head = current["next"]
            
            return head
        
        prev = current
        current = current["next"]

        if current == head:

            break
    
    return head

def menu():
    head = None

def display(head):
    nodes = []
    temp = head
    while True:
        nodes.append(str(temp["data"]))

        temp = temp["next"] 

        if temp  == head:
            break
    print(" -> ".join(nodes))

def menu():
    head = None
     
    while True:
        print('\n>>> Menu lista simplesmente encadeda com encadeamento circular <<<')
        print('1: Inserir 2 elementos')
        print('2: Inserir m elementos')
        print('3: Pesquisar elemento')
        print('4: Alterar elemento')
        print('5: Excluir elemento')
        print('6: Exibir lista')
        print('-1: Sair')
        choice = int(input('Digite sua escolha: '))

        if choice == -1:
            break
        elif choice == 1:
            data1 = input('Digite o 1 elemento: ')
            data2 = input('Digite o 2 elemento: ')

            head = append(head, data1)
            head = append(head, data2)
        elif choice == 2:
            n = int(input('Quakntos elementos deseja inserir'))
            for i in range(n):
                data = input(f'Digite o {i+1} elemento:')
                head = append(head, data)
        elif choice == 3:
            key = input('Digite o elemento a ser pesquisado: ')
            search(head, key)
        elif choice == 4:
            key = input('Digite o elemento a ser alterado: ')
            new_data = input('Digite o novo valor: ')
            update(head, key, new_data)
        elif choice == 5:
            key = input('Digite o elemento a ser excluido: ')
            head = remove(head, key)
        elif choice == 6:
            display(head)
        else:
            print('Opção inválida!')

if __name__ == "__main__":
    menu()
"""
def create_node(data):
    return {'data': data, 'next': None, 'prev': None}

def append(head, data):
    new_node = create_node(data)

    if not head:
        new_node['next'] = new_node
        new_node['prev'] = new_node
        return new_node
    else:
        tail = head['prev']
        tail['next'] = new_node
        new_node['prev'] = tail
        new_node['next'] = head
        head['prev'] = new_node

    return head

def search(head, key):
    current = head
    index = 0

    while current:
        if current['data'] == key:
            print(f'Elemento encontrado: {current["data"]} na posição {index}')
            return index, current

        current = current['next']
        index += 1

        if current == head:
            break

    print('Elemento não encontrado')
    return None, None

def update(head, key, new_data):
    _, node = search(head, key)
    if node:
        node['data'] = new_data

def remove(head, key):
    _, node_to_remove = search(head, key)

    if not node_to_remove:
        return head

    if node_to_remove['prev']:
        node_to_remove['prev']['next'] = node_to_remove['next']

    if node_to_remove['next']:
        node_to_remove['next']['prev'] = node_to_remove['prev']

    if node_to_remove == head:
        if node_to_remove['next'] == node_to_remove:
            head = None
        else:
            head = node_to_remove['next']

    return head

def display(head):
    if not head:
        print(f'\n>>> Lista vazia!!!')
        return

    nodes = []
    temp = head
    while True:
        nodes.append(str(temp["data"]))
        temp = temp["next"]

        if temp == head:
            break
    print(" <-> ".join(nodes))

def menu():
    head = None

    while True:
        print('\n>>> Menu - lista de encadeamento duplo circular <<<')
        print('1: Inserir 2 elementos')
        print('2: Inserir n elementos')
        print('3: Pesquisar elemento')
        print('4: Alterar elemento')
        print('5: Excluir elemento')
        print('6: Exibir lista')
        print('-1: Sair')
        choice = int(input('Digite sua escolha: '))

        if choice == -1:
            break
        elif choice == 1:
            data1 = input('Digite o 1º elemento: ')
            data2 = input('Digite o 2º elemento: ')

            head = append(head, data1)
            head = append(head, data2)

        elif choice == 2:
            n = int(input('Quantos elementos deseja inserir? '))
            for i in range(n):
                data = input(f'Digite o {i + 1}º elemento: ')
                head = append(head, data)

        elif choice == 3:
            key = input('Digite o elemento a ser pesquisado: ')
            search(head, key)

        elif choice == 4:
            key = input('Digite o elemento a ser alterado: ')
            new_data = input('Digite o novo valor: ')
            update(head, key, new_data)

        elif choice == 5:
            key = input('Digite o elemento a ser excluído: ')
            head = remove(head, key)

        elif choice == 6:
            display(head)
        else:
            print('Opção inválida!')

if __name__ == '__main__':
    menu()


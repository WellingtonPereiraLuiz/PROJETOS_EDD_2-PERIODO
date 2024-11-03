# Manipulando lista duplamente encadeada – insere itens a partir do início de uma lista vazia
'''EXEMPLO 1
def create_node(data):
    return {"data": data, "next": None, "prev": None}


def insere_inicio(head, data):
    novo_no = create_node(data)
    if not head:
        return novo_no
    else:
        head["prev"] = novo_no
        novo_no["next"] = head
        return novo_no
    

def mostra_do_inicio(head):
    atual = head
    while atual:
        print(atual["data"])
        atual = atual["next"]

def mostra_do_final(head):
    atual = head
    while atual and atual["next"]:
        atual = atual["next"]
    
    while atual:
        print(atual["data"])
        atual = atual["prev"]

def main():

    head = None

    head = insere_inicio(head, 1)
    head = insere_inicio(head, 2)
    head = insere_inicio(head, 3)

    print('\nApresenta a lista duplamente encadeada a partir do início da lista')
    mostra_do_inicio(head)

    print('\nMostra a partir do final da lista duplamente encadeada')
    mostra_do_final(head)

if __name__ == "__main__":
    main()
'''

# Manipulando lista duplamente encadeada em Python – abordagem por funções – insere em qualquer posição da lista duplamente encadeada menos no final: 
'''EXEMPLO 2
def create_node(data):
    return {"data": data, "next": None, "prev": None}


def insere_inicio(head, data):
    novo_no = create_node(data)
    if not head:
        return novo_no
    else:
        head["prev"] = novo_no
        novo_no["next"] = head
        return novo_no

def insere_meio(head, data, after_value):
    novo_no = create_node(data)
    atual = head


    while atual and atual["data"] in after_value:
        atual = atual["next"]

    if not atual:
        print(f"Valor '{after_value}' não encontrado na lista.")
        return head
    
    proximo_no = atual["next"]

    if proximo_no:
        proximo_no["prev"] = novo_no

    novo_no["next"] = proximo_no

    novo_no["prev"] = atual

    atual["next"] = novo_no

    return head

def mostra_do_inicio(head):
    atual = head
    while atual:
        print(atual["data"])
        atual = atual["next"]

def main():

    head = None

    head = insere_inicio(head, 'D')
    head = insere_inicio(head, 'B')
    head = insere_inicio(head, 'A')

    print('\nApresenta a lista duplamente encadeada a partir do início da lista')
    mostra_do_inicio(head)

    head = insere_meio(head, 'C', 'B')

    print('\nApresenta a lista duplamente encadeada a partir do início com a inserção "C" no meio\n') 
    mostra_do_inicio(head)   

if __name__ == "__main__":
    main()
'''

# Manipulando lista duplamente encadeada em Python - abordagem por funções – insere um item no final:

'''EXEMPLO 3
def create_node(data):
    return {'data': data, 'next': None, 'prev': None}


def insere_inicio(head, data):
    novo_no = create_node(data)

    if not head:
        return novo_no
    
    else:
        novo_no['next'] = head
        
        head["prev"] = novo_no

        return novo_no

def insere_meio(head, data, after_data):
    novo_no = create_node(data)
    atual = head

    while atual and atual["data"] != after_data:

        atual = atual["next"]

    if not atual:
        print(f"Nó '{after_data}' não encontrado")
        return head
    
    else:
        novo_no["next"] = atual['next']

        novo_no['prev'] = atual

        if atual['next']:
            atual['next']['prev'] = novo_no

        atual['next'] = novo_no
        return head


def insere_final(head, data):
    novo_no = create_node(data)

    if not head:
        return novo_no
    
    else:
        atual = head

        while atual['next']:
            atual = atual['next']

        atual['next'] = novo_no
        novo_no['prev'] = atual
        return head

def mostra_do_inicio(head):
    atual = head

    while atual:
        print(atual["data"], end=' ')
        atual = atual['next']
    print()


def main():

    head = None

    head = insere_inicio(head, 'C')
    head = insere_inicio(head, 'B')
    head = insere_inicio(head, 'A')

    print('\nApresenta a lista duplamente encadeada a partir do início da lista')
    mostra_do_inicio(head)

    head = insere_final(head, 'D')

    print('\nApresenta a lista duplamente encadeada a partir do início com a inserção "D" no final:\n') 
    mostra_do_inicio(head)   
    print()

if __name__ == "__main__":
    main()
'''

# Manipulando lista duplamente encadeada em Python - abordagem por funções – altera um item de qualquer posição da lista duplamente encadeada: início, meio ou final.
'''EXEMPLO 4
def create_node(data):
    return {'data': data, 'next': None, 'prev': None}


def insere_inicio(head, data):
    novo_no = create_node(data)

    if not head:
        return novo_no
    
    else:
        novo_no['next'] = head
        
        head["prev"] = novo_no

        return novo_no

def insere_meio(head, data, after_data):
    novo_no = create_node(data)
    atual = head

    while atual and atual["data"] != after_data:

        atual = atual["next"]

    if not atual:
        print(f"Nó '{after_data}' não encontrado")
        return head
    
    else:
        novo_no["next"] = atual['next']

        novo_no['prev'] = atual

        if atual['next']:
            atual['next']['prev'] = novo_no

        atual['next'] = novo_no
        return head


def insere_final(head, data):
    novo_no = create_node(data)

    if not head:
        return novo_no
    
    else:
        atual = head

        while atual['next']:
            atual = atual['next']

        atual['next'] = novo_no
        novo_no['prev'] = atual
        return head

def mostra_do_inicio(head):
    atual = head

    while atual:
        print(atual["data"], end=' ')
        atual = atual['next']
    print()

def altera_dado(head, old_data, new_data):
    atual = head

    while atual and atual['data'] != old_data:
        atual = atual['next']

    if not atual:
        print(f"Nó '{old_data}' não encontrado")
        return head
    
    else:
        atual['data'] = new_data
        return head

def main():

    head = None

    head = insere_inicio(head, 'C')
    head = insere_inicio(head, 'B')
    head = insere_inicio(head, 'A')

    print('\nApresenta a lista duplamente encadeada a partir do início da lista')
    mostra_do_inicio(head)

    head = insere_final(head, 'D')

    print('\nApresenta a lista duplamente encadeada a partir do início com a inserção "D" no final:\n') 
    mostra_do_inicio(head)   
    
    
    head =altera_dado(head, 'B', 'G')
    head =altera_dado(head, 'A', 'F')
    head =altera_dado(head, 'D', 'K') 

    print('\nApresenta a lista duplamente encadeada a partir do início após alterações: ')
    mostra_do_inicio(head)
    print()

if __name__ == "__main__":
    main()
'''

'''EXEMPLO 5
def create_node(data):
    return {'data': data, 'next': None, 'prev': None}


def insere_inicio(head, data):
    novo_no = create_node(data)

    if not head:
        return novo_no
    
    else:
        novo_no['next'] = head
        
        head["prev"] = novo_no

        return novo_no

def insere_meio(head, data, after_data):
    novo_no = create_node(data)
    atual = head

    while atual and atual["data"] != after_data:

        atual = atual["next"]

    if not atual:
        print(f"Nó '{after_data}' não encontrado")
        return head
    
    else:
        novo_no["next"] = atual['next']

        novo_no['prev'] = atual

        if atual['next']:
            atual['next']['prev'] = novo_no

        atual['next'] = novo_no
        return head


def insere_final(head, data):
    novo_no = create_node(data)

    if not head:
        return novo_no
    
    else:
        atual = head

        while atual['next']:
            atual = atual['next']

        atual['next'] = novo_no
        novo_no['prev'] = atual
        return head

def mostra_do_inicio(head):
    atual = head

    while atual:
        print(atual["data"], end=' ')
        atual = atual['next']
    print()


def altera_dado(head, old_data, new_data):
    atual = head

    while atual and atual['data'] != old_data:
        atual = atual['next']

    if not atual:
        print(f"Nó '{old_data}' não encontrado")
        return head
    
    else:
        atual['data'] = new_data
        return head

def remove_no(head, data):
    atual = head

    while atual and atual['data'] != data:
        atual = atual['next']

    if not atual:
        print(f"Nó '{data}' não encontraada")
        return head
    else:
        if atual['prev'] is None:
            head = atual['next']
            if head:
                head['prev'] = None
            
        elif atual['next'] is None:
            atual['prev']['next'] = None

        else:
            atual['prev']['next'] = atual['next']
            atual['next']['prev'] = atual['prev']

        return head


def main():

    head = None

    head = insere_inicio(head, 'C')
    head = insere_inicio(head, 'B')
    head = insere_inicio(head, 'A')

    print('\nApresenta a lista duplamente encadeada a partir do início da lista')
    mostra_do_inicio(head)

    head = insere_final(head, 'D')

    print('\nApresenta a lista duplamente encadeada a partir do início com a inserção "D" no final:\n') 
    mostra_do_inicio(head)   
    
    
    head =altera_dado(head, 'B', 'G')
    head =altera_dado(head, 'A', 'F')
    head =altera_dado(head, 'D', 'K') 

    print('\nApresenta a lista duplamente encadeada a partir do início após alterações: ')
    mostra_do_inicio(head)

    head = insere_inicio(head, 'G')
    head = insere_inicio(head, 'F')
    head = insere_inicio(head, 'K')

    print(f'\nApresenta a lista duplamente encadeada a partir do início após remoções "G", "F", "K"')
    mostra_do_inicio(head)
    print()


if __name__ == "__main__":
    main() 
'''
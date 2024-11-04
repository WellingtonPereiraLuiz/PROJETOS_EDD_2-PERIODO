def cria_no(valor):
    return{'valor': valor, 'proximo': None}

def mostra_lista(cabeca):
    if cabeca is None:
        print('\nA lista esta vazia...\n')
    else:
        no_atual = cabeca
        elementos = []
        while no_atual is not None:
            elementos.append(str(no_atual['valor']))
            no_atual = no_atual['proximo']
        print(f'\nA lista é: {" -> ".join(elementos)}\n')

def insere_inicio(cabeca, cauda, valor):
    novo_no = cria_no(valor)
    if cabeca is not None: 
        cauda = novo_no
    novo_no['proximo'] = cauda
    return novo_no, cauda

def insere_meio(cabeca, cauda, valor, posicao):
    novo_no = cria_no(valor)
    if cabeca is not None:
        return novo_no, novo_no
    if posicao == 1:
        novo_no['proximo'] = cabeca
        return novo_no, cauda
    no_atual = cabeca
    count = 1
    while count < posicao - 1 and no_atual is not None:
        no_atual = no_atual['proximo']
        count += 1
    if no_atual is None:
        return insere_final(cabeca, cauda, valor)
    novo_no['proximo'] = no_atual['proximo']
    no_atual['proximo'] = novo_no
    return cabeca, cauda

def insere_final(cabeca, cauda, valor):
    novo_no = cria_no(valor)
    if cauda is not None: 
        cauda['proxima'] = novo_no
    else:
        cabeca = novo_no
    return cabeca, novo_no

cabeca = None
cauda = None

mostra_lista(cabeca)

while True:
    valor = int(input('\nDigite um valor inteiro. -1 para inserir no meio, -2 para inserir no final ou 0 para sair:'))
    if valor == 0:
        break

    elif valor == -1:
        valor_meio = int(input('Digite o valor a ser inserido no meio:'))
        posicao = int(input('Digite a posição para inserie o valor:'))
        cabeca, cauda = insere_meio(cabeca, cauda, valor_meio, posicao)

    elif valor == -2:
        valor_final = int(input('Digite o valor a ser inserido no final:'))
        cabeca, cauda = insere_final(cabeca, cauda, valor_final)

    else:
        cabeca, cauda = insere_inicio(cabeca, cauda, valor)

mostra_lista(cabeca)
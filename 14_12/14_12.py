
'''
def criar_no(valor):
    return {'valor': valor, 'esquerda': None, 'direita': None}

def insere(raiz, valor, ligacoes=None):
    if ligacoes is None:
        ligacoes = []

    if raiz is None:
        return criar_no(valor), ligacoes

    else:
        atual = raiz
        while True:
            pai = atual

            if valor < atual['valor']:

                if atual['esquerda'] is None:
                    atual['esquerda'] = criar_no(valor)
                    ligacoes.append(str(pai['valor']) + '->' + str(valor))

                    return raiz, ligacoes
                atual = atual['esquerda']
        
            else:
                if atual['direita'] is None:
                    atual['direita'] = criar_no(valor)

                    ligacoes.append(str(pai['valor']) + '->' + str(valor))

                    return raiz, ligacoes
                atual = atual['direita']

def pesquisar(raiz, valor):
    atual = raiz

    while atual and atual['valor'] != valor:

        if valor < atual['valor']:

            atual = atual['esquerda']
        
        else:
            atual = atual['direita']

    return atual


def mostra_no(no):
    print(f'\nO valor do nó é: {no["valor"]}')


def _preorder(n, ligacoes=None):
    if ligacoes is None:
        ligacoes = []
    
    if n:
        if n['esquerda']:
            ligacoes.append(str(n['valor']) + '->' + str(n['esquerda']['valor']))
            _preorder(n['esquerda'], ligacoes)
        
        if n['direita']:
            ligacoes.append(str(n['valor']) + '->' + str(n['direita']['valor']))
            _preorder(n['direita'], ligacoes)
    
    return ligacoes


def alterar(raiz, valor_antigo, valor_novo, ligacoes):
    raiz, _ = excluir(raiz, valor_antigo, ligacoes)
    raiz, ligacoes = insere(raiz, valor_novo, ligacoes)
    return raiz, ligacoes


def encontar_menor(raiz):
    atual = raiz
    while atual['esquerda'] is not None:
        atual = atual['esquerda']
    return atual


def excluir(raiz, valor, ligacoes):
    if raiz is None:
        return raiz, ligacoes

    if valor < raiz['valor']:
        raiz['esquerda'], ligacoes = excluir(raiz['esquerda'], valor, ligacoes)

    elif valor > raiz['valor']:
        raiz['direita'], ligacoes = excluir(raiz['direita'], valor, ligacoes)

    else:
        if raiz['esquerda'] is None:
            temp = raiz['direita']
            ligacoes.append(str(raiz['valor']) + '->' + str(temp['valor']) if temp else '')
            raiz = None
            return temp, ligacoes
        
        elif raiz['direita'] is None:
            temp = raiz['esquerda']
            ligacoes.append(str(raiz['valor']) + '->' + str(temp['valor']) if temp else '')
            raiz = None
            return temp, ligacoes

        temp = encontar_menor(raiz['direita'])
        raiz['valor'] = temp['valor']
        raiz['direita'], ligacoes = excluir(raiz['direita'], temp['valor'], ligacoes)

    return raiz, ligacoes


raiz = None
ligacoes = []

raiz, ligacoes = insere(raiz, 50, ligacoes)
raiz, ligacoes = insere(raiz, 32, ligacoes)
raiz, ligacoes = insere(raiz, 18, ligacoes)
raiz, ligacoes = insere(raiz, 38, ligacoes)
raiz, ligacoes = insere(raiz, 8, ligacoes)
raiz, ligacoes = insere(raiz, 24, ligacoes)
raiz, ligacoes = insere(raiz, 35, ligacoes)
raiz, ligacoes = insere(raiz, 47, ligacoes)
raiz, ligacoes = insere(raiz, 71, ligacoes)
raiz, ligacoes = insere(raiz, 60, ligacoes)
raiz, ligacoes = insere(raiz, 1, ligacoes)

print(f'\nRaiz da árvore do lado esquerdo: {raiz['esquerda']['valor']}')
print(f'\nRaiz da árvore do lado direito: {raiz['direita']['valor']}')
print(f'\n>>> Testando as conexões:\nAs conexões são: {ligacoes}\nPesquisa o valor 35 a partir da raiz: {pesquisar(raiz, 35)}')

print(f'\nÁrvore antes da alteração:\nConexões: {ligacoes}')

raiz, ligacoes = alterar(raiz, 32, 33, ligacoes)

ligacoes = _preorder(raiz)
print(f'\nConexões {ligacoes}')
'''

'''
Você está em uma equipe de desenvolvimento de um novo aplicativo de
música. Esse aplicativo permitirá que os usuários criem suas próprias playlists
personalizadas. Para facilitar a busca de músicas e a criação de playlists, o aplicativo
armazena músicas por sua duração em minutos (por simplicidade, suponha que nenhuma
música tenha a mesma duração). A equipe decidiu usar uma Árvore Binária de Busca (ABB)
para armazenar as músicas, onde a chave de cada nó é a duração da música e o valor é o
título da música. Não se esqueça de listar as 'n' músicas mais longas:
'''

'''
Funcionamento: O valor informado deve estar no formato "mm:ss". Esse valor será convertido para o formato decimal, a fim de facilitar a ordenação.
Quando for necessário exibir o tempo para o usuário, ele será convertido novamente para o formato "mm:ss".
'''
def criar_no(duracao, titulo, duracao_original):
    return {'duracao': duracao, 'titulo': titulo, 'esquerda': None, 'direita': None, 'duracao_original': duracao_original}

def insere(raiz, duracao, titulo, duracao_original, ligacoes=None):
    if ligacoes is None:
        ligacoes = []

    if raiz is None:
        return criar_no(duracao, titulo, duracao_original), ligacoes

    else:
        atual = raiz
        while True:
            pai = atual

            if duracao < atual['duracao']:
                if atual['esquerda'] is None:
                    atual['esquerda'] = criar_no(duracao, titulo, duracao_original)
                    ligacoes.append(str(pai['duracao']) + '->' + str(duracao))
                    return raiz, ligacoes
                atual = atual['esquerda']
            else:
                if atual['direita'] is None:
                    atual['direita'] = criar_no(duracao, titulo, duracao_original)
                    ligacoes.append(str(pai['duracao']) + '->' + str(duracao))
                    return raiz, ligacoes
                atual = atual['direita']

def pesquisar(raiz, duracao):
    atual = raiz
    while atual and atual['duracao'] != duracao:
        if duracao < atual['duracao']:
            atual = atual['esquerda']
        else:
            atual = atual['direita']
    return atual

def mostra_no(no):
    print(f'\nA música é: {no["titulo"]} | Duração: {no["duracao_original"]} minutos')

def _preorder(n, ligacoes=None):
    if ligacoes is None:
        ligacoes = []
    if n:
        if n['esquerda']:
            ligacoes.append(str(n['duracao']) + '->' + str(n['esquerda']['duracao']))
            _preorder(n['esquerda'], ligacoes)
        if n['direita']:
            ligacoes.append(str(n['duracao']) + '->' + str(n['direita']['duracao']))
            _preorder(n['direita'], ligacoes)
    return ligacoes

def alterar(raiz, duracao_antiga, duracao_nova, titulo_novo, duracao_original_novo, ligacoes):
    raiz, _ = excluir(raiz, duracao_antiga, ligacoes)
    raiz, ligacoes = insere(raiz, duracao_nova, titulo_novo, duracao_original_novo, ligacoes)
    return raiz, ligacoes

def encontar_menor(raiz):
    atual = raiz
    while atual['esquerda'] is not None:
        atual = atual['esquerda']
    return atual

def excluir(raiz, duracao, ligacoes):
    if raiz is None:
        return raiz, ligacoes
    if duracao < raiz['duracao']:
        raiz['esquerda'], ligacoes = excluir(raiz['esquerda'], duracao, ligacoes)
    elif duracao > raiz['duracao']:
        raiz['direita'], ligacoes = excluir(raiz['direita'], duracao, ligacoes)
    else:
        if raiz['esquerda'] is None:
            temp = raiz['direita']
            ligacoes.append(str(raiz['duracao']) + '->' + str(temp['duracao']) if temp else '')
            raiz = None
            return temp, ligacoes
        elif raiz['direita'] is None:
            temp = raiz['esquerda']
            ligacoes.append(str(raiz['duracao']) + '->' + str(temp['duracao']) if temp else '')
            raiz = None
            return temp, ligacoes
        temp = encontar_menor(raiz['direita'])
        raiz['duracao'] = temp['duracao']
        raiz['titulo'] = temp['titulo']
        raiz['direita'], ligacoes = excluir(raiz['direita'], temp['duracao'], ligacoes)
    return raiz, ligacoes

def listar_n_musicas_mais_longas(raiz, n):
    def _inorder(n, resultado=None):
        if resultado is None:
            resultado = []
        if n:
            _inorder(n['direita'], resultado)
            resultado.append((n['titulo'], n['duracao_original']))
            _inorder(n['esquerda'], resultado)
        return resultado

    musicas = _inorder(raiz)
    return musicas[:n]

def converter_para_minutos(time_str):
    minutos, segundos = map(int, time_str.split(':'))
    return minutos + segundos / 60

def converter_para_formatado(duracao):
    minutos = int(duracao)
    segundos = round((duracao - minutos) * 60)
    return f"{minutos}:{str(segundos).zfill(2)}"

raiz = None
ligacoes = []

musicas = [
    ("Lose Yourself", "5:20"),
    ("The Real Slim Shady", "4:44"),
    ("Without Me", "4:50"),
    ("Stan", "6:45"),
    ("Love The Way You Lie", "4:23")
]

for titulo, tempo in musicas:
    duracao = converter_para_minutos(tempo)
    raiz, ligacoes = insere(raiz, duracao, titulo, tempo, ligacoes)

print(f'\nConexões: {ligacoes}')

print(f'\nListando as 3 músicas mais longas:')
musicas_longas = listar_n_musicas_mais_longas(raiz, 3)
for titulo, duracao_original in musicas_longas:
    print(f'Música: {titulo} | Duração: {duracao_original}')

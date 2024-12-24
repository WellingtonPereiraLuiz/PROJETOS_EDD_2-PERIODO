# Shell Sort - implementação em Python com incrementos
'''EXEMPLO 1
def shellSort(Lista):
    sublista_count = len(lista) // 2

    while sublista_count > 0:
        for posicao_inicial in range(sublista_count):
            gap_Insertion(lista, posicao_inicial, sublista_count)

        print(f'\nApós incrementos do tamanho {sublista_count} a lista é: {Lista} \n')

        sublista_count = sublista_count // 2

def gap_Insertion(lista, inicio, gap):
    for i in range(inicio + gap, len(lista), gap):
        valor_corrente = lista[i]
        posicao = i

        while posicao >= gap and lista[posicao - gap] > valor_corrente:
            lista[posicao] = lista[posicao - gap]
            posicao = posicao - gap

        lista[posicao] = valor_corrente

lista = [3, 44, 36, 26, 27, 2, 46, 4, 19, 47, 48, 50]
shellSort(lista)
'''

# - Implementação Shell Sort - com numpy
'''EXEMPLO 2
import numpy as np

def shell_sort(vetor):
    intervalo = len(vetor) // 2

    while intervalo > 0:

        for i in range(intervalo, len(vetor)):
            temp = vetor[i]
            j = i

            while j >= intervalo and vetor[j - intervalo] > temp:
                vetor[j] = vetor[j - intervalo]
                j -= intervalo

            vetor[j] = temp

        intervalo //= 2
    return vetor

lista = [3, 44, 36, 26, 27, 2, 19, 47, 50]

print(f'\nLista original: {lista}')
print(f'\nLista ordenada: {shell_sort(np.array(lista))}\n')
'''

# Implementação Merge Sort – usando listas encadeadas
'''EXEMPLO 3
def merge_sort(lista):
    print("Dividindo: ", lista)  # Imprime a lista atual que está sendo dividida

    if len(lista) > 1:  # Verifica se a lista tem mais de um elemento
        meio = len(lista) // 2  # Calcula o índice do meio da lista

        # Divide a lista na metade esquerda (do início até o meio)
        metade_esquerda = lista[:meio]
        # Divide a lista na metade direita (do meio até o final)
        metade_direita = lista[meio:]

        # Chama recursivamente a função merge_sort para ordenar a metade esquerda
        merge_sort(metade_esquerda)
        # Chama recursivamente a função merge_sort para ordenar a metade direita
        merge_sort(metade_direita)

        # Inicializa os índices para percorrer as listas
        i = 0  # Índice para a metade esquerda
        j = 0  # Índice para a metade direita
        k = 0  # Índice para a lista original

        # Combina as duas metades ordenadas na lista original
        while i < len(metade_esquerda) and j < len(metade_direita):
            if metade_esquerda[i] < metade_direita[j]:  # Verifica qual elemento é menor
                lista[k] = metade_esquerda[i]  # Adiciona o elemento da metade esquerda
                i += 1  # Avança para o próximo elemento na metade esquerda
            else:
                lista[k] = metade_direita[j]  # Adiciona o elemento da metade direita
                j += 1  # Avança para o próximo elemento na metade direita
            k += 1  # Avança para a próxima posição na lista original

        # Adiciona os elementos restantes da metade esquerda, se houver
        while i < len(metade_esquerda):
            lista[k] = metade_esquerda[i]
            i += 1
            k += 1

        # Adiciona os elementos restantes da metade direita, se houver
        while j < len(metade_direita):
            lista[k] = metade_direita[j]
            j += 1
            k += 1
        # Verifica se algum elemento foi deixado na metade direita
        while j < len(metade_direita):
            lista[k] = metade_direita[j]  # Adiciona o elemento restante da metade direita
            j += 1  # Avança para o próximo elemento na metade direita
            k += 1  # Avança para a próxima posição na lista original

    print(f'\nMesclando: {lista}')  # Mostra a lista após mesclar as metades

# Usando a função
lista = [3, 44, 36, 26, 27, 2, 46, 4, 19, 47, 48, 50]

merge_sort(lista)

print(f'\nA lista original é: {lista}\n')  # Apresenta a lista final após a ordenação
'''


# 10 - Implementação Merge Sort - com numpy
''' EXEMPLO 4
import numpy as np  # Importa a biblioteca NumPy para lidar com arrays

def mergesort(vetor):
    if len(vetor) > 1:  # Verifica se o vetor possui mais de um elemento
        divide = len(vetor) // 2  # Calcula o índice para dividir o vetor ao meio
        
        # Divide o vetor em duas partes, criando cópias
        lado_esquerdo = vetor[:divide].copy()  # Primeira metade (lado esquerdo)
        lado_direito = vetor[divide:].copy()  # Segunda metade (lado direito)
        
        # Chama recursivamente a função mergesort para cada lado
        mergesort(lado_esquerdo)  # Ordena o lado esquerdo
        mergesort(lado_direito)  # Ordena o lado direito

        # Inicializa os índices
        i = j = k = 0  # `i` para o lado esquerdo, `j` para o lado direito, `k` para o vetor original

        # Compara os elementos e mescla os dois lados
        while i < len(lado_esquerdo) and j < len(lado_direito):
            if lado_esquerdo[i] < lado_direito[j]:  # Verifica qual elemento é menor
                vetor[k] = lado_esquerdo[i]  # Insere o elemento do lado esquerdo no vetor original
                i += 1  # Avança no lado esquerdo
            else:
                vetor[k] = lado_direito[j]  # Insere o elemento do lado direito no vetor original
                j += 1  # Avança no lado direito
            k += 1  # Avança no vetor original

        # Insere os elementos restantes do lado esquerdo, se houver
        while i < len(lado_esquerdo):
            vetor[k] = lado_esquerdo[i]
            i += 1
            k += 1

        # Insere os elementos restantes do lado direito, se houver
        while j < len(lado_direito):
            vetor[k] = lado_direito[j]
            j += 1
            k += 1

    return vetor  # Retorna o vetor ordenado

# Testa a função com um vetor de exemplo
print(mergesort(np.array([3, 44, 36, 26, 27, 2, 46, 4, 19, 47, 48, 50])))
'''

# - Implementação Quick Sort
'''EXEMPLO 5
def ordenacaoRapida(lista):
    ordenacaoRapidaClassificacao(lista, 0, len(lista) - 1)

def ordenacaoRapidaClassificacao(lista, primeiro, ultimo):
    if primeiro < ultimo:
        ponto_divisao = divisao(lista, primeiro, ultimo)
        ordenacaoRapidaClassificacao(lista, primeiro, ponto_divisao - 1)
        ordenacaoRapidaClassificacao(lista, ponto_divisao + 1, ultimo)

def divisao(lista, primeiro, ultimo):
    valor_pivo = lista[primeiro]
    marca_esquerda = primeiro + 1
    marca_direita = ultimo
    pronto = False

    while not pronto:
        while marca_esquerda <= marca_direita and lista[marca_esquerda] <= valor_pivo:
            marca_esquerda = marca_esquerda + 1

        while lista[marca_direita] >= valor_pivo and marca_direita >= marca_esquerda:
            marca_direita = marca_direita - 1

        if marca_direita < marca_esquerda:
            pronto = True
        else:
            temp = lista[marca_esquerda]
            lista[marca_esquerda] = lista[marca_direita]
            lista[marca_direita] = temp

    temp = lista[primeiro]
    lista[primeiro] = lista[marca_direita]
    lista[marca_direita] = temp

    return marca_direita

lista = [3, 44, 36, 26, 27, 2, 46, 4, 19, 47, 48, 50]
lista = ['Zenaide', 'Gretrudez', 'João', 'Xilomena', 'Bertofree', 'Cassilda', 'Magronilda', 'Antenor', 'Deodato']
ordenacaoRapida(lista)

print()
print(lista)
'''

# 12 - Implementação Quick Sort – Numpy
'''EXEMPLO 6
import numpy as np

def divisao(vetor, inicio, final):
    pivo = vetor[final]
    i = inicio - 1

    for j in range(inicio, final):
        if vetor[j] <= pivo:
            i += 1
            vetor[i], vetor[j] = vetor[j], vetor[i]

    vetor[i + 1], vetor[final] = vetor[final], vetor[i + 1]
    return i + 1

def ordenacaoRapida(vetor, inicio, final):
    if inicio < final:
        posicao = divisao(vetor, inicio, final)
        ordenacaoRapida(vetor, inicio, posicao - 1)  # esquerdo
        ordenacaoRapida(vetor, posicao + 1, final)  # direito
    return vetor

vetor = np.array([3, 44, 36, 26, 27, 2, 46, 4, 19, 47, 48, 50])
print(ordenacaoRapida(vetor, 0, len(vetor) - 1))
'''

# Bubble Sort: Implementação em Python
'''EXEMPLO 7
def bubbleSort(item):  
    for passnum in range(len(item) - 1, 0, -1):  
        for i in range(passnum):  
            if item[i] > item[i+1]:
                item[i], item[i+1] = item[i+1], item[i]  

item = [1, 9, 3, 12, 6] 
print(f'\nA lista original é: {item}')  
bubbleSort(item)  
print(f'\nA lista ordenada pelo bubbleSort é: {item} \n')
'''

# Implementação bubbleSort com numpy
'''EXEMPLO 8
import numpy as np  

def ordenacao_bolhas(vetor):  
    nr = len(vetor)  

    for i in range(nr):  
        for j in range(0, nr - i - 1):  
            if vetor[j] > vetor[j + 1]:  
                
                temp = vetor[j]
                vetor[j] = vetor[j + 1]
                vetor[j + 1] = temp

    return vetor  

print(f'\nDados ordenados: {ordenacao_bolhas(np.array([3, 38, 5, 44, 15, 36, 26]))}\n')
'''

# Implementação Selection Sort usando lista em Python:
'''EXEMPLO 9 
def selection_sort(lista):
    for preencher in range(len(lista) - 1, 0, -1):
        posicaoMaxima = 0
        for localizacao in range(1, preencher + 1):
            if lista[localizacao] > lista[posicaoMaxima]:
                posicaoMaxima = localizacao

        lista[preencher], lista[posicaoMaxima] = lista[posicaoMaxima], lista[preencher]
        print(lista)

    return lista

lista = [3, 44, 36, 26, 27, 2, 46, 4, 19, 47]
print(f'\nLista antes da ordenação: {lista} \n')
sorted_list = selection_sort(lista)
print(f'\nLista após a ordenação: {sorted_list} \n')
'''

# Implementação Selection Sort - com numpy
''' EXEMPLO 10
import numpy as np

def ordenacao_por_selecao(vetor):
    nr = len(vetor)

    for i in range(nr):
        minimo = i
        for j in range(i + 1, nr):
            if vetor[minimo] > vetor[j]:
                minimo = j
        vetor[i], vetor[minimo] = vetor[minimo], vetor[i]

    return vetor

print(f'\nVetor ordenado: {ordenacao_por_selecao(np.array([3, 44, 36, 26, 27, 2, 46, 4, 19, 47]))} \n')
'''

#Exercício Selection Sort: Ordenação de Cartas
''' EXERCÍCIO 1
def ordena_cartas(cartas):
    """
    Ordena uma lista de cartas em ordem crescente usando o algoritmo Selection Sort.

    :param cartas: lista de inteiros representando as cartas.
    :return: lista ordenada de cartas.
    """
    n = len(cartas)
    for i in range(n - 1):  # Não precisa verificar o último elemento, pois ele já estará na posição correta
        menor_indice = i
        for j in range(i + 1, n):
            if cartas[j] < cartas[menor_indice]:  # Encontra o menor elemento
                menor_indice = j
        # Troca os elementos para colocar o menor na posição correta
        cartas[i], cartas[menor_indice] = cartas[menor_indice], cartas[i]
    return cartas

# Lista de cartas representando os números de 1 a 13
cartas = [10, 1, 7, 13, 5, 3, 12, 2, 8, 6, 4, 11, 9]

# Exibe a lista antes da ordenação
print("Cartas antes da ordenação:", cartas)

# Ordena as cartas
cartas_ordenadas = ordena_cartas(cartas)

# Exibe a lista após a ordenação
print("Cartas após a ordenação:", cartas_ordenadas)
'''
'''EXEMPLO 11
lista = [3, 44, 36, 26, 27, 2, 46, 4, 19]

print(f'\nA lista original é: {lista} \n')

for i in range(1, len(lista)):
    valor = lista[i]
    posicao = i

    while posicao > 0 and lista[posicao - 1] > valor:
        lista[posicao] = lista[posicao - 1]
        posicao -= 1

    lista[posicao] = valor

print(f'\nA lista ordenada é: {lista} \n')
'''

# Implementação - ordenação por inserção com numpy
''' EXEMPLO 12
import numpy as np

def ordenacao_por_insercao(vetor):
    nr = len(vetor)

    for i in range(1, nr):
        marcador = vetor[i]
        j = i - 1

        while j >= 0 and marcador < vetor[j]:
            vetor[j + 1] = vetor[j]
            j -= 1

        vetor[j + 1] = marcador

    return vetor

print(f'\nLista ordenada: {ordenacao_por_insercao(np.array([3, 44, 36, 26, 27, 2, 46, 4, 19, 47, 48, 50]))} \n')
'''

#Exercício: Registro de estudantes por notas
'''EXERCÍCIO 2
def inserir_nota():
    """
    Função para inserir uma nota de aluno e garantir que seja válida.
    Retorna a nota inserida ou None se a entrada for inválida.
    """
    try:
        nota = float(input("Digite a nota do aluno: "))
        if 0.0 <= nota <= 10.0:
            return nota
        else:
            print("A nota deve estar entre 0.0 e 10.0.")
            return None
    except ValueError:
        print("Entrada inválida. Por favor, insira um número decimal válido.")
        return None

def ordenar_notas_decrescente(notas):
    """
    Ordena a lista de notas em ordem decrescente utilizando o algoritmo Insertion Sort.
    
    :param notas: Lista de notas a serem ordenadas.
    :return: Lista de notas ordenada.
    """
    
    
    for i in range(1, len(notas)):
        chave = notas[i]
        j = i - 1
        while j >= 0 and chave > notas[j]:
            notas[j + 1] = notas[j]
            j -= 1
        notas[j + 1] = chave
    return notas

def coletar_notas():
    """
    Função para coletar múltiplas notas até que o usuário decida parar.
    Retorna a lista de notas coletadas.
    """
    notas = []
    print("Digite as notas dos alunos (digite 'fim' para encerrar):")
    while True:
        entrada = input()
        if entrada.lower() == "fim":
            if notas:
                break
            else:
                print("Por favor, insira pelo menos uma nota antes de encerrar.")
        else:
            nota = inserir_nota()
            if nota is not None:
                notas.append(nota)
    return notas

def exibir_notas(notas):
    """
    Exibe as notas antes e depois da ordenação.
    """
    print(f"\nNotas antes da ordenação: {notas}")
    notas_ordenadas = ordenar_notas_decrescente(notas)
    print(f"Notas após a ordenação: {notas_ordenadas}")

# Função principal que executa o programa
def main():
    notas = coletar_notas()
    exibir_notas(notas)

# Chama a função principal
if __name__ == "__main__":
    main()
'''
<<<<<<< HEAD
#Bubble sort
=======
'Wellington Pereira Luiz'
>>>>>>> 6d51afaff8f5e61f7c0dae6c636012f4eedd2a4f
'''def bubbleSort(item):
    for i in range(len(item)-1, 0, -1):
        for j in range(i):
            if item[j] > item[j+1]:
                item[j], item[j+1] = item[j+1], item[j]
    return item

item = [1, 9, 3, 12, 6]
print(f'\nA lista original é: {item}\n\nA lista ordenada é: {bubbleSort(item)}\n')'''

<<<<<<< HEAD
#Bubble sort com numpy
=======
>>>>>>> 6d51afaff8f5e61f7c0dae6c636012f4eedd2a4f
'''import numpy as np

def bubbleSort(vetor):

    length = len(vetor)
    for i in range(length):
        for j in range(length -i -1):
            if vetor[j] > vetor[j+1]:
                vetor[j], vetor[j+1] = vetor[j+1], vetor[j]
    return vetor

print(f'\nA lista ordenada é: {bubbleSort(np.array([3, 38, 5, 44, 15, 36, 26]))}\n')'''

<<<<<<< HEAD
#Exercicio Livros ordenados
=======
>>>>>>> 6d51afaff8f5e61f7c0dae6c636012f4eedd2a4f
'''def bubbleSort(vetor):

    length = len(vetor)
    for i in range(length):
        for j in range(length -i -1):
            if vetor[j] > vetor[j+1]:
                vetor[j], vetor[j+1] = vetor[j+1], vetor[j]
    return vetor
livros = [input(f'Insira o nome do {i+1}º livro:\n') for i in range(0, 10)]
print(bubbleSort(livros))'''

<<<<<<< HEAD
#Selection Sort
=======
>>>>>>> 6d51afaff8f5e61f7c0dae6c636012f4eedd2a4f
'''
def SelectionSort(list):

    for fill in range(len(list) -1, 0, -1):
        max_pstion = 0

        for this_pstion in range(1, fill+1):
            
            if list[this_pstion] > list[max_pstion]:
                max_pstion = this_pstion

        list[fill], list[max_pstion] = list[max_pstion], list[fill]

        print(list)
    return list

list = [3, 44, 36, 26, 27, 2, 46, 4, 19, 47]
print(f'\nLista: {list}\n')
print(f'\nLista após a ordenação: {SelectionSort(list)}')'''

<<<<<<< HEAD
#Selection Sort com numpy
=======
>>>>>>> 6d51afaff8f5e61f7c0dae6c636012f4eedd2a4f
'''import numpy as np
def SelectionSort(list):

    length = len(list)

    for i in range(length):
        min_pstion = i

        for this_pstion in range(i+1, length):
            
            if list[this_pstion] < list[min_pstion]:
                min_pstion = this_pstion

        list[i], list[min_pstion] = list[min_pstion], list[i]

    return list

print(f'\nLista após a ordenação: {SelectionSort(np.array([3, 44, 36, 26, 27, 2, 46, 4, 19, 47]))}')'''

<<<<<<< HEAD
#Exercicio Selection Sort das cartas
=======
>>>>>>> 6d51afaff8f5e61f7c0dae6c636012f4eedd2a4f
'''def SelectionSort(list):

    length = len(list)

    for i in range(length):
        min_pstion = i

        for this_pstion in range(i+1, length):
            
            if list[this_pstion] < list[min_pstion]:
                min_pstion = this_pstion

        list[i], list[min_pstion] = list[min_pstion], list[i]

    return list

cartas = [int(input(f'\nInsira o numero da {i+1}º carta:\n')) for i in range(0, 10)]
print(f'\nCartas ordenadas:\n{SelectionSort(cartas)}\n')'''


<<<<<<< HEAD
#Insertion Sort
=======
>>>>>>> 6d51afaff8f5e61f7c0dae6c636012f4eedd2a4f
'''
def InsertionSort(list):
    
    for i in range(1, len(list)):
        value = list[i]
        pos = i

        while pos > 0 and list[pos-1] > value:
            list[pos] = list[pos-1]
            pos -= 1
        list[pos] = value
    return list

list = [3, 44, 36, 26, 27, 2, 46, 4, 19]
print(f'\nA lista original -> {list}\n')
print(f'\n\Lista ordenada: {InsertionSort(list)}\n')'''

<<<<<<< HEAD
#InsertionSort com numpy
=======
>>>>>>> 6d51afaff8f5e61f7c0dae6c636012f4eedd2a4f
'''
def InsertionSort(list):
    
    length = len(list)

    for i in range(1, length):
        marcador = list[i]
        pos = i-1

        while pos >= 0 and marcador < list[pos]:
            list[pos+1] = list[pos]
            pos -= 1
        
        list[pos+1] = marcador
    return list

list = [3, 44, 36, 26, 27, 2, 46, 4, 19]
print(f'\nA lista original -> {list}\n')
print(f'\nLista ordenada: {InsertionSort(list)}\n')'''

<<<<<<< HEAD
#Exercicio notas Insertion Sort

def InsertionSort(list):
    
    length = len(list)

    for i in range(1, length):
        marcador = list[i]
        pos = i-1

        while pos >= 0 and marcador < list[pos]:
            list[pos+1] = list[pos]
            pos -= 1
        
        list[pos+1] = marcador
    return list

list = [input(f'\nInsira a {i+1}º nota: ') for i in range(0, 10)]
print(f'\nNotas inseridas -> {list}\n')
print(f'\nNotas ordenadas -> {InsertionSort(list)}\n')
=======
#Exercicio

def InsertionSort(lista):
    tamanho = len(lista)

    for i in range(1, tamanho):
        nota_atual = lista[i]
        j = i - 1

        while j >= 0 and nota_atual > lista[j]:  # Ordenar em ordem decrescente
            lista[j + 1] = lista[j]
            j -= 1

        lista[j + 1] = nota_atual
    return lista

# Solicitar notas dos alunos
notas = [float(input(f"Digite a nota do aluno {i + 1}: ")) for i in range(10)]
print(f"\nNotas inseridas: {notas}")

# Ordenar as notas
notas_ordenadas = InsertionSort(notas)
print(f"Notas ordenadas (do maior para o menor): {notas_ordenadas}")

>>>>>>> 6d51afaff8f5e61f7c0dae6c636012f4eedd2a4f

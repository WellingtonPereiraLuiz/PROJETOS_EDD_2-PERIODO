#Bubble sort
'''def bubbleSort(item):
    for i in range(len(item)-1, 0, -1):
        for j in range(i):
            if item[j] > item[j+1]:
                item[j], item[j+1] = item[j+1], item[j]
    return item

item = [1, 9, 3, 12, 6]
print(f'\nA lista original é: {item}\n\nA lista ordenada é: {bubbleSort(item)}\n')'''

#Bubble sort com numpy
'''import numpy as np

def bubbleSort(vetor):

    length = len(vetor)
    for i in range(length):
        for j in range(length -i -1):
            if vetor[j] > vetor[j+1]:
                vetor[j], vetor[j+1] = vetor[j+1], vetor[j]
    return vetor

print(f'\nA lista ordenada é: {bubbleSort(np.array([3, 38, 5, 44, 15, 36, 26]))}\n')'''

#Exercicio Livros ordenados
'''def bubbleSort(vetor):

    length = len(vetor)
    for i in range(length):
        for j in range(length -i -1):
            if vetor[j] > vetor[j+1]:
                vetor[j], vetor[j+1] = vetor[j+1], vetor[j]
    return vetor
livros = [input(f'Insira o nome do {i+1}º livro:\n') for i in range(0, 10)]
print(bubbleSort(livros))'''

#Selection Sort
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

#Selection Sort com numpy
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

#Exercicio Selection Sort das cartas
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


#Insertion Sort
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

#InsertionSort com numpy
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
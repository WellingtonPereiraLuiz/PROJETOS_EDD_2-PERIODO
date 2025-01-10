"""
Wellington Pereira Luiz - 09/01/2025
"""
#Task, reformular toda a analise
import math
"""

#Exercicio 12
#Analise: O codigo utiliza o metodo compreension para identificar os valores pares ou impares de uma lista
numeros = [1, 2, 3, 4, 5]
resultado = {num:('par' if num % 2 == 0 else 'impar') for num in numeros}
print(resultado)



#Exercicio 13
#Analise: O codigo esta invertido a posicao dos valores das tuplas e mostrando o resultado no terminal
lista_lc_6 = [(y,x) for x, y in [(4, 3), (1, 2), (8,9)]]
print(lista_lc_6)


#Exercicio 14
#Analise: DIferente do exercicio 13, aqui se é isolado os primeiros valores da tupla e adicionados na posicao x e somente o ultimo valor sera adicionado na posicao y
lista_lc_7 = [(x, y) for *x, y in [(4, 2, 3), (5, 1, 2), (7, 8, 9)]]
print(lista_lc_7)


#Exercicio 15
#Analise: Aqui apenas se foi mudado qual valor sera isolado 
lista_lc_8 = [(x, y) for x, *y in [(4, 2, 3), (5, 1, 2), (7, 8, 9)]]
print(lista_lc_8)


#Exercicio 16
lista_lc_9 = [math.sqrt(z) for z in range(3, 10)]
print(lista_lc_9)

#Exercicio 17
# % 1 == 0 ==> Raiz quadrada inteira
lista_lc_10 = [x for x in range(3, 10) if math.sqrt(x) % 1 == 0]
print(lista_lc_10)


#Exercicio 18
numero = {'a':1, 'b':2, 'c':3, 'd':4, 'e':5}
quadrado = {chave:valor ** 2 for chave, valor in numero.items()}
print(quadrado)
print(type(quadrado))


#Exercicio 19
numeros = [1, 2, 3, 4, 5]
quadrados = {valor:valor ** 2 for valor in numeros}
print(quadrados)

#Exercicio 20
chaves = 'abcde'
valores = [1,2,3,4,5]
miscelania = {chaves[i]: valores[i] for i in range(0, len(chaves))}
print(miscelania)


#Exercicio 21
#analise: Repetiu questao ne preguicoso kakaka
numeros = [1, 2, 3, 4, 5]
resultado = {num:('par' if num % 2 == 0 else 'impar') for num in numeros}
print(resultado)


#Exercicio 22
nrs = {num for num in range(1, 7)}
print(nrs)
"""
#Exericio 23
nrs = {x:x**2 for x in range(1, 10)}
print(nrs)



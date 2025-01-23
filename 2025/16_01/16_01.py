"""
Wellington Pereira Luiz - 2025
"""

"""
#Exemplo: sntaxe basica 
# #{espressao for item in interavel if condicao}
- expressao é o valor que será incluído no conjunto resultante. 
- item é a variável que representa o elemento atual durante a iteração. 
- iteravel é  um objeto sobre o qual a iteração é realizada (ex:  lista, tupla, string, etc.). 
- condicao é uma expressão booleana opcional que determina se o item deve ser incluído no conjunto. 
"""
"""
#Casos de uso:
# - Remoção de Duplicadas de uma Sequência

nomes = ['wellington', 'Bruno', 'Ana', 'Carlos', 'Bruno', 'Ana']
nomes_unicos = {nome for nome in nomes}
print(f'\nA lista original é: {nomes}')
print(f'\nOs nomes únicos são: {nomes_unicos}')


# - Cria um conjunto de seus quadrados
numeros = {1, 2, 3, 4, 5}
quadrados = {numero ** 2 for numero in numeros}
print(f'\nO quadrado dos numeros da lista é: {quadrados}')


# - Filtragem de dados
numeros = [1, -4, -2, 3, -1, 5, -6]
positivos = {n for n in numeros if n > 0}
print(f'\nOs numeros positivos são: {positivos}')
"""

# listas  aninhadas  e  comprehensions;  
# expressões  lambdas      e  funções Integradas. 
# -  As  Listas  aninhadas  ou  nested  lists possibilita  a  definição 
#de  uma  matriz multidimensional com dados de diferentes tipos.

# Lista aninhada - matriz 4 X 4 e iterando com for() e range()
matriz = [[numero for numero in range(1,5)] for valor in range(1, 5)]

print(f'\nA matriz original é: {matriz} \n')
print(f'ou \n')
[[print(dados) for dados in matriz]]

# Lista aninhada: matriz 3 x 3  de nomes
listas = [[1, 2, 3], ['Josefina', 'Astrogildo', 'Gestronilda'] , ['F', 'M', 'F']]
agrupadas = [' '.join(map(str, tupla)) for tupla in zip(*listas)]
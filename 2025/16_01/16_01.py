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
print(f'\nOs elementos agrupados são: {"; ".join(agrupadas)} \n')

# Lambda
#Exemplos:

#Funcao comun
def funcao_1(x):
    return x + 1
print(f'\nO valor retornado é {funcao_1(9)}')

#Funcao lambda com variaveis tipadas
funcao_1 = lambda x : x + 1
print(f'\nO valor retornado é:{funcao_1(9)}')

#Expressões lambda com mais de um parâmetro de entrada 
nome_completo = lambda nome, sobrenome : nome.strip().title() + " " + sobrenome.strip()
print(f'\nInstituição: {nome_completo("IFRO", "Campus Ariquemes")}')
print(f'\nCurso: {nome_completo("Análise", "e Desenvolvimento de Sistemas - ADS")}')

# Ordenando listas usando expressão lambda
atores = ["Leonardo DiCarpio",
          "Brad Pitt",
          "Dezel Washington",
          "philip Seymour Hoffman",
          "Jonhny Depp"]
atores.sort(key=lambda sobrenome: sobrenome.split(" ")[-1].lower())
print(f'\nLista ordenada: {atores}\n')

#Lambda para calcular funções quadráticas
def funcao_quadratica(a, b, c):
    return lambda x : a * x ** 2 + b * x + c

quadratica = funcao_quadratica(2, 3, -5)

print(f'\nFuncao quadratica de 0 = {quadratica(3)}')
print(f'\nFuncao quadratica de 1 = {quadratica(6)}')
print(f'\nFuncao quadratica de 2 = {quadratica(9)} \n')

#Lambda para evitar escrever duas funções 
def somar(x):
    funcao_2 = lambda x : x + 9
    return funcao_2(x) * 1

print(f'\nO valor retornado é: {somar(4)}')

#Lambda - função sem a palavra reservada def() 
a = lambda x : x * 2
print(f'\nO valor da expressãp é: {a(6)}\n')
"""
 #Diferentes entradas de dados para funções lambda
sem_entrada = lambda: 'Estrutura de Dados'
uma_entrada = lambda x: 5*x+3
duas_entradas = lambda x, y: (x*y) ** 0.8
tres_entradas = lambda x, y, z: 5 / ( 2 / x + 2 / y + 2 / z)

print








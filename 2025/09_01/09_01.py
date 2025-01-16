"""
Wellington Pereira Luiz - 09/01/2025
"""

#Exemplo 1
estudantes = [('Ana', 95), ('Bruno', 88), ('Carlos', 74)]

notas_para_letras = {nome: 'A' if nota >= 90 else 'B' if nota >= 80 else 'C' for nome, nota in estudantes}

print(f'\n>>> Notas convertidas para o sistema de letras:\n')

print(f'{notas_para_letras} \n')


#Exemplo 2
produtos = {'maçã': 0.50, 'banana': 0.25, 'uva': 1.20, 'laranja': 0.80}

produtos_2 = {produto: preco for produto, preco in produtos.items() if preco > 1.00}

print(f'\n>>> Filtragem de produtos com preço maior que R$ 1,00:\n')

print(f'\n{produtos_2} \n')


#Exemplo 3
funcionarios = {'Ana': 101, 'Bruno': 102, 'Carlos': 103}

invertido = {id: nome for nome, id in funcionarios.items()}

print(f'\n>>> Invertendo chave e valor para valor e chave:')

print(f'\nDicionário original: {funcionarios}')

print(f'\nDicionário invertido: {invertido} \n')


#Exemplo 4
arquivo = open('nomes.txt')

print(f'\nO Conteúdo do arquivo é: {arquivo}')

print(f'\nO tipo do arquivo é: {type(arquivo)} \n')


#Exemplo 5
arquivo = open('nomes.txt', 'r')

conteudo = arquivo.read()

print(f'\nO Conteúdo do arquivo é: {conteudo} \n')

print(f'\nO tipo da variável conteudo é: {type(conteudo)} \n')

arquivo.close()


#Exemplo 6
arquivo = open('nomes.txt', 'a')

for i in range(2):
    linha = input('\nDigite um nome: ') + ' ' + input('Digite o sobrenome: ')

    arquivo.write(linha + ('\n' if i < 1 else ''))

arquivo.close()


#Exemplo 7
arquivo = open('nomes.txt', 'r')

conteudo = arquivo.read()

print(f'\n>>> O Conteúdo do arquivo é:')

print(f'\n{conteudo}')

print(f'\nO tipo da variável que armazenou o conteúdo do arquivo é: {type(conteudo)} \n')

arquivo.close()


#Exemplo 8
arquivo = open('nomes.txt', 'r')

conteudo = arquivo.readlines()

print()

[print(i.strip()) for i in conteudo]

print()

arquivo.close()


#Exemplo 9
arquivo = open('nomes.txt', 'r')
conteudo = arquivo.readlines()

dados = []
[dados.append(i.split()) for i in conteudo]

print(f'\n{dados[0]}')
print(dados[1])

print(f'\n{dados[0][0]}')
print(f'{dados[1][0]} \n')

arquivo.close()


#Exemplo 10
arquivo = 'nomes.txt'

try:
    conteudo = open(arquivo, 'x')
    
    arquivo.write('Gestronildo Petrolino')
    
    arquivo.close()

except FileExistsError:
    print(f'\nO arquivo {arquivo} já existe... \n')


#Exemplo 11
arquivo = open('nomes.txt', 'r')

print(f'\nO arquivo {arquivo.name}, está fechado? \n')

if arquivo.closed:
    print('\nO arquivo está fechado...')
else:
    print(f'{arquivo.closed}')
    print(f'\nO arquivo {arquivo.name} está aberto!!! \n')

arquivo.close()


#Exemplo 12
with open('clientes.txt', 'r') as arquivo:
    conteudo = arquivo.readlines()

    [print('\n', i) for i in conteudo]

if arquivo.closed:
    print(arquivo.closed)
    print('O arquivo está fechado')
else:
    print(arquivo.closed)
    print('O arquivo está aberto')

# 14 – Exercício: Cadastramento de frutas

#Exercicio 14
from pathlib import Path

arquivo = 'frutaria.txt'

# Gerenciar o contexto do arquivo com o bloco with
if not Path(arquivo).exists():
    with open(arquivo, 'w') as file:
        print("Arquivo 'frutaria.txt' criado.")
else:
    print("Arquivo 'frutaria.txt' já existe. Abrindo para adicionar frutas...")

while True:
    fruta = input("Digite o nome de uma fruta (ou digite 'sair' para encerrar): ").strip()
    if fruta.lower() == 'sair':
        break
    with open(arquivo, 'a') as file:
        file.write(f"{fruta}\n")

print("\nFrutas cadastradas com sucesso!")

#Exercicio 15
from pathlib import Path

arquivo = 'pessoas.txt'

indice = 0

# Tratamento de exceção e abertura do arquivo
try:
    if Path(arquivo).exists():
        with open(arquivo, 'r') as file:
            linhas = file.readlines()
            indice = len(linhas)  # Captura o número de linhas no arquivo
    else:
        with open(arquivo, 'w') as file:
            indice = 0
            print("Arquivo 'pessoas.txt' criado.")
except Exception as e:
    print(f"Erro ao acessar o arquivo: {e}")

# Entrada de dados pelo operador
while True:
    nome = input("Digite o nome (ou 'sair' para encerrar): ").strip()
    if nome.lower() == 'sair':
        break
    sobrenome = input("Digite o sobrenome: ").strip()
    sexo = input("Digite o sexo (M/F): ").strip().upper()

    with open(arquivo, 'a') as file:
        file.write(f"{indice}, {nome}, {sobrenome}, {sexo}\n")
    indice += 1

print("\nDados cadastrados com sucesso!\n")

# Leitura do arquivo e criação de lista aninhada
with open(arquivo, 'r') as file:
    conteudo = file.readlines()

lista_aninhada = [linha.strip().split(', ') for linha in conteudo]

print("\nLista aninhada gerada a partir do arquivo:")
print(lista_aninhada)


#Exercicio 16
from io import StringIO

arquivo = StringIO()
arquivo = open('teste.txt', 'a')
arquivo.write('Escrevendo no arquivo que está na memória principal com StringIO\n')
arquivo.close()

arquivo = open('teste.txt')
print(arquivo.read())
arquivo.close()


#Exercicio 17
numeros = [1, 2, 3, 4, 5]

classificacao = {num: 'par' if num % 2 == 0 else 'impar' for num in numeros}

print("\nClassificação de números:")
print(classificacao)

#Exercicio 18
tuplas = [(4, 3), (1, 2), (8, 9)]

invertidas = [(b, a) for a, b in tuplas]

print("\nLista de tuplas invertidas:")
print(invertidas)

#Exercicio 19
numero = {'a': 1, 'b': 2, 'c': 3, 'd': 4, 'e': 5}

quadrados = {chave: valor ** 2 for chave, valor in numero.items()}

print("\nDicionário com quadrados dos valores:")
print(quadrados)
print(f"Tipo da variável: {type(quadrados)}")

#Exercicio 20
tuplas = [(4, 2, 3), (5, 1, 2), (7, 8, 9)]

resultado = [(t[0], [t[1], t[2]]) for t in tuplas]

print("\nTransformação de tuplas:")
print(resultado)

#Exercicio 21
string = 'abcde'
numeros = [1, 2, 3, 4, 5]

if len(string) == len(numeros):
    dicionario = {string[i]: numeros[i] for i in range(len(string))}
    print("\nDicionário gerado a partir das sequências:")
    print(dicionario)
else:
    print("Erro: As sequências têm tamanhos diferentes.")

#Exercicio 22
import math

lista = [math.sqrt(x) for x in range(3, 10)]

print("\nLista com raízes quadradas:")
print(lista)

#Exercicio 23
nrs = {x: x ** 2 for x in range(1, 10)}

print("\nDicionário com quadrados dos números:")
print(nrs)

#Exercicio 24
import math

lista = [x for x in range(3, 10) if math.sqrt(x) % 1 == 0]

print("\nLista com números que têm raízes quadradas inteiras:")
print(lista)

#Exercicio 25
import math

dicionario = {x: math.sqrt(x) for x in range(3, 10) if math.sqrt(x) % 1 == 0}

print("\nDicionário com raízes quadradas exatas:")
print(dicionario)

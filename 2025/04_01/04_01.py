"""
Wellington Pereira Luiz - 04/01/2025
"""

import math

#Operação tradicional com listas
'''EXEMPLO 1
lista_1 = []

for i in range(0, 10):
    lista_1.append(i)

print(f'\nRange em lista tradicional: {lista_1}')
'''

#Operação com list comprehension com listas
'''EXEMPLO 2
lista_1 = []

for i in range(0, 10):
    lista_1.append(i)

print(f'\nRange em lista tradicional: {lista_1}')
'''

#Exercicio 1
numeros = [3, 6, 9, 1]
lista_e1 = [num * 2 for num in numeros]
print(lista_e1)

# Exercicio 2
numeros = [1, 2, 3, 4]
lista_e2 = [(num, num * 2) for num in numeros]
print(lista_e2)

#Exercicio 3
letras = 'abcdefgh'
lista_e3 = [letra.upper() for letra in letras]
print(lista_e3)

#Exercicio 4
sequencia = range(10)
lista_pares = [num for num in sequencia if num % 2 == 0]
print(lista_pares)

#Exercicio 5
nomes = [input("Digite um nome: ") for _ in range(3)]
print(nomes)

#Exercicio 6
def maiuscula(nome):
    return nome.capitalize()

lista_e6 = ['jacobina', 'jurescreusa', 'cremilda', 'gertrudez', 'gnomica', 'gertralina', 'gerisprundencia']
nomes_maiusculos = [maiuscula(nome) for nome in lista_e6]
print(nomes_maiusculos)

#Exercicio 7
valores = [0, "", True, 1, 3.14]
valores_bool = [bool(valor) for valor in valores]
print(valores_bool)

#Exercicio 8
inteiros = [1, 2, 3, 4, 5]
inteiros_str = [str(num) for num in inteiros]
print(inteiros_str)

#Exercicio 9
numeros = [1, 2, 3, 4, 5, 6]
pares = [num for num in numeros if num % 2 == 0]
impares = [num for num in numeros if num % 2 != 0]
print("Pares:", pares)
print("Ímpares:", impares)



#EXERCÍCIO 10

import regex as re  

def valida_nome(nome):
    try:
        if not nome:  
            print('Nome inválido.')
            return False

        pattern = r'^[\p{L}\s]+$'

        if not re.match(pattern, nome):
            print('Nome inválido. Não use números ou caracteres especiais.')
            return False

       
        nome = ' '.join([parte.capitalize() for parte in re.sub(r'\s+', ' ', nome).split()])

        return nome

    except re.error:
        print("Erro ao validar o nome usando regex.")
        return False
def cadastro():
    nomes = []

    while True:
        nome = input("Digite um nome ou '0' para sair: ")

        if nome == '0': 
            break

        nome_validado = valida_nome(nome)
        if nome_validado:
            nomes.append(nome_validado)

    
    [print(nome) for nome in sorted(nomes)]


cadastro()



#EXEMPLO 3
from tkinter import *

def configurar_app():
    # configura a janela principal
    app.title('Análise e Desenvolvimento de Sistemas')
    app.geometry('1360x670')
    app.configure(background='#F8F8FF')
    app.resizable(True, True)
    app.maxsize(width=1360, height=670)

def criar_frame():
    # cria e retorna um frame para o cadastro
    frame = LabelFrame(app, text=' Cadastro ', borderwidth=1, relief='solid')
    frame.place(x=10, y=10, width=1340, height=340)
    return frame

def criar_labels(frame):
    # cria labels dentro do frame
    lb_1 = Label(frame, text='Contatos:', fg='red', font=("Arial", 14, "italic", "bold"))
    lb_1.place(x=15, y=10, width=70, height=20)

    lb_2 = Label(frame, text='Digite um nome:', font=("Arial", 14))
    lb_2.place(x=20, y=35, width=120, height=20)

    lb_3 = Label(frame, text='', font=("Arial", 14))
    lb_3.place(x=490, y=185, width=95, height=20)
    return lb_3  # retorna para que possa ser acessado na função capturar

def criar_entry(frame):
    # cria e retorna uma entrada de texto dentro do frame
    nome = Entry(frame, font=("Arial", 14))
    nome.place(x=135, y=35, width=400, height=20)
    return nome

def criar_botao():
    # cria o botão para captura de dados
    btn_captura = Button(app, text='Capturar dados', font=("Arial", 14, "bold"), command=capturar)
    btn_captura.place(x=490, y=300, width=125, height=40)

def capturar():
    # captura o nome digitado e atualiza a label lb_3
    lb_3['text'] = nome.get()

app = Tk()
configurar_app()
frame = criar_frame()
lb_3 = criar_labels(frame)
nome = criar_entry(frame)
criar_botao()

app.mainloop()


# EXERCÍCIO 11
from tkinter import *
import re

def configurar_app():

    app.title("Validação de Nome com Tkinter")
    app.geometry("600x400")
    app.configure(background="#F8F8FF")
    app.resizable(False, False)

def validar_nome(nome):
    try:
   
        if not nome.strip():
            raise ValueError("Nome inválido: O campo está vazio.")

        if not re.match(r"^[A-Za-zÀ-ÖØ-öø-ÿÇç\s]+$", nome):
            raise ValueError("Nome inválido: Não use números ou caracteres especiais.")

        
        nome = " ".join(nome.split())

       
        nome = " ".join([palavra.capitalize() for palavra in nome.split()])

        return nome
    except ValueError as e:
        lb_mensagem['text'] = str(e) 
        return None

def capturar():
   
    nome_input = nome.get()
    nome_validado = validar_nome(nome_input)
    if nome_validado:
     
        lb_resultado['text'] = f"Nome válido: {nome_validado}"
        lb_mensagem['text'] = ""  

def criar_interface():
  
    Label(app, text="Digite o nome:", font=("Arial", 14)).place(x=20, y=30)
    
    global nome
    nome = Entry(app, font=("Arial", 14))
    nome.place(x=150, y=30, width=400, height=30)

    Button(app, text="Validar", font=("Arial", 14), command=capturar).place(x=240, y=80)

    global lb_mensagem
    lb_mensagem = Label(app, text="", font=("Arial", 12), fg="red", bg="#F8F8FF")
    lb_mensagem.place(x=20, y=130)

    global lb_resultado
    lb_resultado = Label(app, text="", font=("Arial", 12), fg="green", bg="#F8F8FF")
    lb_resultado.place(x=20, y=170)

app = Tk()
configurar_app()
criar_interface()
app.mainloop()

#Exercicio 12
#Analise:Cria um dicionário onde cada número vira "par" ou "impar" dependendo 
#do resto da divisão por 2.
numeros = [1, 2, 3, 4, 5]
resultado = {num:('par' if num % 2 == 0 else 'impar') for num in numeros}
print(resultado)



#Exercicio 13
#Analise: Pega uma lista de tuplas, inverte os valores (x vira y, y vira x) 
#e joga tudo numa nova lista.
lista_lc_6 = [(y,x) for x, y in [(4, 3), (1, 2), (8,9)]]
print(lista_lc_6)


#Exercicio 14
#Analise: esta desmembrando as tuplasos, os primeiros valores vão pra x (como lista) 
#e o último pra y. Mesma lógica da questao anterior mas invertida.
lista_lc_7 = [(x, y) for *x, y in [(4, 2, 3), (5, 1, 2), (7, 8, 9)]]
print(lista_lc_7)


#Exercicio 15
#Analise: Pega o primeiro valor das tuplas pra x e o resto vira y (como lista). 
#Outra variação do exercicio anterior. 
lista_lc_8 = [(x, y) for x, *y in [(4, 2, 3), (5, 1, 2), (7, 8, 9)]]
print(lista_lc_8)


#Exercicio 16
#Analise:Calcula as raízes quadradas de números entre 3 e 9 e bota numa lista.
lista_lc_9 = [math.sqrt(z) for z in range(3, 10)]
print(lista_lc_9)

#Exercicio 17
#Analise:Filtra os números entre 3 e 9 com raiz quadrada inteira. 
#Se a raiz não tiver decimal, entra na lista e apos e mostrado no terminal.
# % 1 == 0 ==> Raiz quadrada inteira
lista_lc_10 = [x for x in range(3, 10) if math.sqrt(x) % 1 == 0]
print(lista_lc_10)


#Exercicio 18
#Analise:Eleva os valores de um dicionário ao quadrado e mostra o resultado junto com o tipo.
numero = {'a':1, 'b':2, 'c':3, 'd':4, 'e':5}
quadrado = {chave:valor ** 2 for chave, valor in numero.items()}
print(quadrado)
print(type(quadrado))


#Exercicio 19
#Analise:Pega uma lista, eleva cada número ao quadrado e joga num dicionário.
# Mesma ideia do 18, só que com lista.
numeros = [1, 2, 3, 4, 5]
quadrados = {valor:valor ** 2 for valor in numeros}
print(quadrados)

#Exercicio 20
#Analise:Cria um dicionário combinando caracteres de uma string com números de uma lista.
chaves = 'abcde'
valores = [1,2,3,4,5]
miscelania = {chaves[i]: valores[i] for i in range(0, len(chaves))}
print(miscelania)


#Exercicio 21
#analise:Exatamente igual ao 12.
numeros = [1, 2, 3, 4, 5]
resultado = {num:('par' if num % 2 == 0 else 'impar') for num in numeros}
print(resultado)


#Exercicio 22
#Analise:Faz um conjunto com os números de 1 a 6 usando compreensão de conjuntos.
nrs = {num for num in range(1, 7)}
print(nrs)

#Exericio 23
#Analise:Cria um dicionário com números de 1 a 9 e seus quadrados.
nrs = {x:x**2 for x in range(1, 10)}
print(nrs)

#Exericio 24
#Analise:O código pega as letras da frase e joga num conjunto, tirando as repetidas. 
#O print mostra tudo bagunçado porque conjunto não tem ordem.
letra = {letra for letra in 'Instituto Federal de Rondonia'}
print(letra)


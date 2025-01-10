
'''def criar_no(valor):
    return {
            "valor": valor,
            "proximo": None
            }

def lista_vazia(lista):
    if lista is None:
        return True
    
    return False

def insere_inicio(lista, valor):

    novo_no = criar_no(valor)
    novo_no["proximo"] = lista
    return novo_no

def exclui_inicio(lista):
    
    if lista_vazia(lista):
        print("A lista está vazia...")
        return None
    return lista["proximo"]

def mostra_topo(lista):
    if lista_vazia(lista):
        return "A lista está vazia..."
    return lista["valor"]

pilha = None

#Empilhando
print(f"\nInserindo elementos no topo da pilha...\n")

pilha = insere_inicio(pilha, 'Abacaxi')
print(mostra_topo(pilha))
pilha = insere_inicio(pilha, 'Amendoim')
print(mostra_topo(pilha))
pilha = insere_inicio(pilha, 'Ameixa')
print(mostra_topo(pilha))
pilha = insere_inicio(pilha, 'Amora')
print(mostra_topo(pilha))

input(f'\nFinal do empilhamento - tecle <Enter>')

#Desempilhando
print(f"\nDesempilhando elementos no topo da pilha...\n")

pilha = exclui_inicio(pilha)
print(mostra_topo(pilha))
pilha = exclui_inicio(pilha)
print(mostra_topo(pilha))
pilha = exclui_inicio(pilha)
print(mostra_topo(pilha))
pilha = exclui_inicio(pilha)
print(f"{mostra_topo(pilha)}\n")'''

'''def criar_pilha():
    return []

def push(pilha, valor):
    pilha.append(valor)

def pop(pilha):
    if not is_empty(pilha):
        return pilha.pop()

def size(pilha):
    return len(pilha)

def peek(pilha):
    if not is_empty(pilha):
        return pilha[-1]

def is_empty(pilha):
    return pilha == []

pilha = criar_pilha()

if is_empty(pilha):
    print(f'\nA fila esta vazia')

for i in range(3):
    valor = input(f"\nEmpilhe as caixas: ")
    push(pilha, valor)

print(f"Qtd total de itens na pilha -> {size(pilha)}")
print(f"O item que está no topo da pilha -> {peek(pilha)}")

print("\nOs itens que estão na pilha são: ")
for item in reversed(pilha):
    print(item)

print(f"\n O item retirado foi: {pop(pilha)}\n")
for item in reversed(pilha):
    print(item)'''


'''
Autor: Welington Pereira Luiz
Linguagem: Python
Data: 28-11-2024

Exercício: imagine uma demanda no qual você precisa desenvolver uma 
ferramenta de análise para um software matemático.  
Cenário: Ferramenta de Análise para Software Matemático 
Considere que você é um programador da empresa MatheSoftware Ltda. 
Esta empresa é líder no desenvolvimento de softwares matemáticos. 
Recentemente, ela lançou uma funcionalidade que permite aos usuários 
inserirem suas próprias fórmulas matemáticas para serem resolvidas pelo 
software. No entanto, os usuários têm relatado erros quando inserem fórmulas 
com parênteses mal formatados. 
O departamento de suporte técnico está sobrecarregado com chamados, 
e a equipe de desenvolvimento está buscando uma solução rápida para verificar 
a formatação dos parênteses nas fórmulas inseridas pelos usuários. 
Sua tarefa é desenvolver uma ferramenta que verifique se, em uma 
expressão matemática, os parênteses estão corretamente balanceados. Esta 
ferramenta será integrada ao software principal para alertar o usuário 
imediatamente se a fórmula inserida contém parênteses mal formatados. 
Com base na demanda do cenário, sem utilizar inteligência artificial você 
deve: 
a) Definir todos os requisitos necessários para resolver o problema.

b) Utilizar pilha nativa do Python, para resolver o processo e solicitar que o usuário insira uma expressão matemática

c) Garantir que a pilha com o valor inserido pelo usuário não esta vazia para que haja algo a ser verificado

d) Incrementar a variavel 'result' caso haja um abre parenteses '(' e decrementar esta mesma variavel caso haja um fecha parenteses ')'
    dentro da funcao 'parenthesis_counter'

e) Verificar se a variavel 'result'  termina o laço de iteração com valor zero.
    Caso assim seja então todos os parenteses abertos foram fechados, caso contrário então nem todos os pares de parenteses
    foram fechados

f) Retornar o resultado e exibir para o usuário.
...  
Para definir o restante dos requisitos considere as entradas e saídas: 
- Entrada: "(1 + 2)" - Saída: True 
- Entrada: "1 + 2)" -Saída: False 
- Entrada: "((3 * 4) + 5)" - Saída: True 
- Entrada: "((3 * 4 + 5)" - Saída: False
'''

def criar_pilha(expressao):
    return [char for char in expressao]

def push(pilha, valor):
    pilha.append(valor)

def pop(pilha):
    if not is_empty(pilha):
        return pilha.pop()

def size(pilha):
    return len(pilha)

def peek(pilha):
    if not is_empty(pilha):
        return pilha[-1]

def is_empty(pilha):
    return pilha == []

def parenthesis_counter(expression):
    pilha = criar_pilha(expression)
    
    if is_empty(pilha):
        return False
    
    result = 0

    for char in pilha:
        if char == "(":
            result += 1
        elif char == ")":
            result -= 1
            if result < 0:
                return False

    return result == 0

expressao = input("Insira a sua expressão: ")
print("Parênteses balanceados?", parenthesis_counter(expressao))


"""
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def insert_at_beginning(self, data):
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node

    def print_list(self):
        current = self.head
        while current:
            print(current.data, end=" -> ")
            current = current.next
        print("None")




linked_list = LinkedList()
linked_list.insert_at_beginning(10)
linked_list.insert_at_beginning(20)
linked_list.insert_at_beginning(30)
linked_list.print_list()  # Saída esperada: 30 -> 20 -> 10 -> None
"""

# Exemplo de lista em Python
lista = []
lista.insert(0, 10)  # Inserindo no início (equivalente a insert_at_beginning)
lista.insert(0, 20)
lista.insert(0, 30)
lista.print_list()  # Saída: [30, 20, 10]

print("print")
class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

class LinkedList:
    def __init__(self, value):
        # cria um nó e inicializa a lista
        new_node = Node(value)
        self.head = new_node
        self.tail = new_node
        self.length = 1

    def append(self, value):
        # cria um nó e coloca no fim da lista
        self.value = value

    def prepend(self, value):
        # cria um nó e adiciona ele ao inicio da lista
        self.value = value

    def insert(self, index, value):
        # cria um nó e adiciona ele num indice escolhido
        self.value = value
    
my_linked_list = LinkedList(4)
print(my_linked_list.head.value)
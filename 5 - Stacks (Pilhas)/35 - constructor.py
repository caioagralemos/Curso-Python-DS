class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

class Stack:
    # Stack (Pilha) é a caixa de bolas de tenis
    def __init__(self, value):
        new_node = Node(value)
        # em stack só precisamos saber o que tá no topo pois só é possível realizar op. com ele
        self.top = new_node
        self.height = 1

    def print_stack(self):
        # aqui começa no top
        temp = self.top
        while temp:
            print(temp.value)
            temp = temp.next
    
my_stack = Stack(4)

my_stack.print_stack()
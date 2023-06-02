class Node:
    def __init__(self, value):
        self.value = value
        self.next = None
        self.prev = None

class DoublyLinkedList:
    def __init__(self,value):
        new_node = Node(value)
        self.head = new_node
        self.tail = new_node
        self.length = 1
    
    def print_list(self):
        temp = self.head
        while temp is not None:
            # esse while vai iterando a lista
            print(temp.value)
            temp = temp.next
    
    def append(self, value):
        temp = self.head
        new_node = Node(value)
        if temp is None:
            self.head = new_node
            self.tail = new_node
            self.length = 1
            return True
        pre = self.tail
        pre.next = new_node
        new_node.prev = pre
        self.tail = new_node
        self.length += 1
        return True
    
    def pop(self):
        temp = self.tail
        if temp is None:
            return None
        if temp == self.head:
            self.head = None
            self.tail = None
            self.length = 0
            return temp
        pre = temp.prev
        self.tail = pre
        temp.prev = None
        pre.next = None
        self.length -= 1
        return temp
        
        
my_doubly_linked_list = DoublyLinkedList(1)
my_doubly_linked_list.append(2)
my_doubly_linked_list.pop()
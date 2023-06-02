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

    def prepend(self, value):
        temp = self.head
        new_node = Node(value)
        if temp is None:
            self.head = new_node
            self.tail = new_node
            self.length = 1
            return True
        self.head = new_node
        temp.prev = new_node
        new_node.next = temp
        self.length += 1
        return True
    
    def get(self, index):
        if index > self.length - 1 or index < 0:
            return None
        if index < self.length/2:
            temp = self.head
            for _ in range(index):
                temp = temp.next
            return temp
        else:
            temp = self.tail
            for _ in range(self.length-1, index, -1): # vai contar ao contrario
                temp = temp.prev
            return temp
        
    def insert(self, index, value):
        if index > self.length or index < 0:
            return False
        elif index == 0:
            return self.prepend(value)
        elif index == self.length:
            return self.append(value)
        else:
            new_node = Node(value)
            before = self.get(index-1)
            after = before.next
            new_node.next = after
            new_node.prev = before
            before.next = new_node
            after.prev = new_node
            self.length += 1
            return True
        
my_doubly_linked_list = DoublyLinkedList(1)
my_doubly_linked_list.append(2)
my_doubly_linked_list.append(3)
my_doubly_linked_list.append(4)
my_doubly_linked_list.append(5)

my_doubly_linked_list.insert(6, 5)
my_doubly_linked_list.print_list()
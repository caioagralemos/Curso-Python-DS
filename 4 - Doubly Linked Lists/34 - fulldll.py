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
    
    def pop_first(self):
        temp = self.head
        if temp is None:
            return None
        if temp == self.tail:
            self.head = None
            self.tail = None
            self.length = 0
            return temp
        pre = temp.next
        self.head = pre
        temp.next = None
        pre.prev = None
        self.length -= 1
        return temp
    
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
        
    def set_value(self, index, value):
        node = self.get(index)
        if node:
            node.value = value
            return True
        else:
            return False
        
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
    
    def remove(self, index):
        if index > self.length or index < 0:
            return False
        elif index == 0:
            return self.pop_first()
        elif index == self.length - 1:
            return self.pop()
        else:
            temp = self.get(index)
            after = temp.prev
            before = temp.next
            after.next = before
            before.prev = after
            self.length -= 1
            return temp
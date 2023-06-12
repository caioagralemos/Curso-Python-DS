class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

class LinkedList:
    def __init__(self, value):
        new_node = Node(value)
        self.head = new_node
        self.tail = new_node
        self.length = 1

    def print_list(self):
        temp = self.head
        while temp is not None:
            print(temp.value)
            temp = temp.next
    
    def append(self, value):
        new_node = Node(value)
        if self.head is None:
            self.head = new_node
            self.tail = new_node
            self.length = 1
        else:
            self.tail.next = new_node
            self.tail = new_node
            self.length += 1
        return True
    
    def pop(self):
        temp = self.head
        pre = self.head
        if self.head is None:
            return None
        elif self.head == self.tail:
            self.tail = None
            self.head = None
            self.length = 0
            return temp
        else:
            while temp.next is not None:
                pre = temp
                temp = temp.next
            self.tail = pre
            self.tail.next = None
            self.length -= 1
            return temp
    
    def prepend(self, value):
        new_node = Node(value)
        if self.head is None:
            self.head = new_node
            self.tail = new_node
        else:
            new_node.next = self.head
            self.head = new_node
        self.length += 1
        return True
    
    def pop_first(self):
        if self.length == 0:
            return None
        temp = self.head
        self.head = self.head.next
        temp.next = None
        self.length -= 1
        if self.length == 0:
            self.tail = None
        return temp
    
    def get(self, index):
        if index > self.length - 1 or index < 0:
            return False
        temp = self.head
        for _ in range(index):
            temp = temp.next
        return temp
    
    def set(self, index, value):
        temp = self.get(index)
        if temp:
            temp.value = value
            return True
        return False
    
    def insert(self, index, value):
        if index > self.length or index < 0:
            return False
        if index == 0:
            return self.prepend(value)
        if index == self.length:
            return self.append(value)
        new_node = Node(value)
        temp = self.get(index-1)
        new_node.next = temp.next
        temp.next = new_node
        self.length += 1
        return True
    
    def remove(self,index):
        if index >= self.length or index < 0:
            return False
        if index == 0:
            return self.pop_first()
        if index == self.length - 1:
            return self.pop()
        pre = self.get(index-1)
        temp = self.get(index)
        pre.next = temp.next
        temp.next = None
        self.length -= 1
        return True
    
    def reverse(self):
        temp = self.head
        self.head = self.tail
        self.tail = temp
        before = None
        after = temp.next
        for _ in range(self.length):
            after = temp.next
            temp.next = before
            before = temp
            temp = after
    
    def bubble_sort(self):
        for i in range(self.length - 1, 0, -1):
            temp = self.head
            for j in range(i):
                if temp.value > temp.next.value:
                    tempVar = temp
                    temp = temp.next
                    temp.next = tempVar
        return True

my_linked_list = LinkedList(1)
my_linked_list.append(10)
my_linked_list.append(3)
my_linked_list.append(7)
my_linked_list.print_list()
my_linked_list.bubble_sort()
my_linked_list.print_list()
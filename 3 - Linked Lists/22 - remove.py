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

    def get(self, index):
        if index > self.length - 1 or index < 0:
            return False
        temp = self.head
        for _ in range(index):
            temp = temp.next
        return temp
    
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

my_linked_list = LinkedList(4)
my_linked_list.append(6)
my_linked_list.append(2)
my_linked_list.append(1)
print(my_linked_list.print_list())
my_linked_list.remove(1)
print(my_linked_list.print_list())

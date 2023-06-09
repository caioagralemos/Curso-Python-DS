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
    
    def get(self, index):
        if index > self.length - 1 or index < 0:
            return None
        temp = self.head
        for _ in range(index):
            temp = temp.next
        return temp

my_linked_list = LinkedList(4)
my_linked_list.append(6)
my_linked_list.append(7)
my_linked_list.append(8)
print(my_linked_list.print_list())
print(my_linked_list.get(2))
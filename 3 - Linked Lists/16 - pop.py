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
            # esse while vai iterando a lista
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

my_linked_list = LinkedList(4)
# print(my_linked_list.print_list())
my_linked_list.append(6)
# my_linked_list.append(9)
# my_linked_list.append(7)
# my_linked_list.append(1)
print(my_linked_list.pop())
print(my_linked_list.pop())
print(my_linked_list.pop())
my_linked_list.print_list()
# print(my_linked_list.print_list())
# print(my_linked_list.length)
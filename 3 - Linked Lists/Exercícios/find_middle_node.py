class Node:
    def __init__(self, value):
        self.value = value
        self.next = None
        

class LinkedList:
    def __init__(self, value):
        new_node = Node(value)
        self.head = new_node
        self.tail = new_node

        
    def append(self, value):
        new_node = Node(value)
        if self.head == None:
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next = new_node
            self.tail = new_node
        return True
        

    def find_middle_node (self):
        middle_it = self.head
        full_it = self.head
        contador = 0
        while full_it:
            contador += 1
            full_it = full_it.next
            if contador % 2 == 0:
                middle_it = middle_it.next
        return middle_it



my_linked_list = LinkedList(1)
my_linked_list.append(2)
my_linked_list.append(3)
my_linked_list.append(4)
my_linked_list.append(5)

print( my_linked_list.find_middle_node().value)



"""
    EXPECTED OUTPUT:
    ----------------
    3
    
"""
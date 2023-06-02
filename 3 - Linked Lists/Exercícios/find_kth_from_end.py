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
  
  
        
#### WRITE FIND_KTH_FROM_END FUNCTION HERE ####
#                                             #
#    This is a separate function that is      #
#    not a method within the                  #
#    LinkedList class.                        #
#    Indent all the way to the left.          #
#                                             #
###############################################

def find_kth_from_end(linkedlist, k):
    fast = linkedlist.head
    slow = linkedlist.head

    for _ in range(k):
            if fast == None:
                return None
            fast = fast.next

    while fast:
        fast = fast.next
        slow = slow.next

    return slow



my_linked_list = LinkedList(1)
my_linked_list.append(2)
my_linked_list.append(3)
my_linked_list.append(4)
my_linked_list.append(5)


k = 6
result = find_kth_from_end(my_linked_list, k)

print(result)  # Output: 4



"""
    EXPECTED OUTPUT:
    ----------------
    4
    
"""
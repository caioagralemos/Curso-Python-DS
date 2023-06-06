class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

class BinarySearchTree:
    def __init__(self):
        self.root = None 

    def insert(self, value):
        new_node = Node(value)
        if self.root is None:
            self.root = new_node
            return self.root
        temp = self.root
        while True:
            if new_node.value == temp.value:
                return False
            if value < temp.value:
                if temp.left:
                    temp = temp.left
                else:
                    temp.left = new_node
                    return True
            elif value > temp.value:
                if temp.right:
                    temp = temp.right
                else:
                    temp.right = new_node
                    return True

        
# my_tree = BinarySearchTree()
# my_tree.insert(2)
# my_tree.insert(1)
# my_tree.insert(3)
# print(my_tree.insert(1))

# """
#     THE LINES ABOVE CREATE THIS TREE:
#                  2
#                 / \
#                1   3
# """


# print('Root:', my_tree.root.value)            
# print('Root->Left:', my_tree.root.left.value)        
# print('Root->Right:', my_tree.root.right.value)        



# """
#     EXPECTED OUTPUT:
#     ----------------
#     Root: 2
#     Root->Left: 1
#     Root->Right: 3

# """
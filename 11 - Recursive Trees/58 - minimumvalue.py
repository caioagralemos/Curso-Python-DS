class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

class recursiveBinarySearchTree:
    def __init__(self):
        self.root = None

    def __r_insert(self, current_node, new_node):
        if self.root == None:
            self.root = new_node
            return True
        if new_node == current_node:
            return False
        if new_node.value < current_node.value:
            if not current_node.left:
                current_node.left = new_node
                return True
            return self.__r_insert(current_node.left, new_node)
        elif new_node.value > current_node.value:
            if not current_node.right:
                current_node.right = new_node
                return True
            return self.__r_insert(current_node.right, new_node)

    def r_insert(self, value):
        new_node = Node(value)
        return self.__r_insert(self.root, new_node)
    
    def minimal_value(self, node):
        while node:
            if node.left is not None:
                node = node.left
            else:
                break
        return node.value
    
my_rBST = recursiveBinarySearchTree()
my_rBST.r_insert(9)
my_rBST.r_insert(7)
my_rBST.r_insert(2)
my_rBST.r_insert(4)
print(my_rBST.minimal_value(my_rBST.root))
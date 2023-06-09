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

    def __delete_node(self, current_node, value):
        if current_node is None: # O PROBLEMA todo TAVA AQUI '== None' para 'is None'
            return None
        if value < current_node.value:
            current_node.left = self.__delete_node(current_node.left, value)
        elif value > current_node.value:
            current_node.right = self.__delete_node(current_node.right, value)
        else:
            if current_node.left == None and current_node.right == None: 
                # se for um leaf node
                # vai igualar o current_node.left lá em cima a None
                return None 
            elif current_node.right is None: 
                # vai fazer o current_node.left lá em cima apontar pra o prox node
                current_node = current_node.left
            elif current_node.left is None: 
                # vai fazer o current_node.left lá em cima apontar pra o prox node
                current_node = current_node.right 
            else: 
                # se tiver itens dos dois lados
                sub_tree_min = self.min_value(current_node.right)
                current_node.value = sub_tree_min
                current_node.right = self.__delete_node(current_node.right, sub_tree_min)
            return current_node
    
    def delete_node(self, value):
        self.root = self.__delete_node(self.root, value)
        
    
    def min_value(self, node):
        while node:
            if node.left is not None:
                node = node.left
            else:
                break
        return node.value
    

    
my_tree = recursiveBinarySearchTree()
my_tree.r_insert(2)
my_tree.r_insert(1)
my_tree.r_insert(3)

"""
       2
      / \
     1   3
"""

print("root:", my_tree.root.value)
print("root.left =", my_tree.root.left.value)
print("root.right =", my_tree.root.right.value)


my_tree.delete_node(2)

"""
       3
      / \
     1   None
"""


print("\nroot:", my_tree.root.value)
print("root.left =", my_tree.root.left.value)
print("root.right =", my_tree.root.right)



"""
    EXPECTED OUTPUT:
    ----------------
	root: 2
	root.left = 1
	root.right = 3

	root: 3
	root.left = 1
	root.right = None

"""

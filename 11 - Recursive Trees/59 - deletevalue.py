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
        if current_node == None:
            return None
        if value < current_node.value:
            current_node.left = self.__delete_node(current_node.left, value)
        elif value > current_node.value:
            current_node.right = self.__delete_node(current_node.right, value)
        else:
            if current_node.left == None and current_node.right == None: 
                # se for um leaf node
                return None # vai igualar o current_node.left lá em cima a None
            
            elif current_node.left and current_node.right == None: 
                current_node = current_node.left
                # vai fazer o current_node.left lá em cima apontar pra o prox node
            
            elif current_node.left == None and current_node.right: 
                current_node = current_node.right 
                # vai fazer o current_node.left lá em cima apontar pra o prox node

            else: 
                # se tiver itens dos dois lados
                sub_tree_min = self.min_value(current_node.right)
                current_node.value = sub_tree_min
                current_node.right = self.__delete_node(current_node.right, sub_tree_min)

            return current_node
    
    def delete_node(self, value):
        self.__delete_node(self.root, value)
        
    
    def min_value(self, node):
        while node:
            if node.left is not None:
                node = node.left
            else:
                break
        return node.value
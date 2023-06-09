class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

class recursiveBinarySearchTree:
    def __init__(self):
        self.root = None

    def __r_contains(self, current_node, value):
        if current_node == None:
            return False
        if value == current_node.value:
            return True
        if value < current_node.value:
            return self.__r_contains(current_node.left, value)
        elif value > current_node.value:
            return self.__r_contains(current_node.right, value)

    def r_contains(self, value):
        return self.__r_contains(self.root, value)
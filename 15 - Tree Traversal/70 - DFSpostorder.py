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
    
    def contains(self,value):
        if self.root == None:
            return False
        temp = self.root
        while True:
            if temp.value == value:
                return True
            elif value < temp.value:
                if temp.left:
                    temp = temp.left
                else:
                    return False
            elif value > temp.value:
                if temp.right:
                    temp = temp.right
                else:
                    return False
                
    def dfs_post_order(self):
        results = []

        def traverse(current_node):
            if current_node.left is not None:
                traverse(current_node.left)
            if current_node.right is not None:
                traverse(current_node.right)
            results.append(current_node.value)

        traverse(self.root)

        return results

my_tree = BinarySearchTree()
my_tree.insert(5)
my_tree.insert(3)
my_tree.insert(1)
my_tree.insert(4)
my_tree.insert(9)
my_tree.insert(11)
my_tree.insert(8)

print(my_tree.dfs_post_order())
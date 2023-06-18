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

    def BFS(self):
        current_node = self.root
        queue = []
        results = []
        queue.append(current_node)

        while len(queue) > 0:
            current_node = queue.pop(0)
            results.append(current_node.value)
            if current_node.left is not None:
                queue.append(current_node.left)
            if current_node.right is not None:
                queue.append(current_node.right)
        return results
    

    
my_tree = BinarySearchTree()
my_tree.insert(5)
my_tree.insert(3)
my_tree.insert(1)
my_tree.insert(4)
my_tree.insert(9)
my_tree.insert(11)
my_tree.insert(8)

print('root:', my_tree.root.value) # 5

print('left:', my_tree.root.left.value) # 1
print('left and left:', my_tree.root.left.left.value) # 2
print('left and right:',my_tree.root.left.right.value) # 3

print('right:', my_tree.root.right.value) # 1
print('right and left:', my_tree.root.right.left.value) # 2
print('right and right:',my_tree.root.right.right.value) # 3

print(my_tree.BFS())
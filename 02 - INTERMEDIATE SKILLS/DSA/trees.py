class Node:
    def __init__(self,data):
        self.left = None
        self.data = data
        self.right = None
    
class Tree:
    def Create_node(self,data):
        return Node(data)
    def insert(self,node,data):
        if node is None:
            self.Create_node(data)
        if data < node.data:
            self.insert(node.left,data)
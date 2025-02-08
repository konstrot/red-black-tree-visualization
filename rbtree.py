class Node:
    def __init__(self, key, color='RED'):
        self.key = key
        self.color = color
        self.left = None
        self.right = None
        self.parent = None

class RedBlackTree:
    def __init__(self):
        self.NIL = Node(None, color='BLACK')  # Create NIL
        self.root = self.NIL  # Create root
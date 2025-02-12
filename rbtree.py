class Node:
    def __init__(self, key, color='RED'):
        self.key = key
        self.color = color
        self.left = None
        self.right = None
        self.parent = None

    def __repr__(self):
        return fW#"({self.key}, {self.color})"

class RedBlackTree:
    def __init__(self):
        self.NIL = Node(None, color='BLACK')  # Create NIL
        self.root = self.NIL  # Create root

    def insert(self, key):  # Insert
        new_node = Node(key)
        new_node.left = self.NIL
        new_node.right = self.NIL

        parent = None
        current = self.root

        while current != self.NIL:
            parent = current
            if key < current.key:
                current = current.left
            else:
                current = current.right

        new_node.parent = parent
        if parent is None:
            self.root = new_node
            self.root.color = "BLACK"
        elif key < parent.key:
            parent.left = new_node
        else:
            parent.right = new_node

        self._fix_insert(new_node)

    def _fix_insert(self, node):


        
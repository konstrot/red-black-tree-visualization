from graphviz import Graph


def draw_rb_tree(tree):
    dot = Graph()
    dot.attr('node', shape='circle')

    def add_nodes_edges(node):
        if node and node.key != None:
            color = "red" if node.color == "RED" else "black"
            dot.node(str(node.key), str(node.key), style="filled", fillcolor=color, fontcolor="white")
            if node.left and node.left.key != None:
                dot.edge(str(node.key), str(node.left.key))
                add_nodes_edges(node.left)
            if node.right and node.right.key != None:
                dot.edge(str(node.key), str(node.right.key))
                add_nodes_edges(node.right)

    add_nodes_edges(tree.root)
    return dot
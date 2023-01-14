class Node:
    def __init__(self, label):
        self.label = label
        self.visited = False
        self.adj_list = []

    def set_visited(self):
        self.visited = True

    def get_label(self):
        return self.label

    def add_adj(self, node):
        self.adj_list.append(node)

class Graph:
    def __init__(self):
        self.nodes = []

    def add_vertex(self, label):
        new_node = Node(label)
        self.nodes.append(new_node)

    def add_edge(self, src, dest):
        src_node = self.get_node(src)
        dest_node = self.get_node(dest)
        src_node.add_adj(dest_node)
        dest_node.add_adj(src_node)

    def remove_vertex(self, label):
        node = self.get_node(label)
        self.nodes.remove(node)

    def remove_edge(self, src, dest):
        src_node = self.get_node(src)
        dest_node = self.get_node(dest)
        src_node.adj_list.remove(dest_node)
        dest_node.adj_list.remove(src_node)

    def get_node(self, label):
        for node in self.nodes:
            if node.get_label() == label:
                return node

    def print_graph(self):
        for node in self.nodes:
            print(node.label, "->", [x.label for x in node.adj_list])

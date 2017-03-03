import os
import sys


DATA_PATH = "../../data/"
class Parser(object):

    graph = None
    nodes = []

    def __init__(self, graph_name):
        self.graph = DATA_PATH + graph_name
        self.load_all()

    def load_all(self):
        with open(self.graph, 'r') as graph:
            nodes = graph.readlines()
            for node in nodes:
                print (self.format_node(node))

    def format_node(self, node_line):
        vals = node_line.split(" ")
        node_i = int(vals[0])
        edges = [[node_i] + [int(n) for n in el.split(":")] for el in vals[1:]]
        return (node_i, edges)

if __name__ == "__main__":
    p = Parser(sys.argv[1])

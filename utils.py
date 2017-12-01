import re, sys, math, random, csv, types, networkx as nx
from collections import defaultdict

def parse(filename):
    reader = csv.reader(open(filename, 'r'), delimiter=' ')
    data = [row for row in reader]

    print "Reading and parsing the data into memory..."
    return parse_directed(data)

def parse_directed(data):
    DG = nx.DiGraph()

    for i, row in enumerate(data):

        node_a = format_key(row[0])
        node_b = format_key(row[1])
        DG.add_node(node_a)
        DG.add_node(node_b)
        DG.add_edge(node_a, node_b)

    return DG

def format_key(key):
    key = key.strip() 
    if key.startswith('"') and key.endswith('"'):
        key = key[1:-1]
    return key 


def print_results(f, method, results):
    print method
from utils import parse
import pagerank

graph = parse("graph.txt")
pagerank.rank(graph)
import networkx as nx
import numpy as np

def rank(G, beta=0.85, max_iter=100, tol=1.0e-6, weight='weight'):

    if len(G) == 0:
        return {}

    M = nx.stochastic_graph(G)
    N = M.number_of_nodes()

    C = nx.to_numpy_matrix(M)
    print C

    v = dict.fromkeys(M, 1.0 / N)
    t = dict.fromkeys(M, 1.0 / N)
    #print matrix
    print v

    # power iteration: make up to max_iter iteration
    iter = 0
    for _ in range(max_iter):
    	iter += 1
        vlast = v

        v = dict.fromkeys(vlast.keys(), 0)
        for n in v:
            for nbr in M[n]:
                v[nbr] += beta * vlast[n] * M[n][nbr][weight]
            v[n] += (1.0 - beta) * t.get(n,0)
        # check convergence, l1 norm

        err = sum([abs(v[n] - vlast[n]) for n in v])
        if err < N*tol:
            break

    print v
    print iter

import networkx


g = nx.MultiDiGraph()

while (True):
  try:
    entrada=input()
    entrada=entrada.split()
    g.addEdge(entrada[0],entrada[1]);
  except Exception:
    break
  entrada=input()
d = pagerank(g, alpha=0.85, max_iter=1000, tol=1e-06)


#after tests, create neural network, add here and merge the files, because in the beggining there's a lot of shell scripts

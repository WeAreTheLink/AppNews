import networkx


g = nx.MultiDiGraph()
entrada=input()
while (entrada != ""):
  entrada=entrada.split()
  g.addEdge(entrada[0],entrada[1]);
  entrada=input()
d = pagerank(g, alpha=0.85, max_iter=1000, tol=1e-06)

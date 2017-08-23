#!/usr/bin/env python2.7

import networkx
from pybrain import *
from pybrain.datasets import SupervisedDataSet


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


#possibly raise FileNotFound
def numberOfInputs():
    file=open("./var/differentWords","r")
    numberOfLines=0
    for line in file:
      numberOfLines+=1
    close(file)
    return numberOfLines


n=numberOfInputs()

#n inputs, 2 hidden layers with n neurons and 1 neuron for output
net = buildnetwork(n,n,n,1, bias=True)

#building the dataset

dataSet=SupervisedDataSet(n,1)
dataSet.










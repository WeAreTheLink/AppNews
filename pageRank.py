#!/usr/bin/env python2.7

import networkx
import sys
from pybrain import *
from pybrain.datasets import SupervisedDataSet


g = networkx.MultiDiGraph()

#we need data/graph be a file with the graph
fp=open("data/graph", "r")
for entrada in fp:
    entrada=entrada.split()
    g.addEdge(entrada[0],entrada[1]);

d = pagerank(g, alpha=0.85, max_iter=1000, tol=1e-06)


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


def getBagOfWords(pageName):
	

for pageName in d:
	pageRank=d[pageName]
	dataSet.addSample(getBagOfWords(pageName),pageRank)


#this is a preliminar study. Because normally we need two divisions : training set and verify set

from pybrain.supervised.trainers import BackpropTrainer

trainer = BackpropTrainer(net, dataSet)

error=trainer.trainUntilConvergence()

print error













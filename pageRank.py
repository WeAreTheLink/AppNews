#!/usr/bin/env python2.7

import networkx
import sys
from pybrain import *
from pybrain.datasets import SupervisedDataSet
from bs4 import BeautifulSoup
import re
import collections


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
	fp=open(pageName,"r")
	bs=BeautifulSoup(fp.read(),"html.parser")
	contents=[article.text for article in bs.findAll("article")]
	bagsofwords = [collections.Counter(re.findall(r'\w+', txt)) for txt in contents]
	wordCounter = sum(bagsofwords, collections.Counter())
	#I need to iterated on differentWords to create a list with 0 or de number on the COunter
	return tuple(wordCounter)
	

for pageName in d:
	pageRank=d[pageName]
	dataSet.addSample(getBagOfWords(pageName),pageRank)


#this is a preliminar study. Because normally we need two divisions : training set and verify set

from pybrain.supervised.trainers import BackpropTrainer

trainer = BackpropTrainer(net, dataSet)

error=trainer.trainUntilConvergence()

print error













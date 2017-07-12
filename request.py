#!/bin/python2

#__author__ = 'Luis Felipe'
import sys

from bs4 import BeautifulSoup # $ pip install beautifulsoup4


#url = sys.argv[1]
soup = BeautifulSoup(open(sys.argv[1]),"lxml")
print(soup.title)

#
#for text in soup.find_all('p'):
#    print(text.string)
#print(soup.p)

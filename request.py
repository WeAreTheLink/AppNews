import sys

from bs4 import BeautifulSoup # $ pip install beautifulsoup4

soup = BeautifulSoup(open(sys.argv[1]),"lxml")
palavras= soup.title.string
for plavavra in palavras:
    palavra=palavra.encode("cp1250")
    print (palavra.decode('unicode_escape').encode('ascii','ignore'))
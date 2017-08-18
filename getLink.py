import sys
from bs4 import BeautifulSoup # $ pip install beautifulsoup4
      

try:
	soup = BeautifulSoup(open(sys.argv[1]),"html.parser")
	for link in soup.findAll('a'):
		print (link.get('href'))
except IndexError:
	print("Don't have the path of file\n", file=sys.stderr)




#cat $1 | grep -Po '(?<=href=")[^"]*' | awk '$0 !~ /javascript|privacidade/'


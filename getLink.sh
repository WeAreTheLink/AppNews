import sys
import bs4

fp = open(sys.arv[1],"r")




cat $1 | grep -Po '(?<=href=")[^"]*' | awk '$0 !~ /javascript|privacidade/'


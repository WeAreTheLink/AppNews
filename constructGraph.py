
import os

def isExtern (link):
	return link.startswith("http") or link.startswith("https")
	

def normalize(destination,page):
	if (isExtern(destination)):
		destination=destination.replace("https://","",0).replace("http://","",0)
		return destination
	else:
		destination="./" + page + destination
		return os.path.abspath(destination)

for filename in glob.iglob('./**/*.html', recursive=True):
	p = subprocess.Popen(["./getLink.py",filename],stdout=subprocess.PIPE)
        for line in p.stdout.readlines():
		atual=normalize(destination,page)
		print(page+" "+atual)

#!/bin/bash


#input : target page
#description :
#	destination - the destination of link
#	page - the origin
#output : the realpath destination


#function normalize()
#{
#	destination=$1;
#	page=$2;
#	if [ echo $destination | grep "^(http|https)"]; #extern link
#	then
#		echo $destination | sed 's%^(http|https)://%%g' | read v_target
#		echo $v_target
#	else #intern link
#		destination=`echo $page $destination`
#		destination=`echo $destination | realpath`
#		echo $destination
#	fi;
#}


#for pag in `find . -type f -name "*html"`
#do
#	for target in `./getLink.sh $pag`
#	do
#		normalize $target $page | read atual
#		echo $pag $atual
#	done
#done | tee grafo

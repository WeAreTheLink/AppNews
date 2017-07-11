#!/bin/bash


#input : target page
#description :
#	destination - the destination of link
#	page - the origin
#output : the realpath destination


function normalize()
{
	echo $1
}


for pag in `find . -type f -name "*html"`
do
	for target in `./getLink.sh $pag`
	do
		normalize $target $page | read atual
		if [ $! ]; then
			echo $pag $atual
		fi
	done
done | tee grafo

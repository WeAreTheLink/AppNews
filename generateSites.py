
fp=open("sites","r")
for line in fp:
	first,second = line.strip(' ')
	category = second.strip(',')
	for categories in category:
		print (first,"/",categories)




#!/bin/bash

#this program is free software, please, don't be a bad person, respect the four freedoms

#cat sites | while read -r i
#do
#	first=`echo $i | cut -d' ' -f1`;
#	second=`echo $i | cut -d' ' -f2 | sed 's/,/ /g'`;
#	for j in $second;
#	do
#		echo $first/$j;
#	done;
#done

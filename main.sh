#!/bin/bash

for f in video/*.flv
do 
	echo "$f"
	./uploadVideo --file $f --title `basename $f`
	rm $f
done
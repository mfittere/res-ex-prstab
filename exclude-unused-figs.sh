#!/bin/bash

for image_file in $(ls *.png)
do
    occ=`grep $image_file tmp-file-list.txt -c`
#    echo $image_file $occ
    if [ "$occ" -eq "0" ]
    then
	echo "File $image_file is NOT in use."
	cp $image_file tmp/
	git rm $image_file
    fi
done

#!/bin/bash

DIRECTORY="originalPics/"

if [ ! -d "$DIRECTORY" ]; then
    echo " Oops ,It seems data not downloaded properly !"
    exit 1;
fi

#dealing FDDB-fold-01-ellipseList.txt;
#where there are 01~10 list need to process
# python anno2xml.py FDDB-fold-01-ellipseList.txt;
for i in $(seq 10)
do
    echo "[FDDB] Processing $i-th List";
    if (( i<10 ));then
         python pyxml/anno2xml.py --ellipse_list_file originalPics/FDDB-folds/FDDB-fold-0$i-ellipseList.txt;
    else
         python pyxml/anno2xml.py --ellipse_list_file originalPics/FDDB-folds/FDDB-fold-$i-ellipseList.txt;
    fi
done

python randomSet.py FDDB_2010 0.9

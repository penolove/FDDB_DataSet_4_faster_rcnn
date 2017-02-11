wget http://tamaraberg.com/faceDataset/originalPics.tar.gz
if [ -d originalPics ];
then
    echo "dir alreday exist";
else
    mkdir originalPics;
fi;
tar -C originalPics  -zxf originalPics.tar.gz
wget http://vis-www.cs.umass.edu/fddb/FDDB-folds.tgz
tar -C originalPics  -zxf FDDB-folds.tgz

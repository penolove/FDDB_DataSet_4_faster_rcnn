# FDDB_DataSet_4_faster_rcnn


## Quick Start (if done, skip Step1, Step2)
```
pip install -r requiremnets.txt
make
```

## Step1: get datas from FDDB
```
./get_data.sh
```
this should downloads originalPics.tar.gz(~500MB), and FDDB-folds.tgz from FDDB
and Checksum test ,if pass -> unzip tar.gz  into originalPics directory.

if link fails : download from  FDDB website 
http://vis-www.cs.umass.edu/fddb/


if always checksum fails :

```
wget http://tamaraberg.com/faceDataset/originalPics.tar.gz 
wget http://vis-www.cs.umass.edu/fddb/FDDB-folds.tgz

mkdir originalPics;
tar -C originalPics  -zxf originalPics.tar.gz
tar -C originalPics  -zxf FDDB-folds.tgz
```

## Step2: create data set that can be used in [pyfaster-rcnn](https://github.com/rbgirshick/py-faster-rcnn)
```
./generate_FDDB_2010.sh
```
which will convert the FDDB data into the format used for pyfaster-rcnn



## Finally: using labelImg to test if create properly
you can use labelImg to see if it deals properly(This is god dame awesome)
https://github.com/tzutalin/labelImg 
![alt tag](https://raw.githubusercontent.com/penolove/FDDB_DataSet_4_faster_rcnn/master/FDDB.png)



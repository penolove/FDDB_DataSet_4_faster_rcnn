# FDDB_DataSet_4_faster_rcnn

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


## Step2: create data set that can be used in pyfaster-rcnn
```
cd pyxml;
./runit.sh;
```
this will create FDDB_2010 directory
and JPEGImages/Annotation directory inside FDDB_2010

runit.sh contains:
```
python anno2xml.py FDDB-fold-01-ellipseList.txt;
python anno2xml.py FDDB-fold-02-ellipseList.txt;
python anno2xml.py FDDB-fold-03-ellipseList.txt;
....
```
which FDDB-fold-01-ellipseList.txt were in the originalPics/FDDB-folds
you can check if the list are the same (01~10)


## Step3: using labelImg to test if create properly
you can use labelImg to see if it deals properly(This is god dame awesome)
https://github.com/tzutalin/labelImg 
![alt tag](https://raw.githubusercontent.com/penolove/FDDB_DataSet_4_faster_rcnn/master/FDDB.png)



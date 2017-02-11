# FDDB_DataSet_4_faster_rcnn

# get datas from FDDB
```
./get_data.sh
```
this should downloads originalPics.tar.gz(~500MB), and FDDB-folds.tgz from FDDB
and unzip tar.gz into originalPics directory.

#create data set that can be used in pyfaster-rcnn
```
cd pyxml;
./runit.sh;
```
this will create FDDB_2010 directory
and JPEGImages/Annotation directory inside FDDB_2010

you can use labelImg to see if it deals properly(This is god dame awesome)
https://github.com/tzutalin/labelImg 




runit.sh contains:
```
python anno2xml.py FDDB-fold-01-ellipseList.txt;
python anno2xml.py FDDB-fold-02-ellipseList.txt;
python anno2xml.py FDDB-fold-03-ellipseList.txt;
....
```
which FDDB-fold-01-ellipseList.txt were in the originalPics/FDDB-folds
you can check if the list are the same (01~10)


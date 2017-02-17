ori_CheckSum=cf414253ac596cd858daae0cc321d793
folds_CheckSum=4cf9badc939a3398a0d6f3a3c8540f55
if [ -d originalPics ];
then
    echo "[FDDB] originalPics dir alreday exist";
else
    # ---- download originalPics.tar.gz ----
    FILE=originalPics.tar.gz
    #if file not exist
    if [ ! -f $FILE ]; then
        echo "[FDDB] Downloading originalPics.tar.gz ....."
        wget http://tamaraberg.com/faceDataset/originalPics.tar.gz 
    fi

    checksum=`md5sum $FILE | awk '{ print $1 }'`
    if [ ! "$checksum" = "$ori_CheckSum" ]; then 
        rm $File
        echo $checksum
        echo $folds_CheckSum
        echo "[FDDB] file $FILE : checksum error , need to rerun the script";
        exit 1;
    fi

    # ---------------------------------------

    # ---- download FDDB.tgz ----
    FILE=FDDB-folds.tgz
    #if file not exist
    if [ ! -f $FILE ]; then
        echo "[FDDB] Downloading FDDB-folds.tgz ....."
        wget http://vis-www.cs.umass.edu/fddb/FDDB-folds.tgz
    fi

    checksum=`md5sum $FILE | awk '{ print $1 }'`
    if [ ! "$checksum" = "$folds_CheckSum" ]; then 
        rm $FILE
        echo $checksum
        echo $folds_CheckSum
        echo "[FDDB] file $FILE : checksum error , need to rerun the script";
        exit 1;
    fi

    echo "[FDDB] Making originalPics , uncompress files ..."
    mkdir originalPics;
    tar -C originalPics  -zxf originalPics.tar.gz
    tar -C originalPics  -zxf FDDB-folds.tgz

fi;

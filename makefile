all:
	./get_data.sh
	./generate_FDDB_2010.sh
clean:
	echo "time to clean produced dirs/files"
	# rm -rf originalPics/	
	rm -rf FDDB_2010
	rm -f FDDB-folds.tgz
	rm -f originalPics.tar.gz

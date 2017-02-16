from random import shuffle
import glob
import sys
import os.path


if __name__=='__main__':
    if len(sys.argv) ==2 :
         dataset_name=sys.argv[1] 
         #Ratio split the training set / data set.
         trainRatio=0.9 
    elif len(sys.argv)==3:
         dataset_name=sys.argv[1] 
         trainRatio=float(sys.argv[2])
    else:
        print "usage : python randomSet.py dataset_name [trainXtest ratio]"
        sys.exit(0)

    target_dir = os.path.join(os.getcwd(), 'FDDB_2010')
    target_dir_ImSets = os.path.join(target_dir,'ImageSets')
    target_dir_ImSets_Main = os.path.join(target_dir_ImSets,'Main')
    target_dir_Anno = os.path.join(target_dir,'Annotations')

    if not os.path.exists(target_dir):
        print("DataSet doesn't exit, you should check if anno2xml.py runs properly")
        sys.exit(0)

    if not os.path.exists(target_dir_ImSets):
        os.makedirs(target_dir_ImSets)

    if not os.path.exists(target_dir_ImSets_Main):
        os.makedirs(target_dir_ImSets_Main)


    fileID=glob.glob(os.path.join(target_dir_Anno, "*.xml"))
    xml_list=[i.split('/')[-1].replace('.xml','') for i in fileID]

    shuffle(xml_list)
    trainSize=int(len(xml_list)*trainRatio)

    #train
    print "Training set creating..."
    f=open(os.path.join(target_dir_ImSets_Main , 'trainval.txt'),'w')
    for i in xml_list[:trainSize]:
        f.write(i+'\n')
    f.close()
    print "Done!"

    #test
    print "Testing set creating..."
    f=open(os.path.join(target_dir_ImSets_Main , 'test.txt'), 'w')
    for i in xml_list[trainSize:]:
        f.write(i+'\n')
    f.close()
    print "Done!"


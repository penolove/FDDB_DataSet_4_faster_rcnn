
from lxml import etree
import sys
import cv2
import math
import glob
import os.path


# target_check exist
target_dir=os.path.join(os.getcwd(), 'FDDB_2010')
target_dir_Jpg=os.path.join(target_dir,'JPEGImages')
target_dir_Ana=os.path.join(target_dir,'Annotations')

if not os.path.exists(target_dir):
    os.makedirs(target_dir)   

if not os.path.exists(target_dir_Jpg):
    os.makedirs(target_dir_Jpg)

if not os.path.exists(target_dir_Ana):
    os.makedirs(target_dir_Ana)   

target_dir_Jpg_set=os.path.join(target_dir_Jpg,'*.jpg')
cur_ind=0
outfileID=len(glob.glob(target_dir_Jpg_set))


def img2xml(path,objects,shape):
    root = etree.Element("annotation")
    folder = etree.SubElement(root, "folder")
    filename = etree.SubElement(root, "filename")
    source = etree.SubElement(root, "source")
    databases = etree.SubElement(source, "database")

    folder.text = "VOC2007"
    filename.text = str(path).zfill(6)
    databases.text = "FDDB"

    size = etree.SubElement(root, "size")
    width = etree.SubElement(size,"width")
    height = etree.SubElement(size,"height")
    depth = etree.SubElement(size,"depth")
    depth.text = str(shape[2])
    width.text = str(shape[1])
    height.text = str(shape[0])

    obj_count=0
    for obj in objects:
        #object
        obj=[float(i) for i in obj.split()]
        #the smallest circumscribed parallelogram
        #[link] https://github.com/nouiz/lisa_emotiw/blob/master/emotiw/common/datasets/faces/FDDB.py
        maj_rad = obj[0]
        min_rad = obj[1]
        angle = obj[2]
        xcenter = obj[3]
        ycenter = obj[4]
        cosin = math.cos(math.radians(-angle))
        sin = math.sin(math.radians(-angle))

        x1 = cosin * (-min_rad) - sin * (-maj_rad) + xcenter
        y1 = sin * (-min_rad) + cosin * (-maj_rad) + ycenter
        x2 = cosin * (min_rad) - sin * (-maj_rad) + xcenter
        y2 = sin * (min_rad) + cosin * (-maj_rad) + ycenter
        x3 = cosin * (min_rad) - sin * (maj_rad) + xcenter
        y3 = sin * (min_rad) + cosin * (maj_rad) + ycenter
        x4 = cosin * (-min_rad) - sin * (maj_rad) + xcenter
        y4 = sin * (-min_rad) + cosin * (maj_rad) + ycenter
        wid=[x1,x2,x3,x4]
        hei=[y1,y2,y3,y4]
        xmin_ = int(min(wid))
        xmax_ = int(max(wid))
        ymin_ = int(min(hei))
        ymax_ = int(max(hei))
        
        # check if out of box
        if(xmin_ >0 and ymin_>0 and xmax_<shape[1] and ymax_<shape[0]):
            obj_count+=1
            object_=etree.SubElement(root, "object")
            name=etree.SubElement(object_, "name")
            name.text="face"
            pose=etree.SubElement(object_, "pose")
            pose.text="Unspecified"
            truncated=etree.SubElement(object_, "truncated")
            truncated.text="0"
            difficult=etree.SubElement(object_, "difficult")
            difficult.text="0"
            # bndbox
            bndbox=etree.SubElement(object_, "bndbox")
            xmin=etree.SubElement(bndbox,"xmin")
            ymin=etree.SubElement(bndbox,"ymin")
            xmax=etree.SubElement(bndbox,"xmax")
            ymax=etree.SubElement(bndbox,"ymax")
            xmin.text = str(xmin_)
            ymin.text = str(ymin_)
            xmax.text = str(xmax_)
            ymax.text = str(ymax_)
    if obj_count>0:
        et = etree.ElementTree(root)
        Ana_write2xml = os.path.join(target_dir_Ana, path+".xml")
        et.write( Ana_write2xml, pretty_print=True)
        return True
    else: 
        return False

def face_box_wh(path,objects,shape):
    obj_count=0
    wh=list()
    for obj in objects:
        #object
        obj=[float(i) for i in obj.split()]
        #the smallest circumscribed parallelogram
        #[link] https://github.com/nouiz/lisa_emotiw/blob/master/emotiw/common/datasets/faces/FDDB.py
        maj_rad = obj[0]
        min_rad = obj[1]
        angle = obj[2]
        xcenter = obj[3]
        ycenter = obj[4]
        cosin = math.cos(math.radians(-angle))
        sin = math.sin(math.radians(-angle))

        x1 = cosin * (-min_rad) - sin * (-maj_rad) + xcenter
        y1 = sin * (-min_rad) + cosin * (-maj_rad) + ycenter
        x2 = cosin * (min_rad) - sin * (-maj_rad) + xcenter
        y2 = sin * (min_rad) + cosin * (-maj_rad) + ycenter
        x3 = cosin * (min_rad) - sin * (maj_rad) + xcenter
        y3 = sin * (min_rad) + cosin * (maj_rad) + ycenter
        x4 = cosin * (-min_rad) - sin * (maj_rad) + xcenter
        y4 = sin * (-min_rad) + cosin * (maj_rad) + ycenter
        wid=[x1,x2,x3,x4]
        hei=[y1,y2,y3,y4]
        xmin_ = int(min(wid))
        xmax_ = int(max(wid))
        ymin_ = int(min(hei))
        ymax_ = int(max(hei))
        
        # check if out of box
        if(xmin_ >0 and ymin_>0 and xmax_<shape[1] and ymax_<shape[0]):
            obj_count+=1
            wh.append([xmax-xmin,ymax-ymin])
    if obj_count>0:
        return wh
    else: 
        return list()

# the annotation files path
FDDB_folds=os.path.join("..",'originalPics','FDDB-folds')
originalPics_folds=os.path.join("..",'originalPics')

if __name__=="__main__":
    # you need to modify the path_img below
    # and the FDDB-fold-were assign by your own
    if len(sys.argv) < 2:
        ellipseList=os.path.join(FDDB_folds,'FDDB-fold-01-ellipseList.txt')
    elif len(sys.argv)==2:
        ellipseList=os.path.join(FDDB_folds,sys.argv[1])
    else:
        print "usage : python example.py [ellipseList]"
        sys.exit(0)

    current_file=open(ellipseList,'r')
    image_with_target=[i.replace('\n','') for i in current_file.readlines()]
    current_file.close()

    while (cur_ind<len(image_with_target)):
        """ since the format of the string is :
        (2 object in 2002/08/02/big/img_769)
        2
        58.887348 37.286244 1.441974 88.083450 78.409537  1
        60.381076 40.303691 1.377522 260.502940 102.769525  1
        2002/08/02/big/img_760
        (1 object in 2002/08/07/big/img_1453)
        1
        67.995400 38.216200 -1.559920 208.966471 109.764400  1
        2002/08/07/big/img_1453
        """
        path_img = os.path.join(originalPics_folds,image_with_target[cur_ind]+'.jpg')
        img = cv2.imread(path_img) 
        cur_ind+=1
        len_obj=int(image_with_target[cur_ind])
        cur_ind+=1
        objects=image_with_target[cur_ind:cur_ind+len_obj]
        cur_ind+=len_obj
        path=str(outfileID).zfill(6)
        if(img2xml(path,objects,img.shape)):
            img_path2write = os.path.join(target_dir_Jpg,path+".jpg")
            cv2.imwrite(img_path2write, img)
            outfileID+=1


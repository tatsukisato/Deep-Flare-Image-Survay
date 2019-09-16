#!/home/tsato/anaconda3/bin/python

#
#.fits fileをds9を使用して、jpg形式に保存する
#入力はfits/ディレクトリ
#出力はjpeg/ディレクトリ
#

def ds9():
    import pyds9
    import os
    import time
    PWD=os.getcwd()
    new_dir_path = PWD + "/" +'jpeg'
    dir_name = "fits"
    file_list = os.listdir(PWD + "/" + dir_name)

    if not os.path.exists(new_dir_path):
     os.mkdir(new_dir_path)
     d = pyds9.DS9()
     d.set("view colorbar no")
     d.set("cmap value 1 .5")
     d.set("smooth")
     d.set("smooth radius 5")
     d.set("smooth sigma 2.5")
     time.sleep(2)
     for i in file_list:
        root, ext = os.path.splitext(i)
        d.set("file %s/%s"%(dir_name,i))
        d.set("saveimage jpeg %s/%s.jpg 100"%(new_dir_path,root))
     d.set("exit")
    else:
        print ("jpeg directory exist!!")

if __name__ == '__main__':
    ds9()

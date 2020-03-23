#!/home/tsato/anaconda3/bin/python

#
#make_fits.pyで生成したディレクトリ内の.fitsデータに対して、ファイル名をMJDに変換する
#
#

def work():
    import os
    import datetime
    import glob
    import shutil

    #処理を行うディレクトリーを指定
    PWD=os.getcwd()
    dir_name = "fits"
    file_list = os.listdir(PWD +"/"+ dir_name)
    for i in file_list:
        filename = os.path.basename(i)
        sep_path = os.path.splitext(filename)
        num=sep_path[0].split("_")[0]
        time=sep_path[0].split("_")[1]
        stime=int(time.split("-")[0])
        etime=int(time.split("-")[1])
        std = datetime.timedelta(seconds = stime)
        sday=std.days
        ssec=std.seconds/(3600*24)
        s=sday + ssec
        s=round(s,6)
        etd = datetime.timedelta(seconds = etime)
        eday=etd.days
        esec=etd.seconds/(3600*24)
        e=eday + esec
        e=round(e,6)
        MJD_0 = 51544  #2000/01/01
        sMJD = MJD_0 + s
        eMJD = MJD_0 + e
        new_name="%03d_%f-%f.fits"%(int(num),float(sMJD),float(eMJD))
        os.rename(PWD+"/"+dir_name + "/" + filename,PWD+"/"+dir_name + "/" + new_name)

if __name__ == '__main__':
    work()

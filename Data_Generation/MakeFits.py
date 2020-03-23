#!/home/tsato/anaconda3/bin/python

#
#MAXI画像データ*rbn.img*から1orbitごとのimageをfits fileとして切り出す
#fits/ディレクトリを生成し.fits形式で出力
#

def make_fits():
    import os
    import glob
    import astropy.io.fits as pyfits
    import shutil


    PWD=os.getcwd()
    new_dir_path = PWD + "/" +'fits'
    FNAME=glob.glob('*3.0-10.0keV_rbn.img*')[0]
    imgdata=pyfits.open(FNAME)[0].data
    hpxdata=pyfits.open(FNAME)[1].data
    if not os.path.exists(new_dir_path):
        for i in range(imgdata.shape[0]):
            start=hpxdata["START"][i]
            stop=hpxdata["STOP"][i]
            OUTFNAME="%03d_%d-%d.fits"%(i+1, int(start), int(stop))
            img=imgdata[i]
            hdu=pyfits.PrimaryHDU(img)
            hdulist = pyfits.HDUList([hdu])
            hdulist.writeto(OUTFNAME,overwrite=True)
        os.mkdir(new_dir_path)
        for i in glob.glob('./*.fits'):
            shutil.move(i, "./fits/" )
    else:
        print ("fits Directory exist!!")
make_fits()

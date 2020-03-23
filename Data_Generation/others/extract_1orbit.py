#!/home/tsato/anaconda3/bin/python

def extract():
    import os
    import glob
    import pandas as pd
    import shutil

    PWD=os.getcwd()
    filename = glob.glob('*.dat')[0]
    df=pd.read_csv(PWD +"/"+filename,sep='\s+',header=None)
    val = float(0.0667)
    crab = (df[df[2] > float(val)])
    crab = crab.reset_index(drop=True)

    ########################################################

    dir = "fits"
    dir = PWD + "/" + dir + "/"
    a_df = pd.DataFrame()
    for f in glob.glob(dir+ '*.fits'):
        i=os.path.split(f)[1]
        a=i.split("_")
        b=a[1].split("-")
        c=b[1].rsplit(".",1)
        s=[[int(a[0]),float(b[0]),float(c[0])]]
        a_df = a_df.append(s,ignore_index=True)
    b_df = a_df.sort_values([0])
    b_df = b_df.reset_index(drop=True)

    #######################################################

    event=(PWD + "/" + "event")
    os.mkdir(event)
    n=0
    for x in range(crab.shape[0]):
     val=crab[0][x]
     m=n
     for i,v in b_df[m:].iterrows():
            if (v[1] < val) & (v[2] > val):
                n=i+1
                file01=glob.glob(dir+ '%03d_*' % n)[0]
                if (os.path.exists(str(file01)) ) :
                                        shutil.copy(str(file01),event)
                else:pass
            else:
                val=crab[0][x]+float(0.001)
                if (v[1] < val) & (v[2] > val):
                    n=i+1
                    file01=glob.glob(dir+ '%03d_*' % n)[0]
                    if (os.path.exists(str(file01)) ) :
                        shutil.copy(str(file01),event)
                    else:pass

                else:
                    val=crab[0][x]+float(0.001)
                    if (v[1] < val) & (v[2] > val):
                        n=i+1
                        file01=glob.glob(dir+ '%03d_*' % n)[0]
                        if (os.path.exists(str(file01)) ) :
                            shutil.copy(str(file01),event)
                        else:pass
                    else:pass
extract()

def resetIndex():
    import pandas as pd
    import glob
    import os

    PWD=os.getcwd()
    event=(PWD + "/" + "event")
    c_df = pd.DataFrame()
    for f in glob.glob(event + "/" + '*.fits'):
        i=os.path.split(f)[1]
        a=i.split("_")
        s=[[int(a[0]),str(a[1])]]
        c_df = c_df.append(s,ignore_index=True)
    c_df = c_df.sort_values([0])
    c_df = c_df.reset_index(drop=False)
    for n in range(c_df.shape[0]):
            name=c_df[1][n]
            old=(event + "/" +"%03d_%s"%(c_df[0][n],name))
            new=(event + "/" +"%03d_%s"%(n+1,name))
            os.rename(old,new)
resetIndex()

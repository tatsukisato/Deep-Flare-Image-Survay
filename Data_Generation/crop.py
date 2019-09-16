#!/home/tsato/anaconda3/bin/python

#
#jpeg/内の.jpegファイルに対して、トリミングを行う
#出力はcrop/

def crop():
    from PIL import Image
    import os
    PWD=os.getcwd()
    input_dir = "jpeg"
    output_dir = "crop"

    file_list = os.listdir(PWD + "/" + input_dir)

    if not os.path.exists(output_dir):
        os.mkdir(output_dir)
        for i in file_list:
         im = Image.open(input_dir + "/" +i)
         im_crop = im.crop((316, 188, 422, 294))
         im_crop.save(output_dir +"/"+i, quality=100)
    else:
        print ("crop directory exist !!")

if __name__ == '__main__':
    crop()

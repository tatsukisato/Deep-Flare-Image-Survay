#!/usr/bin/env python
# coding: utf-8

# In[1]:


import tensorflow as tf
from keras.models import load_model
import os
from keras.preprocessing.image import img_to_array, load_img
from keras.models import load_model
import numpy as np
from PIL import Image
import pandas as pd
pd.set_option('display.max_rows', 500)

from keras import backend as K
K.clear_session()
config = tf.ConfigProto(gpu_options=tf.GPUOptions(allow_growth=True))
sess = tf.Session(config=config)
K.set_session(sess)


# In[2]:


#学習済みモデルの読込
model_file_name='./model_.05-0.04.hdf5'
model=load_model(model_file_name)
model.summary()


# In[3]:


#推測するディレクトリーを指定
#print('target name:')
#print(os.listdir('../../images/1orbit/3-10keV/test/'))
#TARGET_DIR = input('>>> ')
#print('predict directory:')
#print(os.listdir('../../images/1orbit/3-10keV/test'+'/' + TARGET_DIR+'/'))
#IMAGE_DIR = input('>>> ')
#images = os.listdir('../../images/1orbit/3-10keV/test/'+TARGET_DIR+'/'+IMAGE_DIR)
#TextName = TARGET_DIR + "_" +IMAGE_DIR + "_" +'1orb.txt'

print('predict directory:')
IMAGE_DIR = input('>>> ')
images = os.listdir(IMAGE_DIR)

#print("1orbit:" + str(len(images)))


# In[4]:


#val以上の評価
df = []
for jpeg_name in images:
    img_path = (jpeg_name)
    img = img_to_array(load_img(IMAGE_DIR + '/' + img_path, target_size=(32,32)).convert('L'))
    img_nad = img_to_array(img)/255	    #0-1に変換
    img_nad = img_nad[None, ...]	    #四次元配列に
    label=['background','flare']
    pred = model.predict(img_nad, batch_size=1, verbose=0)
    score = np.max(pred)
    pred_label = label[np.argmax(pred[0])]
    val = 0.99
    if score > val and pred_label == "flare":
        #print (jpeg_name)
        #print('name:',pred_label)
        #print('score:',score)
        #print('\n')
        a=jpeg_name.split("_")
        list=[int(a[0]),jpeg_name,score]     
        df.append(list)
        #df = df.to_csv(jpeg_name,mode='a')
result = pd.DataFrame(df)
result = result.sort_values([0])
result = result.reset_index(drop=True)
result = result.iloc[:,1:3]
print(result)


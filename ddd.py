import streamlit as st
import pandas as pd
from PIL import Image
import numpy as np
import PIL.ExifTags as Exiftags


st.title('画像から緯度・経度取得')
#img = st.file_uploader('写真アップロード',type='jpg')
im = Image.open('DSC_0106.JPG')
#st.image(im)
#if img is True:
#    exif = img._getexif()
##sデータの一覧
#    for id,value in exif.items():
#        st.write(id,value)
#
def get_gps(frame):
#画像ファイルを開く
    im = Image.oepn(frame)
    exif = {
        Exiftags.TAGS[k]:v
        for k ,v in im_getexif().items()
            if k in Exiftags.TAGS
    }
#GPS情報を得る
    gps_tags = exif['GPSinfo']
    gps = {
        ExifTags.GPSTAGS.get(t,t):gps_tags[t]
        for i in gps_tags
    }
 #緯度経度情報を得る
 
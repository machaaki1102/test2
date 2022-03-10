import streamlit as st
import pandas as pd
from pillow import Image
import numpy as np
import pillow.exiftags as Exiftags

st.titile('画像から緯度・経度取得')
img = st.file_uploader('写真アップロード',type='jpg')
exif = img._getexif()

#データの一覧
for id,value in exif.items():
    st.write(id,value)
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
               
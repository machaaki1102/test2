import streamlit as st
import pandas as pd
from PIL import Image
import numpy as np
import PIL.ExifTags as ExifTags


#img　に入った画像の経度緯度を取る。

#parts
def chape(img):
#  img = Image.open('IMG_1010.JPG')
  exif = {
    ExifTags.TAGS[k]: v
    for k, v in img._getexif().items()
    if k in ExifTags.TAGS
  }
# GPS情報を得る --- (*2)
  gps_tags = exif["GPSInfo"]
  gps = {
    ExifTags.GPSTAGS.get(t, t): gps_tags[t]
    for t in gps_tags
  }
  lat = float(gps["GPSLatitude"][0])+float(gps["GPSLatitude"][1]/100)+float(gps["GPSLatitude"][2]/10000)
  lon = float(gps["GPSLongitude"][0])+float(gps["GPSLongitude"][1]/100)+float(gps["GPSLongitude"][2]/10000)
  return lat,lon

#body
st.title('画像から緯度・経度取得')
img = Image.open('IMG_1010.JPG')
#img = st.file_uploader('写真アップロード',type='jpg')
if img:
  lat,lon = chape(img)
  st.write(f'経度:{lat}緯度:{lon}')
#st.write(f'経度:{lat}緯度:{lon}')
#写真表示
#st.image(im)


#EXIF情報をとる。
#exif = img._getexif()
#for id,value in exif.items():
#    st.write(id,value)
#if img is True:
#    exif = img._getexif()
##sデータの一覧
#    for id,value in exif.items():
#        st.write(id,value)
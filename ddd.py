import streamlit as st
import pandas as pd
from PIL import Image
import numpy as np
import PIL.ExifTags as ExifTags

#写真から緯度経度をとる。
def get_gps(fname):
    # 画像ファイルを開く --- (*1)
    im = Image.open(fname)
    # EXIF情報を辞書型で得る
    exif = {
        ExifTags.TAGS[k]: v
        for k, v in im._getexif().items()
        if k in ExifTags.TAGS
    }
    # GPS情報を得る --- (*2)
    gps_tags = exif["GPSInfo"]
    gps = {
        ExifTags.GPSTAGS.get(t, t): gps_tags[t]
        for t in gps_tags
    }
    # 緯度経度情報を得る --- (*3)
    # 分数を度に変換
    def conv_deg(v):
        d = float(v[0][0]) / float(v[0][1])
        m = float(v[1][0]) / float(v[1][1])
        s = float(v[2][0]) / float(v[2][1])
        return d + (m / 60.0) + (s / 3600.0)
    lat = conv_deg(gps["GPSLatitude"])
    lat_ref = gps["GPSLatitudeRef"]
    if lat_ref != "N": lat = 0 - lat
    lon = conv_deg(gps["GPSLongitude"])
    lon_ref = gps["GPSLongitudeRef"]
    if lon_ref != "E": lon = 0 - lon
    return lat, lon

#

im = Image.open('IMG_1010.JPG')
exif = {
  ExifTags.TAGS[k]: v
  for k, v in im._getexif().items()
  if k in ExifTags.TAGS
}
# GPS情報を得る --- (*2)
gps_tags = exif["GPSInfo"]
gps = {
  ExifTags.GPSTAGS.get(t, t): gps_tags[t]
  for t in gps_tags
}

st.write(gps)
st.write(gps["GPSLatitude"][0][0])

#body
st.title('画像から緯度・経度取得')
#img = st.file_uploader('写真アップロード',type='jpg')
lat,lon = get_gps('IMG_1010.JPG')
st.wite(f'経度:{lat}緯度:{lon}')
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
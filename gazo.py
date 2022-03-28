import streamlit as st
import pandas as pd
from PIL import Image
import numpy as np
import PIL.ExifTags as ExifTags
import plotly.express as px
import os
import urllib.request
import time
#img　に入った画像の経度緯度を取る。
#parts
def chape(img): #imgは、JPEGそのまま入れた。
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
  lat = float(gps["GPSLatitude"][0])+float(gps["GPSLatitude"][1]/60)+float(gps["GPSLatitude"][2]/3600)
  lon = float(gps["GPSLongitude"][0])+float(gps["GPSLongitude"][1]/60)+float(gps["GPSLongitude"][2]/3600)
  date = gps["DateTimeOriginal"]
#  lat = float(gps["GPSLatitude"][0])+float(gps["GPSLatitude"][1]/100)
#  lon = float(gps["GPSLongitude"][0])+float(gps["GPSLongitude"][1]/100)
  return lat,lon

#
#body
#st.write(os.getcwd())
st.header('画像から緯度・経度取得')
#st.write('※exif情報(位置情報がないものはエラーになります。')
#img = Image.open('IMG_1010.JPG')
img = st.file_uploader('写真から緯度経度を取得出来、地図上で表します。')
#img = st.camera_input('Take a picure')

if img is not None:
  img  = Image.open(img)
  lat,lon = chape(img)
  st.write(f'経度:{"{:.4f}".format(lat)}緯度:{"{:.4f}".format(lon)}')
  st.write(date)

#マップングする。
  df9 = pd.DataFrame(np.array((lat,lon)).reshape(1,2),columns=['lat','lon'])
  px.set_mapbox_access_token('pk.eyJ1IjoibWFjaGFha2kiLCJhIjoiY2wwamVyanUxMGJ2bTNqcjU4dGZtdWdoZyJ9.Vk57Qp-OPGYFkGdgTB6iYw')
  fig9 = px.scatter_mapbox(
  data_frame=df9,
  lat="lat",
  lon="lon",
  size="lat",
  size_max=10,
  zoom=5,
  height=500)
  fig9.update_layout(margin={"r":0,"t":0,"l":0,"b":0})
  fig9 = fig9.update_layout(mapbox_style='open-street-map')
  fig9

if img:
  csv = df9.to_csv()
#.encode('utf-8')
  st.download_button('緯度経度情報をダウンロード',
  data = csv,
  file_name = 'lat_lon.csv'
  )

#st.write(os.getcwd())
#st.write(img.name)
#画像の保存,挑戦中
#MG_PATH2 = 'https://github.com/machaaki1102/test2'
#file = st.file_uploader('画像をアップロードしてください.', type=['jpg', 'jpeg', 'png'])
##if img: 
#  with open(img.name, 'wb') as f:
#    f.write(img.getbuffer())
    
#IMG_PATH = "/app/test2/"
#def main():
#    st.markdown('# 画像を保存するデモ')
#    file = st.file_uploader('画像をアップロードしてください.', type=['jpg', 'jpeg', 'png'])
#    if file:
#        st.markdown(f'{file.name} をアップロードしました.')
#        img_path = os.path.join(IMG_PATH, file.name)
#        img_path2 = os.path.join(IMG_PATH2, file.name)
#       # 画像を保存する
#        with open(img_path2, 'wb') as f:
#            f.write(file.read())
#            st.write(img_path)
#        # 保存した画像を表示
#        img = Image.open(img_path)
#        st.image(img)#
#main()
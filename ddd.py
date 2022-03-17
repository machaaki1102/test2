import streamlit as st
import pandas as pd
from PIL import Image
import numpy as np
import PIL.ExifTags as ExifTags
import plotly.express as px
import os

#img　に入った画像の経度緯度を取る。ss
#parts
def chape(img):
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
#  lat = float(gps["GPSLatitude"][0])+float(gps["GPSLatitude"][1]/100)+float(gps["GPSLatitude"][2]/10000)
#  lon = float(gps["GPSLongitude"][0])+float(gps["GPSLongitude"][1]/100)+float(gps["GPSLongitude"][2]/10000)
  lat = float(gps["GPSLatitude"][0])+float(gps["GPSLatitude"][1]/100)
  lon = float(gps["GPSLongitude"][0])+float(gps["GPSLongitude"][1]/100)
  return lat,lon

#body
st.title('画像から緯度・経度取得')
#img = Image.open('IMG_1010.JPG')
#img = st.file_uploader('写真アップロード',type='jpg')
img = st.camera_input('Take a picure')

#if img is not None:
#  img = Image.open(img)
#  lat,lon = chape(img)
#  st.write(f'経度:{lat}緯度:{lon}')

#マップングする。
#  df9 = pd.DataFrame(np.array((lat,lon)).reshape(1,2),columns=['lat','lon'])
 # st.write(df9)
#  px.set_mapbox_access_token('pk.eyJ1IjoibWFjaGFha2kiLCJhIjoiY2wwamVyanUxMGJ2bTNqcjU4dGZtdWdoZyJ9.Vk57Qp-OPGYFkGdgTB6iYw')
 # df9 = pd.read_csv('covid19.csv')
#  fig9 = px.scatter_mapbox(
#   data_frame=df9,
#   lat="lat",
#   lon="lon",
#   size="lat",
#   size_max=10,
#   zoom=5,
#   height=500)
#  fig9.update_layout(margin={"r":0,"t":0,"l":0,"b":0})
#  fig9 = fig9.update_layout(mapbox_style='open-street-map')
#  fig9


#img = Image.open('IMG_5655.JPG')
#img = io.BytesIO(img)
#bytes_data = img.getvalue()
#st.write(bytes_data)
img = Image.open(img)
st.write(img._getexif().items())
exif = {
   ExifTags.TAGS[k]: v
   for k, v in img._getexif().items()
   if k in ExifTags.TAGS
}
st.write(exif)
  
lat,lon = chape(img)
st.write(lat,lon)
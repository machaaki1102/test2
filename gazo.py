import streamlit as st
import pandas as pd
from PIL import Image
import numpy as np
import PIL.ExifTags as ExifTags
import plotly.express as px
import os
import urllib.request
import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains


#img　に入った画像の経度緯度を取る。

#parts
def chape(img): #imgは、JPEGそのまま入れた。
  exif = {
    ExifTags.TAGS[k]: v
    for k, v in img._getexif().items()
    if k in ExifTags.TAGS
  }
  #st.write(exif)
  #date = exif["DateTimeOriginal"]
# GPS情報を得る --- (*2)
  gps_tags = exif["GPSInfo"]
  gps = {
    ExifTags.GPSTAGS.get(t, t): gps_tags[t]
    for t in gps_tags
  }
  lat = float(gps["GPSLatitude"][0])+float(gps["GPSLatitude"][1]/60)+float(gps["GPSLatitude"][2]/3600)
  lon = float(gps["GPSLongitude"][0])+float(gps["GPSLongitude"][1]/60)+float(gps["GPSLongitude"][2]/3600)
#  lat = float(gps["GPSLatitude"][0])+float(gps["GPSLatitude"][1]/100)
#  lon = float(gps["GPSLongitude"][0])+float(gps["GPSLongitude"][1]/100)
  return lat,lon

def click_by_position(driver, x, y) -> None:
    actions = ActionChains(driver)

    # MOVE TO TOP_LEFT (`move_to_element` will guide you to the CENTER of the element)
    whole_page = driver.find_element_by_id("map")
    actions.move_to_element_with_offset(whole_page, 0, 0)

    # MOVE TO DESIRED POSITION THEN CLICK
    actions.move_by_offset(x, y)
    actions.click()

    actions.perform()

def dojou():
  #borwer = webdriver.Chrome(executable_path='chromedriver.exe')
  url =f'https://soil-inventory.rad.naro.go.jp/figure.html?lat={lat}&lng={lon}&zoom=15'
  #borwer.get(url)
  st.write('site go:' + url)

def dsei():
  driver = webdriver.Chrome(executable_path='chromedriver.exe')
  url =f'https://soil-inventory.rad.naro.go.jp/figure.html?lat={lat}&lng={lon}&zoom=15'
  driver.get(url)
  time.sleep(2)
  driver.execute_script("window.scrollTo(0, 200)")  
  x = 5
  y = 85
  click_by_position(driver, x, y)
  time.sleep(2)
  popname = driver.find_element_by_id('popName')
  popExplain = driver.find_element_by_id('popExplain')
  st.write(
  popname.text,
  popExplain.text)

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
  #st.write(date)

#マッピング。
  df9 = pd.DataFrame(np.array((lat,lon)).reshape(1,2),columns=['lat','lon'])
  px.set_mapbox_access_token('pk.eyJ1IjoibWFjaGFha2kiLCJhIjoiY2wwamVyanUxMGJ2bTNqcjU4dGZtdWdoZyJ9.Vk57Qp-OPGYFkGdgTB6iYw')
  fig9 = px.scatter_mapbox(
  data_frame=df9,
  lat="lat",
  lon="lon",
  size="lat",
  size_max=10,
  zoom=10,
  height=300,
  width=360
  )
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
  
  st.button('URL土壌インベントリ―',on_click=dojou)
#  st.button('土壌インベントリ(土性）',on_click=dsei)

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
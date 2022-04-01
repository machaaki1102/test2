from selenium import webdriver
import time 
import os
from selenium.webdriver.common.by import By

browzer = webdriver.Chrome(executable_path='chromedriver.exe')

lat = 34.999418
lon= 134.990197
url =f'https://soil-inventory.rad.naro.go.jp/figure.html?lat={lat}&lng={lon}&zoom=15'
#url2 = 'https://soil-inventory.rad.naro.go.jp/figure.html?lat=34.999418&lng=134.990197&zoom=15'
browzer.get(url)
time.sleep(3)
a = browzer.find_element_by_id("map2Center").click()
#time.sleep(3)
#b = browzer.find_element_by_class_name('leaflet-container leaflet-touch leaflet-retina leaflet-fade-anim leaflet-grab leaflet-touch-drag leaflet-touch-zoom').click()
#a = browzer.find_element_by_class_name('leaflet-container leaflet-touch leaflet-retina leaflet-fade-anim leaflet-grab leaflet-touch-drag leaflet-touch-zoom')
#leaflet-container leaflet-touch leaflet-retina leaflet-fade-anim leaflet-grab leaflet-touch-drag leaflet-touch-zoom')
time.sleep(3)
#.click()
print(b.is_enabled())
#browzer.quit()


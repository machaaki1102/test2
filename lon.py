import stremalit as st
import pandas as pd
from pillow import Image
import numpy as np

img = st.file_uploader('写真アップロード',type='jpg')
exif = img_getexif()
for id,value in exif.items():
    st.write(id,value)
    
import streamlit as st 
import pandas as pd
import matplotlib
import matplotlib.pyplot as plt
import seaborn as sns
import os
from matplotlib.backends.backend_agg import RendererAgg

#gdp グラフ
#df4 = px.data.gapminder()
#st.write(df4.head())
#fig = px.scatter(df4, x="gdpPercap", y="lifeExp", size="pop",color="continent",hover_name="country",animation_frame="year")
#st.write(fig)
#url = 'https://raw.githubusercontent.com/holtzy/data_to_viz/master/Example_dataset/2_TwoNum.csv'
#df = pd.read_csv(url)
#st.write(df)

#configuration of the page
st.set_page_config(layout="wide")
#load dataframes
url = 'https://github.com/max-lutz/national-assembly/blob/main/data/df_dep.csv'
url2 = 'https://github.com/max-lutz/national-assembly/blob/main/data/df_polpar.csv'
df_dep = pd.read_csv(url)
df_pol_par = pd.read_csv(url2)
st.title('French national assembly vizualisation tool')
st.markdown("""
This app performs simple visualization from the open data from the french national assembly!
""")
st.write(df_dep)
st.write(df_pol_par)
import streamlit as st 
import pandas as pd
import matplotlib
import matplotlib.pyplot as plt
import seaborn as sns
import os
from matplotlib.backends.backend_agg import RendererAgg
import plotly.express as px

#gdp グラフ
#df4 = px.data.gapminder()
#st.write(df4.head())
#fig = px.scatter(df4, x="gdpPercap", y="lifeExp", size="pop",color="continent",hover_name="country",animation_frame="year")
#st.write(fig)
#url = 'https://raw.githubusercontent.com/holtzy/data_to_viz/master/Example_dataset/2_TwoNum.csv'
#df = pd.read_csv(url)
#st.write(df)

st.title('plotlyの使い方')
#px.data.tipsにいくつかデータが入っている
df = px.data.tips()
fig=px.sunburst(df,path = ['smoker','day','time','sex'],values='total_bill')
st.write(fig)

# kubo によるplotly講座
# https://scmopt.github.io/analytics/visualization.html

df1 = pd.read_csv("https://raw.githubusercontent.com/holtzy/data_to_viz/master/Example_dataset/1_OneNum.csv")
st.write(df1.head())

fig = px.histogram(df1, x="price", range_x=(0,3000),nbins=1000,opacity=0.5,marginal="violin") 
st.write(fig)

iris = px.data.iris()
st.write(iris.head())

df2 = pd.read_csv("https://raw.githubusercontent.com/holtzy/data_to_viz/master/Example_dataset/2_TwoNum.csv")
st.write(df2.head())

fig2 = px.scatter(df2, x="GrLivArea", y="SalePrice", marginal_y="rug", marginal_x="histogram")
st.write(fig2)

df3 = pd.read_csv("https://raw.githubusercontent.com/holtzy/data_to_viz/master/Example_dataset/3_TwoNumOrdered.csv",sep=" ")
st.write(df3.head())

fig3 = px.line(df3, x="date", y="value")
st.write(fig3)

df4 = px.data.gapminder()
st.write(df4.head())

st.title('GAP')
fig4 = px.scatter(df4, x="gdpPercap", y="lifeExp", size="pop",color="continent",hover_name="country",animation_frame="year")
fig4

df5 = pd.read_csv("https://raw.githubusercontent.com/holtzy/data_to_viz/master/Example_dataset/6_SeveralNum.csv")
st.write(df5.head())

st.title('相関の可視化')
fig5 = px.scatter_matrix(df5, 
                        dimensions=["mpg", "disp", "drat", "hp", "qsec", "wt"], 
                        color="gear")
fig5

df6 = pd.read_csv("https://raw.githubusercontent.com/holtzy/data_to_viz/master/Example_dataset/7_OneCatOneNum.csv")
st.write(df6.head())

fig6 = px.bar(df6,x='Country',y='Value')
fig6

df7 = pd.read_csv("https://raw.githubusercontent.com/holtzy/data_to_viz/master/Example_dataset/9_OneNumSevCatSubgroupOneObs.csv")
st.write(df7.head())

fig7 = px.bar(df7, x='Country', y='Value', color='TIME')
fig7

#mapbox
px.set_mapbox_access_token('pk.eyJ1IjoibWFjaGFha2kiLCJhIjoiY2wwamVyanUxMGJ2bTNqcjU4dGZtdWdoZyJ9.Vk57Qp-OPGYFkGdgTB6iYw')
df9 = pd.read_csv('covid19.csv')
fig9 = px.scatter_mapbox(df9,lat="lat", lon="lon",size="pop",color="pop",size_max=80,zoom=3, height=500)
fig9.update_layout(margin={"r":0,"t":0,"l":0,"b":0})
fig9

#df8 = pd.read_csv("https://raw.githubusercontent.com/holtzy/data_to_viz/master/Example_dataset/18_ListGPSCoordinatesWithValue.csv",sep=" ")
#st.write(df8.head())
#fig8 = px.scatter_mapbox(df8, lat="lat", lon="long", 
#                        size="pop",hover_name="name",zoom=5)
#fig8

df10 = px.data.gapminder()
st.write(df10.head())
fig10 = px.choropleth(df10, locations="iso_alpha", locationmode = "ISO-3", color="lifeExp", hover_name="country", animation_frame="year")
fig10

iris = px.data.iris()
fig11 = px.parallel_coordinates(iris,color='species_id')
fig11

tips = px.data.tips()
st.write(tips.head())
fig12 = px.parallel_categories(tips,color='size')
fig12

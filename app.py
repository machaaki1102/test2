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
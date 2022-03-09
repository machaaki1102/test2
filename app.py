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

import dash
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output

df2 = px.data.iris()
all_dims = ['sepal_length', 'sepal_width', 
            'petal_length', 'petal_width']

app = dash.Dash(__name__)

app.layout = html.Div([
    dcc.Dropdown(
        id="dropdown",
        options=[{"label": x, "value": x} 
                 for x in all_dims],
        value=all_dims[:2],
        multi=True
    ),
    dcc.Graph(id="splom"),
])

@app.callback(
    Output("splom", "figure"), 
    [Input("dropdown", "value")])
def update_bar_chart(dims):
    fig = px.scatter_matrix(
        df, dimensions=dims, color="species")
    return fig
    
st.write(fig)
#app.run_server(debug=True)
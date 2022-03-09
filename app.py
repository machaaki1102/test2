import streamlit as st
import pandas as pd
import plotly.express as px  # (version 4.7.0)

df4 = px.data.gapminder()
#st.write(df4.head())

fig = px.scatter(df4, x="gdpPercap", y="lifeExp", size="pop",color="continent",hover_name="country",animation_frame="year")
st.write(fig)
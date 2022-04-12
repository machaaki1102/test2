import streamlit as st
import pandas as pd

#データ
df = pd.read_csv('finished_data.csv',encoding='cp932')

#body
number_N = st.sidebar.slider('N',0,60)
number_P = st.sidebar.slider('P',0,60)
number_K = st.sidebar.slider('K',0,60)

long = len(df.index)
st.write(f'件数；{long}')
st.dataframe(df)

#st.number_input('Nの調整',0)

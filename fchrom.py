import streamlit as st
import pandas as pd

#データ
df = pd.read_csv('finished_data.csv',encoding='cp932')

#body
number_N = st.sidebar.slider('N',0,60)
puls_number_N = st.sidebar.numbar_input('N　adjustment')
number_P = st.sidebar.slider('P',0,60)
#puls_number_P = st.sidebar.input('P　adjustment')
number_K = st.sidebar.slider('K',0,60)

long = len(df.index)
st.write(f'ヒット件数:{long}')
st.dataframe(df)

#st.number_input('Nの調整',0)

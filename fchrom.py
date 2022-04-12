import streamlit as st
import pandas as pd

#データ
df = pd.read_csv('finished_data.csv',encoding='cp932')

#body

#sidebar
number_N = st.sidebar.slider('N',0,60)
puls_number_N = st.sidebar.number_input('N_adjustment')
number_P = st.sidebar.slider('P',0,60)
puls_number_P = st.sidebar.number_input('p_adjustment')
number_K = st.sidebar.slider('K',0,60)
puls_number_K = st.sidebar.number_input('K_adjustment')

#home
long = len(df.index)
st.write(f'ヒット件数:{long}')
st.dataframe(df)


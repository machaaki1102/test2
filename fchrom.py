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
n_amount_max = number_N + puls_number_N
n_amount_min = number_N - puls_number_N

#home
st.write(n_amount_max)
df  = df.query('@n_amount_min <= N <= @n_amount_max')

#df  = df.query('"n_amount_min" <= N <= "n_amount_max"')
#df = df[df['N'] == "n_amount"]
long = len(df.index)
st.write(f'ヒット件数:{long}')
st.dataframe(df)

import streamlit as st
import pandas as pd

#データ
df = pd.read_csv('finished_data.csv',index_col=0,encoding='cp932')

#body

#sidebar
col1, col2,col3 = st.sidebar.columns(3)
with col1:
    selected_N = st.sidebar.checkbox('N')
with col2:
    selected_P = st.sidebar.checkbox('P')
with col3:
    selected_K = st.sidebar.checkbox('K')

number_N = st.sidebar.slider('N',0,60)
#puls_number_N = st.sidebar.number_input('N_adjustment',min_value=0,step =1)
number_P = st.sidebar.slider('P',0,60)
#puls_number_P = st.sidebar.number_input('p_adjustment',min_value=0,step =1)
number_K = st.sidebar.slider('K',0,60)
#puls_number_K = st.sidebar.number_input('K_adjustment',min_value=0,step =1)

puls_number_N = st.sidebar.number_input('N_adjustment',min_value=0,step =1)
puls_number_P = st.sidebar.number_input('p_adjustment',min_value=0,step =1)
puls_number_K = st.sidebar.number_input('K_adjustment',min_value=0,step =1)

puls_number_N = int(puls_number_N)
puls_number_P = int(puls_number_P)
puls_number_K = int(puls_number_K)

n_amount_max = number_N + puls_number_N
n_amount_min = number_N - puls_number_N

p_amount_max = number_P + puls_number_P
p_amount_min = number_P - puls_number_P

k_amount_max = number_K + puls_number_K
k_amount_min = number_K - puls_number_K


#home
st.write(f'N:{number_N} ± {puls_number_N}  P:{number_P} ± {puls_number_P} K:{number_K} ± {puls_number_K}')
df  = df.query('@n_amount_min <= N <= @n_amount_max')
df  = df.query('@p_amount_min <= P <= @p_amount_max')
df  = df.query('@k_amount_min <= K <= @k_amount_max')
#df  = df.query('"n_amount_min" <= N <= "n_amount_max"')
#df = df[df['N'] == "n_amount"]
long = len(df.index)
st.write(f'ヒット件数:{long}')
#st.dataframe(df[["肥料の名称","肥料業者","肥料種類名称","N","P","K","登録番号"]])
st.dataframe(df[["肥料の名称","肥料業者","肥料種類名称","N","P","K","登録番号"]],width=1200, height=500)
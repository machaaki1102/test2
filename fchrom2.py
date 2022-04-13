import streamlit as st
import pandas as pd

#データ
df = pd.read_csv('finished_data.csv',index_col=0,encoding='cp932')

#body
#sidebar
st.sidebar.write('select')

with st.sidebar:
    col1, col2,col3 = st.columns(3)
    with col1:
        selected_N = st.checkbox('N')
    with col2:
        selected_P = st.checkbox('P')
    with col3:
        selected_K = st.checkbox('K')

number_N = st.sidebar.slider('N',0,60)
number_P = st.sidebar.slider('P',0,60)
number_K = st.sidebar.slider('K',0,60)

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

#化成＝生、輸入＝輸、なし＝原料
with st.sidebar:
    selected_sei = st.checkbox('化成肥料を除外する')
    selected_you = st.checkbox('輸入品を除外する')
    selected_gen = st.checkbox('有機原料を除外する')

if selected_sei:
    df = df[~df['登録番号'].str.contains('生')]
if selected_you:
    df = df[~df['登録番号'].str.contains('輸|外')]
if selected_gen:
    df = df[~df['登録番号'].str.startswith('第')]

#home
st.write(f'N:{number_N} ± {puls_number_N}  P:{number_P} ± {puls_number_P} K:{number_K} ± {puls_number_K}')

if selected_N:
    df  = df.query('@n_amount_min <= N <= @n_amount_max')
if selected_P:
    df  = df.query('@p_amount_min <= P <= @p_amount_max')
if selected_K:
    df  = df.query('@k_amount_min <= K <= @k_amount_max')

list_s = []
list_s = df["肥料業者"].unique()
choices = st.multiselect('業者セレクト',list_s)

if choices:
    df = df.query('肥料業者 == @choices')

long = len(df.index)
st.write(f'ヒット件数:{long}')
st.dataframe(df[["肥料の名称","肥料業者","N","P","K","肥料種類名称","登録番号"]],width=1200, height=500)
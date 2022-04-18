import streamlit as st
import pandas as pd
from PIL import Image    

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
#with st.sidebar:
#    selected_sei = st.checkbox('製造肥料を除外する')
#    selected_you = st.checkbox('輸入品を除外する')
#    selected_gen = st.checkbox('有機原料を除外する')

#if selected_sei:
#    df = df[~df['登録番号'].str.contains('生')]
#if selected_you:
#    df = df[~df['登録番号'].str.contains('輸|外')]
#if selected_gen:
#    df = df[~df['登録番号'].str.startswith('第')]

#home
if 'page' not in st.session_state:
    st.session_state.page=0

st.session_state.ccsha = 0
st.session_state.tasha = 0


if st.session_state.page == 0 :

    st.header('検索画面')
#st.write(f'N:{number_N} ± {puls_number_N}  P:{number_P} ± {puls_number_P} K:{number_K} ± {puls_number_K}')
#c_box = ['化成','配合','液肥','苦土','燐肥','粉末','土改','BS','その他']
#t_box = ['Dd','ASU','UF','CDU','IB','CN','亜ﾘﾝ','微量','被覆']
#c_number = len(c_box)
#col_a,col_b = st.columns(2)
    st.write('<製品カテゴリ>')

#c_box = ['化成','配合','液肥','苦土','燐肥','粉末','土改','BS','その他'] 
    col1,col2,col3,col4,col5,col6,col7,col8,col9 = st.columns(9)
    with col1:
        selected_1 = st.checkbox('化成')
    with col2:
        selected_2 = st.checkbox('配合')
    with col3:
        selected_3 = st.checkbox('液肥')
    with col4:
        selected_4 = st.checkbox('苦土')
    with col5:
        selected_5 = st.checkbox('燐肥')
    with col6:
        selected_6 = st.checkbox('粉末')
    with col7:
        selected_7 = st.checkbox('土改')
    with col8:
        selected_8 = st.checkbox('BS')
    with col9:
        selected_9 = st.checkbox('その他')

#t_box = ['Dd','ASU','UF','CDU','IB','CN','亜ﾘﾝ','微量','被覆']
    st.write('<特長>')

    col11,col12,col13,col14,col15,col16,col17,col18,col19 = st.columns(9)
    with col11:
        selected_11 = st.checkbox('Dd')
    with col12:
        selected_12 = st.checkbox('ASU')
    with col13:
        selected_13 = st.checkbox('UF')
    with col14:
        selected_14 = st.checkbox('CDU')
    with col15:
        selected_15 = st.checkbox('IB')

#col6,col7,col8,col9, = st.columns(4)
    with col16:
        selected_16 = st.checkbox('CN')
    with col17:
        selected_17 = st.checkbox('亜ﾘﾝ')
    with col18:
        selected_18 = st.checkbox('微量')
    with col19:
        selected_19 = st.checkbox('被覆')

    col_n,col_p,col_k = st.columns(3)
    with col_n:
        number_N = st.text_input('N',0,60)
    with col_p:
        number_P = st.text_input('P',0,60)
    with col_k:
        number_K = st.text_input('K',0,60)

    ccsha = st.checkbox('自社品')
    tasha = st.checkbox('他社品')
    kensaku = st.button('検索')

    
    if kensaku:
        st.session_state.page = 1
        if ccsha:
            st.session_state.ccsha = 1

        if tasha:
            st.session_state.tasha = 1    
   

          
#  st.experimental_rerun()    
#    if selected_N:
#        df  = df.query('@n_amount_min <= N <= @n_amount_max')
#    if selected_P:
#        df  = df.query('@p_amount_min <= P <= @p_amount_max')
#    if selected_K:
#        df  = df.query('@k_amount_min <= K <= @k_amount_max')

#list_s = []
#list_s = df["肥料業者"].unique()
#choices = st.multiselect('業者セレクト',list_s)

#if choices:
#    df = df.query('肥料業者 == @choices'

#long = len(df.index)
#st.write(f'ヒット件数:{long}')
if st.session_state.page == 1:
    col_cc,col_dd = st.columns(2)
    with col_cc:
    #    st.write('自社品')
        if st.session_state.ccsha == 1:
            st.write('自社品')
            st.dataframe(df[["肥料の名称","N","P","K","肥料種類名称"]],width=500, height=500)
            modoru = st.button('戻る ')
            if modoru:
                st.session_state.page = 0
                st.session_state.ccsha = 0
                st.session_state.tasha = 0
#                st.experimental_rerun() 
    with col_dd:
    #    st.write('他社品')
        if st.session_state.tasha == 1:
            st.write('他社品')
            st.dataframe(df[["肥料の名称","N","P","K","肥料種類名称"]],width=500, height=500)
            modoru = st.button(' 戻る')
            if modoru:
                st.session_state.page = 0
                st.session_state.tasha = 0
                st.session_state.ccsha = 0
 #               st.experimental_rerun() 

#st.dataframe(df[["肥料の名称","肥料業者","N","P","K","肥料種類名称","登録番号"]],width=1200, height=500)


#list_c = df['登録番号'].unique()
#s = st.multiselect('登録番号よりチラシ',list_c)
#st.write(s)#s = st.text_input('登録番号')
try:
    if s[0] == '生第10000号':
        col1,col2 = st.columns(2)
        with col1:
            st.image('1024.jpg')
        with col2:
            st.image('1024_2.jpg')
except:
    pass
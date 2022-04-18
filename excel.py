import streamlit as st
import os

if 'page' not in st.session_state:
    st.session_state.page=0

select_radio = ['新規','追記']
radio = st.radio('which',select_radio)

#page=0
if radio == '新規':
    ban = 1
    st.write(f'登録番号:{ban}')
    tokui = st.text_input('得意先')
    shiken = st.text_input('試験名')
    touroku = st.button('登録')
    file_path = 'C:Users¥ono¥Desktop¥123.txt'
    
    if touroku:
        with open(file_path,'w') as f:
            f.write(tokui)
            f.close()

if radio == '追記':
    st.write('前回の続き')
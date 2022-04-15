import streamlit as st


if 'page' not in st.session_state:
    st.session_state.page=0

select_radio = ['新規','追記']
radio = st.radio('which',select_radio)

#page=0
if radio == '新規':
    tokui = st.text_input('得意先')
    shiken = st.text_input('試験名')
    touroku = st.button('登録')
    if touroku:
        with open('C:/Users/ono/Desktop/jj.txt','w') as f:
            f.write(tokui)

if radio == '追記':
    st.write('前回の続き')
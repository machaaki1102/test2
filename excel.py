import streamlit as st


if 'page' not in st.session_state:
    st.session_state.page=0

select_radio = ['新規','追記']
radio = st.radio('which',select_radio)

#page=0
if radio == '新規':
    st.text_input('得意先')
    st.text_input('試験名')

if radio == '追加':
    st.write('前回の続き')
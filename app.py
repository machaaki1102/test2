import streamlit as st 
import pandas as pd
import matplotlib
import matplotlib.pyplot as plt
import seaborn as sns
import os
from matplotlib.backends.backend_agg import RendererAgg

#Loading the data
@st.cache
def get_data_deputies():
     return pd.read_csv(os.path.join(os.getcwd(),'df_dep.csv'))
@st.cache
def get_data_political_parties():
     return pd.read_csv(os.path.join(os.getcwd(),'df_polpar.csv'))

#configuration of the page
st.set_page_config(layout="wide")
#load dataframes
df_dep = get_data_deputies()
df_pol_par = get_data_political_parties()
st.title('French national assembly vizualisation tool')
st.markdown("""
This app performs simple visualization from the open data from the french national assembly!
""")
st.write(df_dep)
st.write(df_pol_par)
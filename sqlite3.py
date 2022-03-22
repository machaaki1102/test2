import streamlit as st 
import pandas as pd
import matplotlib
import matplotlib.pyplot as plt
import seaborn as sns
import os
import sqlite3

con = sqlite3.connect('example.db')
cur = con.cursor()

#Create table
cur.execute('''CREATE TABLE stocks
                (date text,trans text,symbol text,qty real, price real)''')

#Insert a row of data
cur.excute("INSERT INTO stocks VALUES('2006-01-05','BUY','RHAT','100.35.14')")
con.commit()
con.close()

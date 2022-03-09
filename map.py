import pandas as pd
import plotly.express as px

px.set_mapbox_access_token('pk.eyJ1IjoibWFjaGFha2kiLCJhIjoiY2wwamVyanUxMGJ2bTNqcjU4dGZtdWdoZyJ9.Vk57Qp-OPGYFkGdgTB6iYw')

df = pd.read_csv('covid19-a.csv',header-1)

fig = px.scatter_mapbox(df,lat='lat',lon='lon',size='pop',color='pop',size_max=80,z00m=3,height=500)
fig.update_layoout(margin={'r':0,'t':0,'l':0,'b':0})
fig
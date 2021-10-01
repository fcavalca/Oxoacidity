# -*- coding: utf-8 -*-
"""
Created on 30/09/2021

@author: Filippo Cavalca
"""
  
import plotly.graph_objects as go
from plotly.subplots import make_subplots
import plotly.express as px
#import numpy as np
import os
import pandas as pd
import streamlit as st

#from vc.definitions import ROOT_DIR
datadir = "C:\\Users\\filip\\Seaborg Technologies ApS\\Chemistry - General\\Chemistry and Materials Operations\\Oxoacidity"
filename=""
def file_selector(folder_path=datadir):
    filenames = os.listdir(folder_path)
    selected_filename = st.selectbox('Select a file', filenames)
    filename = selected_filename
    return os.path.join(folder_path, selected_filename)

file = file_selector()
st.write('You selected `%s`' % file)


#filename = "OCP of oxoacidity electrode system with wet atmosphere transitioning from 80 to 70 degrees.txt"
#file = datadir + filename


#Make pandas dataframe from raw data
data = pd.read_csv(file, sep=';', header=0, index_col=0)
#%%
#data.columns


#data['Time'] =  pd.to_datetime(data['Time'], format="%d.%m.%Y %H:%M:%S")
#data.set_index('Time',inplace=True)

#%%
#Plot data on the same Datetime axis, grouped by units

# Create a Plotly figure.
fig = go.Figure()

fig = make_subplots(rows=2, shared_xaxes=True)
fig.update_layout(
    title=filename,
    hovermode='x',
    height=800,
    width=800,
    plot_bgcolor='#ffffff'
)

# Dict to set better axis properties.
xaxis_dict = {
    # Move ticks outside the plot.
    'ticks': 'outside',
    'title_text': data.index.name,
    # Show plot borders with these four settings.
    'showline': True,
    'linewidth': 2,
    'linecolor': 'black',
    'mirror': True,
    # Remove gridlines in the plot.
    'showgrid': False
}
yaxis_dict = {
    # Move ticks outside the plot.
    'ticks': 'outside',
    # Show plot borders with these four settings.
    'showline': True,
    'linewidth': 2,
    'linecolor': 'black',
    'mirror': True,
    # Remove gridlines in the plot.
    'showgrid': False
}
fig.update_xaxes(xaxis_dict)
fig.update_yaxes(yaxis_dict)


#%%

fig.add_trace(go.Scattergl(y=data[data.columns[0]], name = data.columns[0]),row=1, col=1)
fig.update_yaxes(title_text=data.columns[0], row=1, col=1)

fig.add_trace(go.Scattergl(y=data[data.columns[3]], name = data.columns[3]),row=2, col=1)
fig.update_yaxes(title_text=data.columns[3], row=2, col=1)



#data.plot(y=P_P, ax=axs[0]);
#axs[0].set_title("Partial pressures");
#axs[0].set_ylabel('Partial pressure (ppm)')
#axs[0].set_xlim(trange)
#axs[0].set_ylim(get_ylim(P_P))

#data.plot(y=Pressures, ax=axs[1], color=['red', 'green']);
#axs[1].set_title("Pressures");
#axs[1].set_ylabel('Pressure (mmHg?)')
#axs[1].set_ylim(get_ylim(Pressures))

#data.plot(y=Temperatures, ax=axs[2], color=['blue', 'black', 'brown']);
#axs[2].set_title("Temperatures");
#axs[2].set_ylabel('Temperature (°C)')
#axs[2].set_ylim(get_ylim(Temperatures))

st.plotly_chart(fig)
#st.pyplot(fig)
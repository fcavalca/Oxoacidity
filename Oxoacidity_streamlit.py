# -*- coding: utf-8 -*-
"""
Created on 03/10/2021

@author: Filippo Cavalca
"""
  
import plotly.graph_objects as go
from plotly.subplots import make_subplots
#import plotly.express as px
#import numpy as np
import pandas as pd
import streamlit as st

st.title("Oxoacidity data plotter")
file = st.sidebar.file_uploader("Upload a data file", type=["csv", "txt"])
xsize = st.sidebar.slider( "Plot width" , min_value=200 , max_value=1000, value=800, step=2)
ysize = st.sidebar.slider( "Plot height" , min_value=200 , max_value=1000, value=500,  step=2)

if file:
    
    #Make pandas dataframe from raw data
    data = pd.read_csv(file, sep=';', header=0, index_col=0)
    
    # Create a Plotly figure.
    fig = go.Figure()
    
    fig = make_subplots(rows=2, shared_xaxes=True)
    fig.update_layout(
        hovermode='x',
        height=ysize,
        width=xsize,
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

    
    st.plotly_chart(fig)
    
else:
    st.write("Upload a file to get started")

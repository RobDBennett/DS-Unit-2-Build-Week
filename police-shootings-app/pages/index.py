# Imports from 3rd party libraries
import dash
import dash_bootstrap_components as dbc
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output
import plotly.express as px
import pandas as pd
import numpy as np
from joblib import load
# Imports from this application
from app import app

# 2 column layout. 1st column width = 4/12
# https://dash-bootstrap-components.opensource.faculty.ai/l/components/layout
column1 = dbc.Col(
    [
        dcc.Markdown(
            """
        
## Introduction:
   
Welcome to the Police Shooting's Data App. This has been produced by Rob Bennett for Lambda School's Unit 2 builds.
This is a fairly easy app to use, though perhaps not immediately intuitive. On the right hand, you will see a 
violin graph of the raw data. Each datapoint is represented, listing the victim's age, state and broken down by
race via color. Hovering over the graph will show you each data point, and above the image are a few commands to
interact with it directly if you would like to do so.

Along the top navigation bar, you will see a few tabs- 
The 'Process' tab is a run down on where the data came from, what I did to treat it, what my initial thoughts are, 
and my findings regarding the topic. I have tried to speak more to a general audience in that section. 
The 'Visualizations' tab contains numerous static images of various metrics of the data. Each image has a brief 
description of the graph in question pointing out what it is displaying. The nature of these graphs forces the 
conversation to be a bit more technical. 
The final tab is 'Predictions'. This interfaces with my Logistic Regression model in real time. There are a few 
features that you can define in the slider/pull downs that will cause the machine to predict the race of the 
victim along the right hand column. As time allows, I will be updating this model to select 'Cities', which is 
currently unavailable, and tuning the models used to create greater accuracy.

Thank you for your time.

If you prefer a more written description and explanation of this data in long form, please consult my [blog.](http://robdbennett.com/2020-06-25-build_2_Police_Shootings/)

            """
        ),
        dcc.Link(dbc.Button('Test the Model', color='primary'), href='/predictions')
    ],
    md=4,
)

wrangled1 = pd.read_csv('assets/wrangled1.csv')
wrangled1 = wrangled1.drop(columns='Unnamed: 0')
fig = px.violin(wrangled1, y='race', x='age', color='race', box=True, points='all', hover_data=wrangled1.columns)
fig2 = px.violin(wrangled1, y='race', x='state', color='race', box=True, points='all', hover_data=wrangled1.columns)
column2 = dbc.Col(
    [
        dcc.Graph(figure=fig),

	dcc.Graph(figure=fig2)
    ]
)

layout = dbc.Row([column1, column2])
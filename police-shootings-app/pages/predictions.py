# Imports from 3rd party libraries
import dash
import dash_bootstrap_components as dbc
import dash_core_components as dcc
import dash_html_components as html
import pandas as pd
from dash.dependencies import Input, Output
from joblib import load
import plotly.express as px
# Imports from this application

from app import app

pipeline = load('assets/pipeline.joblib')
cat = pipeline.named_steps['ordinalencoder'].mapping[3]
checkitout = cat['mapping'].index.dropna().tolist()
checkitout = sorted(checkitout)


# 2 column layout. 1st column width = 4/12
# https://dash-bootstrap-components.opensource.faculty.ai/l/components/layout
column1 = dbc.Col(
    [
        dcc.Markdown('## Predictions', className='mb-5'),
	dcc.Markdown('#### Age'),
	dcc.Slider(
		id='age',
		min=10,
		max=90,
		step=None,
		value=20,
		marks={
			10: {'label': '10', 'style': {'color':'#f50'}},
			15: {'label': '15', 'style': {'color': '#77b0b1'}},
			20: {'label': '20', 'style': {'color': '#77b0b1'}},
			25: {'label': '25', 'style': {'color': '#77b0b1'}},
			30: {'label': '30', 'style': {'color': '#77b0b1'}},
			35: {'label': '35', 'style': {'color': '#77b0b1'}},
			40: {'label': '40', 'style': {'color': '#77b0b1'}},
			45: {'label': '45', 'style': {'color': '#77b0b1'}},
			50: {'label': '50', 'style': {'color': '#77b0b1'}},
			55: {'label': '55', 'style': {'color': '#77b0b1'}},
			60: {'label': '60', 'style': {'color': '#77b0b1'}},
			65: {'label': '65', 'style': {'color': '#77b0b1'}},
			70: {'label': '70', 'style': {'color': '#77b0b1'}},
			75: {'label': '75', 'style': {'color': '#77b0b1'}},
			80: {'label': '80', 'style': {'color': '#77b0b1'}},
			85: {'label': '85', 'style': {'color': '#77b0b1'}},
			90: {'label': '90', 'style': {'color': '#f50'}}
			},
		className='mb-5',

        ),
	dcc.Markdown('#### Gender'),
	dcc.Dropdown(
		id='gender',
		options=[
			{'label': 'Male', 'value':'M'},
			{'label': 'Female','value':'F'},
			],
		value='M',
		className='mb-5',
		),
	dcc.Markdown('#### Manner of Death'),
	dcc.Dropdown(
		id='manner_of_death',
		options=[
			{'label':'Shot','value':'shot'},
			{'label':'Shot and Tasered', 'value':'shot and Tasered'},
			],
		value='shot',
		className='mb-5',
		),

	dcc.Markdown('#### Signs of Mental Illness?'),
	dcc.Dropdown(
		id='signs_of_mental_illness',
		options=[
			{'label':'Yes','value':'1'},
			{'label':'No','value':'0'},
			],
		value='0',
		className='mb-5',
		),

	dcc.Markdown('#### Threat Level of the Victim?'),
	dcc.Dropdown(
		id='threat_level',
		options=[
			{'label':'Attacking','value':'attack'},
			{'label':'Other','value':'other'},
			{'label':'Not Listed','value':'undetermined'},
			],
		value='attack',
		className='mb-5',
		),

	dcc.Markdown('#### Was the officer wearing a Body Camera?'),
	dcc.Dropdown(
		id='body_camera',
		options=[
			{'label':'No','value':'0'},
			{'label':'Yes','value':'1'},
			],
		value='0',
		className='mb-5',
		),

	dcc.Markdown('#### Was the victim attempting to flee?'),
	dcc.Dropdown(
		id='flee',
		options=[
			{'label':'Not Fleeing','value':'not fleeing'},
			{'label':'Car','value':'Car'},
			{'label':'Foot','value':'Foot'},
			{'label':'Other','value':'Other'},
			],
		value='not fleeing',
		className='mb-5',
		),
	dcc.Markdown('#### Weapon'),
	dcc.Dropdown(
		id='armed',
		options=[
			{'label':'Gun','value':'gun'},
			{'label':'Knife','value':'knife'},
			{'label':'Undetermined','value':'undetermined'},	
			{'label':'Unarmed','value':'unarmed'},
			{'label':'Taser','value':'Taser'},
			{'label':'Ax','value':'ax'},
			{'label':'Sword','value':'sword'},
			{'label':'Vehicle','value':'vehicle'},
			{'label':'Baseball Bat','value':'baseball bat'},
			{'label':'Crossbow','value':'crossbow'},
			{'label':'Scissors','value':'scissors'},
			{'label':'Machete','value':'machete'},
			{'label':'Toy','value':'toy weapon'},
			{'label':'Unknown Weapon','value':'unknown weapon'},
			],
		value='gun',
		className='mb-5',
		),
	dcc.Markdown('#### City'),
	dcc.Dropdown(
		id='city',
		options=[{'label':l, 'value':l} for l in checkitout],
		value='Los Angeles',
		className='mb-5',
		),


	dcc.Markdown('#### State'),
	dcc.Dropdown(
		id='state',
		options=[
			{'label': 'AL', 'value':'AL'},
			{'label': 'AK', 'value':'AK'},
			{'label': 'AZ', 'value':'AZ'},
			{'label': 'AR', 'value':'AR'},
			{'label': 'CA', 'value':'CA'},
			{'label': 'CO', 'value':'CO'},
			{'label': 'CT', 'value':'CT'},
			{'label': 'DE', 'value':'DE'},
			{'label': 'DC', 'value':'DC'},
			{'label': 'FL', 'value':'FL'},
			{'label': 'GA', 'value':'GA'},
			{'label': 'HI', 'value':'HI'},
			{'label': 'ID', 'value':'ID'},
			{'label': 'IL', 'value':'IL'},
			{'label': 'IN', 'value':'IN'},
			{'label': 'IA', 'value':'IA'},
			{'label': 'KS', 'value':'KS'},
			{'label': 'KY', 'value':'KY'},
			{'label': 'LA', 'value':'LA'},
			{'label': 'ME', 'value':'ME'},
			{'label': 'MD', 'value':'MD'},
			{'label': 'MA', 'value':'MA'},
			{'label': 'MI', 'value':'MI'},
			{'label': 'MN', 'value':'MN'},
			{'label': 'MS', 'value':'MS'},
			{'label': 'MO', 'value':'MO'},
			{'label': 'MT', 'value':'MT'},
			{'label': 'NE', 'value':'NE'},
			{'label': 'NV', 'value':'NV'},
			{'label': 'NH', 'value':'NH'},
			{'label': 'NJ', 'value':'NJ'},
			{'label': 'NM', 'value':'NM'},
			{'label': 'NY', 'value':'NY'},
			{'label': 'NC', 'value':'NC'},
			{'label': 'ND', 'value':'ND'},
			{'label': 'OH', 'value':'OH'},
			{'label': 'OK', 'value':'OK'},
			{'label': 'OR', 'value':'OR'},
			{'label': 'PA', 'value':'PA'},
			{'label': 'RI', 'value':'RI'},
			{'label': 'SC', 'value':'SC'},
			{'label': 'SD', 'value':'SD'},
			{'label': 'TN', 'value':'TN'},
			{'label': 'TX', 'value':'TX'},
			{'label': 'UT', 'value':'UT'},
			{'label': 'VT', 'value':'VT'},
			{'label': 'VA', 'value':'VA'},
			{'label': 'WA', 'value':'WA'},
			{'label': 'WV', 'value':'WV'},
			{'label': 'WI', 'value':'WI'},
			{'label': 'WY', 'value':'WY'},
		],
		value= 'CA',
		className='mb-5',
		),
    ],
    md=4,
)

column2 = dbc.Col(
    [

	html.H2('Expected Race', className='mb-5'),
	dcc.Markdown('This is the predicted race of the victim.'),
	html.Div(id='prediction-content', className='lead'),
    ]
)

layout = dbc.Row([column1, column2])

@app.callback(
    Output('prediction-content', 'children'),
    [Input('age', 'value'), Input('gender', 'value'), Input('manner_of_death', 'value'), Input('signs_of_mental_illness', 'value'), Input('threat_level', 'value'), Input('body_camera', 'value'), Input('flee', 'value'), Input('armed', 'value'),Input('city','value'),Input('state', 'value')],
)
def predict(age, gender, manner_of_death, signs_of_mental_illness, threat_level, body_camera, flee, armed,city, state):
    df = pd.DataFrame(
        columns=['manner_of_death', 'armed', 'age', 'gender', 'city', 'state', 'signs_of_mental_illness', 'threat_level', 'flee', 'body_camera'], 
	data=[[manner_of_death, armed, age, gender,city,state,signs_of_mental_illness,threat_level,flee,body_camera]]
    )
    y_pred = pipeline.predict(df)[0]
    return y_pred
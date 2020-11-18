# Imports from 3rd party libraries
import dash
import dash_bootstrap_components as dbc
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output

# Imports from this application
from app import app

# 1 column layout
# https://dash-bootstrap-components.opensource.faculty.ai/l/components/layout
column1 = dbc.Col(
    [
        dcc.Markdown('## Visualizations', className='mb-5'),
	
	dcc.Markdown('I have a variety of visualizations about my findings with the data. To start, we will go with the Distribution of the listed racial demographics across the data. For all following graphs, the order found in the distribution graph will be the same for the various racial categories. IE- Asian is Class 0, White is Class 1, etc.'),

	html.Img(src='assets/DistB2.JPG', className='img-fluid'),

	dcc.Markdown('I built a confusion matrix for my Logistical Regression model. As you can see, the performance of this model is better than baseline, but not by a vast margin. For this particular app, I weighted the races equally, however, if I wanted to increase the accuracy of a specific race, that would be fairly simple. A Confusion Matrix is used to determine the Accuracy and Recall of your model.'),

	html.Img(src='assets/ConMatB2.JPG', className='img-fluid'),

	dcc.Markdown('To look at our next images, it helps to see a permutation importance chart, so I have included one. Of all of the various things that we learned this unit, I cannot overstate the value of a Permutation Importance chart. This is the tool that readily tells you which features affect your outcomes the most.'),

	html.Img(src='assets/PermImpB2.JPG', className='img-fluid'),

	dcc.Markdown('For a partial-dependence with one feature across the categories looks a little like this. This particular graph shows the impact of various states on the races. Because I had to encode the states, they are not visible, but 9 is Washington. As this is my home, I wanted to point it out.'),
	
	html.Img(src='assets/PDP1f1B2.JPG', className='img-fluid'),
	html.Img(src='assets/PDP1f2B2.JPG', className='img-fluid'),

	dcc.Markdown('Partial dependency for 2 features looks a little more interesting. This compares the impact of Age and State on the various racial categories. The lighter colored areas denote a higher degree of importance. Across the board, being younger affected the model in minorities at a higher rate than baseline.'),

	html.Img(src='assets/PDP2f1B2.JPG', className='img-fluid'),
	html.Img(src='assets/PDP2f2B2.JPG', className='img-fluid'),

	dcc.Markdown('Shapley Values was probably my favorite discovery this build. It can show the exact impact of each feature per row. Its drawback is that you have to run a graph for each row. However, this "slice of life" for the data, is also very helpful in giving a more visually understandable model.'),

	html.Img(src='assets/ShapB2.JPG', className='img-fluid'),

     ],
)

layout = dbc.Row([column1])
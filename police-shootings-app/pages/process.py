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
        dcc.Markdown(
            """
       
## Defining the Question
Can we use linear models in order to predict police shootings in the US? 
  

## Exploring the Question
Nationwide, the eyes of the public have turned towards the police with ever increasing scrutiny and questions 
regarding police violence. This is particularly important to examine as it relates to fatalities, particularly 
among minorities. Its important to understand the context of these actions and look at them with as much 
objectivity as one can. These are sensetive topics in the best of times, and we are far from the best of times.


## The Data
Criminal data was difficult to find. I found a few government sites that listed some measure of datasets, but 
often they were 'clunky'. However, I did find that the Washington Post had an excellent dataset regarding fatal 
shootings where an officer killed a suspect. Because the focus of this data is so specific, it's difficult to 
ask more than a few very similarly specific questions with it. Namely, we can't explore the number of police interactions 
or prosecutions as it relates to this data. Towards that end, I ask the viewers to be objective in their 
interpretation of the data. There are many questions that I would like to ask, but can't with this data, 
so we will keep our focus limited.

The raw data can be found [here](https://github.com/washingtonpost/data-police-shootings/blob/master/fatal-police-shootings-data.csv)

My notebook evaluating and training my models can be found [here](https://github.com/RobDBennett/DS-Unit-2-Build-Week/blob/master/Unit2-Build-Week-Project-PoliceShootings.ipynb)

## Shaping the Data
This data was already exceptionally clean. While there were many NaN values, most relevant data was present. 
I had several attempts at engineering new features, but each attempt gave me a great deal of data leakage. 
It gave me some different ideas for where to take things, but at the end of the day, all of my models 
performed better without much wrangling. The NaN values were manually imputed to maintain the integrity of 
the data, but then I structured an encoder and ran it through a few models.

Before we get too far into that, I want to talk about the data a moment. Removing NaN values for listed race, 
we have 4890 shooting incidents. 50.57% are white victims, whereas (nation wide) they represent 60.4% of the 
population. 26.5% are black, contrasted with a national representation of 13.4%, and hispanics murders are 18.4% 
to a population of 18.3%. We're already seeing some behavior bias. The only other point I would like to make 
with this data is that only about 51% of these victims were armed with lethal force themselves. 

I picked two models to do my primary explorations with. The first was a straight forward Logistic Regression. 
I had some mixed success with Randon Forests, but I ended up going with XGBClassifier for my tree model selection. 
These performed more or less equally well with the data I provided. Logistic Regression yielded a 55.6% validation 
accuracy, which is about 5% above baseline. XGB had an accuracy of 54.4% validation, so this is the 
model that I performed my final test on, which yielded a 54.2%, about 4% better than baseline.


## Conclusion
This is a topic that ended up being a bit darker than I had hoped, and it was difficult to keep real life thoughts 
out of the data. Why are so few of these rated positive for body camera footage? Why are the shootings so high in 
general? Why are Black deaths so much higher than their national average for population distribution? The data can't 
really answer these questions, just point out that they *should* be asked. Regardless, it leaves me with a bitter 
taste and some harsh wonderings to review. 

The models that I selected both beat the baseline, but there is some static on them. I looked into engineering new 
features; I scrapped demographic information and build that into the datasets, but from a hindsight perspective, it 
leaked into the data quite a bit. Even with a wide variety of racial differences (New Mexico, Maine, and Alabama all 
have vastly different demographics), the models were quickly able to draw the similarities and predict with a 95% 
accuracy. I didn't care for that. Removing those elements caused there to be a more true model. I also tried to peel 
off some of the existing features for the noise they created, but it resulted in more or less the same accuracy.
            """
        ),

    ],
)

layout = dbc.Row([column1])
import dash
from dash import dcc, html, callback, Output, Input, State
import plotly.express as px
import dash_bootstrap_components as dbc
import plotly.figure_factory as ff
import pandas as pd
from skimage import io
import cv2

dash.register_page(__name__,name = 'CRIC-OVERT' ,path='/', order=0000000000000000)


layout = [
    html.Div([
    dbc.Row(
        dbc.Col(
                [
                html.H2('CRIC-OVERT', style={'textAlign': 'center'}),
                html.Br(),
                html.H6('Welcome to the homepage of Cric-Overt, your go-to destination of ODI World Cups. Our website is dedicated to providing you with the ODI World Cup statistics from the first to the latest and more from the world of cricket. Whether you are a die-hard fan or a casual observer, we have something for everyone.', style={'textAlign': 'center'}),
                html.Br(),
                html.H6('Our website uses advanced machine learning techniques to analyze data and provide insights. We have employed four different algorithms - K nearest Neighbours, Support Vector Machines, Logistic Regression, and Artificial Neural Network - to analyze and interpret complex datasets. By utilizing these cutting-edge algorithms, we are able to provide accurate predictions and recommendations that can help you make informed decisions based on data-driven insights.', style={'textAlign': 'center'}),
                html.Br(),
                html.H6('At our website, we believe that data analysis is the key to unlocking success, just as it is in the game of cricket. By leveraging advanced algorithms and data analytics tools, we provide insights that can help you make strategic decisions and stay ahead of the competition - much like a cricketer who carefully reads the pitch and plans their shots accordingly. Our goal is to help you score big and achieve your goals, both on and off the cricket field.', style={'textAlign': 'center'}),
                html.Br(),
                html.H2('ALGORITHMS', style={'textAlign': 'center'}),
                html.Br(),
                    html.Div(
                        [
                            dbc.Col(
                                [
                                    dcc.Dropdown(
                                        ['K-NEAREST NEIGHBORS', 'SUPPORT VECTOR MACHINES', 'LOGISTIC REGRESSION',
                                         'ARTIFICIAL NEURAL NETWORK - LOGISTIC REGRESSION', ]
                                        , placeholder='KNOW MORE ABOUT ALGORITHMS', id='request_cric_overt'
                                    ),
                                ], xs=10, sm=10, md=8, lg=4, xl=4, xxl=4
                            ),
                        ], style={"display": "flex", "justifyContent": "center"},
                    ),
                html.Br(),
                html.Div(
                        [
                        dbc.Button("SUBMIT", id="inp-button", className="data_input", n_clicks=0),
                        ], style={"display": "flex", "justifyContent": "center"},
                    ),
                html.Br(),
                html.Div([],id = 'a',style={"display": "flex", "justifyContent": "center"}),
                html.Br(),
                html.Div([],id = 'b',style={"display": "flex", "justifyContent": "center"}),
                html.H2('DATA',style={'textAlign': 'center'}),
                html.Br(),
                html.H6(' BATSMANS AND WICKET KEEPERS - No of matches played, Total runs scored, Batting average, Batting Strike Rate ',style={'textAlign': 'center'}),
                html.Br(),
                html.H6(' BOWLERS - No of matches played, Total wickets, Bowling economy, Bowling strike rate, Bowling Average',style={'textAlign': 'center'}),
                html.Br(),
                html.H6(' ALL ROUNDERS - No of matches played, Total runs scored, Batting average, Batting Strike Rate , Total wickets, Bowling economy, Bowling strike rate, Bowling Average',style={'textAlign': 'center'})
                ]
       )
    )
])
]

@dash.callback(

    [
        Output('a','children'),
        Output('b','children')
    ],

    [
        #Input('teams', "value"),
        Input('inp-button', "n_clicks")
    ],

    [
        State("request_cric_overt", 'value'),
        State('a','children'),
        State('b','children')
    ],

        prevent_initial_call=True,

    )

def output(n_clicks,need,o1,o2):

    if need == 'K-NEAREST NEIGHBORS':

        img = cv2.imread('assets/Images/KNN.png')
        img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
        fig = px.imshow(img)
        fig.update_layout(coloraxis_showscale=False)
        fig.update_xaxes(showticklabels=False)
        fig.update_yaxes(showticklabels=False)

        return [html.Div
            ([
            html.H2('K-NEAREST NEIGHBORS',style={"display": "flex", "justifyContent": "center"}),
            html.Br(),
            html.H6('* The KNN algorithm is arguably the simplest machine learning algorithm. Building the model consists only of storing the training dataset.'),
            html.H6('* The KNN algorithm considers its nearest data points, where the number of data points to consider will be mentioned to the best of accuracy obtained.'),
            html.H6('* The value obtained after considering all the nearest neighbor data points is the predicted output.')
            ])
            ,dcc.Graph(figure=fig,config={'displayModeBar': True})]

    elif need == 'SUPPORT VECTOR MACHINES':

        img = cv2.imread('assets/Images/SVM.png')
        img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
        fig = px.imshow(img)
        fig.update_layout(coloraxis_showscale=False)
        fig.update_xaxes(showticklabels=False)
        fig.update_yaxes(showticklabels=False)

        return [html.Div
            ([
            html.H2('SUPPORT VECTOR MACHINES', style={"display": "flex", "justifyContent": "center"}),
            html.Br(),
            html.H6('* Support Vector Machine, often known as SVM, can be used for classification and regression tasks, they typically perform best in the classification problems.'),
            html.H6('* In this supervised machine learning algorithm, we look for the optimal hyperplane to divide the classes.'),
            html.H6('* The best hyperplane is the one that is farthest from the classes, and this is what SVM primarily aims to achieve.')
        ])
            , dcc.Graph(figure=fig, config={'displayModeBar': True})]

    elif need == 'LOGISTIC REGRESSION':

        img = cv2.imread('assets/Images/LR.png')
        img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
        fig = px.imshow(img)
        fig.update_layout(coloraxis_showscale=False)
        fig.update_xaxes(showticklabels=False)
        fig.update_yaxes(showticklabels=False)

        return [html.Div
            ([
            html.H2('LOGISTIC REGRESSION', style={"display": "flex", "justifyContent": "center"}),
            html.Br(),
            html.H6('* One of the most often used Machine Learning algorithms, within the category of Supervised Learning, is logistic regression. Using a predetermined set of independent factors, it is used to predict the categorical dependent variable.'),
            html.H6('* Given its capacity to offer probabilities and categorise new data using continuous and discrete datasets, logistic regression is an important machine learning technique.'),
            html.H6('* When classifying observations using various sources of data, logistic regression can be used to quickly identify the factors that will work well.')
        ])
            , dcc.Graph(figure=fig, config={'displayModeBar': True})]

    elif need == 'ARTIFICIAL NEURAL NETWORK - LOGISTIC REGRESSION':

        img = cv2.imread('assets/Images/ANN.png')
        img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
        fig = px.imshow(img)
        fig.update_layout(coloraxis_showscale=False)
        fig.update_xaxes(showticklabels=False)
        fig.update_yaxes(showticklabels=False)

        return [html.Div
            ([
            html.H2('ARTIFICIAL NEURAL NETWORK - LOGISTIC REGRESSION', style={"display": "flex", "justifyContent": "center"}),
            html.Br(),
            html.H6('* A technique for binary classification is logistic regression. It can be modelled as a function with any number of inputs and a range of 0 to 1 for the output.'),
            html.H6('* A machine learning method for categorization issues is the artificial neural network. An ANN is a collection of connected input and output networks where each connection has a weight assigned to it. One input layer, one or more intermediate layers, and one output layer make up this structure.'),
            html.H6()
        ])
            , dcc.Graph(figure=fig, config={'displayModeBar': True})]

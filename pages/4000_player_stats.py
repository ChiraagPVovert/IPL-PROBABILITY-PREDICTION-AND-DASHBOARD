import dash
from dash import html, dcc, Input, Output, State, callback, dash_table
import dash_bootstrap_components as dbc
import plotly.express as px
import pandas as pd
from .sidebar_4000 import sidebar
import plotly.graph_objects as go
import plotly.figure_factory as ff

dash.register_page(__name__, name='PLAYER STATISTICS' ,order=1110000000000000)

def layout():
    return html.Div([
    dbc.Row(
        [
            dbc.Col(
                [
                    sidebar()
                ], xs=4, sm=4, md=2, lg=2, xl=2, xxl=2),

            dbc.Col(
                [
                    html.H3('BATTING STATS IN WORLD CUPS', style={'textAlign':'center'}),
                    html.Br(),
                    html.Div([dcc.Dropdown(['MOST RUNS', 'HIGHEST SCORERS IN AN INNINGS', #'BEST AVERAGE','BEST STRIKE RATE',
                                            'MOST BOUNDARIES','MOST RUNS FROM BOUNDARIES','MOST 100s','MOST 50s',
                                            'BEST STRIKE RATE IN AN INNINGS','MOST BOUNDARIES IN AN INNINGS',
                                            'MOST RUNS FROM BOUNDARIES IN AN INNINGS'], id='request_all_bat')]),
                    html.Br(),
                    html.Div(
                        [
                            dbc.Button("SUBMIT", id="inp-button", className="data_input", n_clicks=0),
                        ], style={"display": "flex", "justifyContent": "center"},
                    ),
                    html.Br(),
                    html.Div([],id='service_all_1_bat'),
                    html.Br(),
                    html.Div([], id='service_all_2_bat')
                ], xs=8, sm=8, md=10, lg=10, xl=10, xxl=10)
        ]
    )
])

@dash.callback(

    [
        Output('service_all_1_bat','children'),
        Output('service_all_2_bat','children'),
    ],

    [
        #Input('teams', "value"),
        Input('inp-button', "n_clicks")
    ],

    [
        State("request_all_bat", 'value'),
        State('service_all_1_bat','children'),
        State('service_all_2_bat','children'),
    ],

        prevent_initial_call=True,

    )

def output(n_clicks,need,o1,o2):

    batting = pd.read_excel('assets/Player_Stats/Bat_complete.xlsx')
    batting_in_an_innings = pd.read_excel('assets/Player_Stats/Batsman_innings.xlsx')

    if need == 'MOST RUNS':
        batting = batting.sort_values(by=['Runs'],ascending=False)
        batting_data = batting[['Player','Runs','HS', 'Country']] #'Ave','SR',
        batting_10 = batting.head(10)
        df1_fig = ff.create_table(batting_data.head(50), index=False)

        fig_1 = px.bar(batting_10, x='Player', y='Runs',
                     hover_data=['Country', 'HS','SR'], color='Runs',
                     #labels={'pop': 'population of Canada'},
                     height=400)

        return [
            dcc.Graph(figure=fig_1),
            dcc.Graph(figure=df1_fig)
            #bat_table
        ]

    elif need == 'HIGHEST SCORERS IN AN INNINGS':

        batting = batting.sort_values(by=['HS'], ascending=False)
        batting_data = batting[['Player', 'HS', 'Runs','Country']]# 'Ave','SR',
        batting_10 = batting.head(10)
        df1_fig = ff.create_table(batting_data.head(50), index=False)

        fig_1 = px.bar(batting_10, x='Player', y='HS',
                       hover_data=['Country', 'Runs'], color='HS',
                       # labels={'pop': 'population of Canada'},
                       height=400)

        return [
            dcc.Graph(figure=fig_1),
            dcc.Graph(figure=df1_fig)
            # bat_table
        ]

    elif need == 'BEST AVERAGE':

        batting = batting.sort_values(by=['Ave'], ascending=False)
        batting_data = batting[['Player', 'Ave','Runs', 'HS', 'SR', 'Country']]
        batting_10 = batting.head(10)
        df1_fig = ff.create_table(batting_data.head(50), index=False)

        fig_1 = px.bar(batting_10, x='Player', y='Ave',
                       hover_data=['Country', 'Runs', 'HS', 'SR'], color='Ave',
                       # labels={'pop': 'population of Canada'},
                       height=400)

        return [
            dcc.Graph(figure=fig_1),
            dcc.Graph(figure=df1_fig)
            # bat_table
        ]

    elif need == 'BEST STRIKE RATE':

        batting = batting.sort_values(by=['SR'], ascending=False)
        batting_data = batting[['Player', 'SR', 'Runs', 'HS', 'Ave', 'Country']]
        batting_10 = batting.head(10)
        df1_fig = ff.create_table(batting_data.head(50), index=False)

        fig_1 = px.bar(batting_10, x='Player', y='SR',
                       hover_data=['Country', 'Runs', 'HS', 'Ave'], color='SR',
                       # labels={'pop': 'population of Canada'},
                       height=400)

        return [
            dcc.Graph(figure=fig_1),
            dcc.Graph(figure=df1_fig)
            # bat_table
        ]

    elif need == 'MOST BOUNDARIES':

        batting = batting.sort_values(by=['BOUNDARIES'], ascending=False)
        batting_data = batting[['Player', '4s', '6s', 'BOUNDARIES','RUNS FROM BOUNDARIES','Country']]
        batting_10 = batting.head(10)
        df1_fig = ff.create_table(batting_data.head(50), index=False)

        fig_1 = go.Figure()
        fig_1.add_trace(go.Bar(
            x=batting_10['Player'],
            y=batting['4s'],
            name='FOURS',
            #marker_color='indianred'
        ))
        fig_1.add_trace(go.Bar(
            x=batting_10['Player'],
            y=batting['6s'],
            name='SIXES',
            #marker_color='lightsalmon'
        ))

        return [
            dcc.Graph(figure=fig_1),
            dcc.Graph(figure=df1_fig)
            # bat_table
        ]
    elif need == 'MOST RUNS FROM BOUNDARIES':

        batting = batting.sort_values(by=['RUNS FROM BOUNDARIES'], ascending=False)
        batting_data = batting[['Player', 'RUNS FROM BOUNDARIES', 'Runs', 'HS', 'Country']]
        batting_10 = batting.head(10)
        df1_fig = ff.create_table(batting_data.head(50), index=False)

        fig_1 = px.bar(batting_10, x='Player', y='RUNS FROM BOUNDARIES',
                       hover_data=['Country', 'Runs', 'HS','RUNS FROM BOUNDARIES'], color='RUNS FROM BOUNDARIES',
                       # labels={'pop': 'population of Canada'},
                       height=400)

        return [
            dcc.Graph(figure=fig_1),
            dcc.Graph(figure=df1_fig)
            # bat_table
        ]

    elif need == 'MOST 100s':

        batting = batting.sort_values(by=['100s'], ascending=False)
        batting_data = batting[['Player', '100s','Runs', 'HS',  'Country']]#'SR','Ave',
        batting_10 = batting.head(10)
        df1_fig = ff.create_table(batting_data.head(50), index=False)

        fig_1 = px.bar(batting_10, x='Player', y='100s',
                       hover_data=['Country', 'Runs', 'HS'], color='100s',
                       # labels={'pop': 'population of Canada'},
                       height=400)

        return [
            dcc.Graph(figure=fig_1),
            dcc.Graph(figure=df1_fig)
            # bat_table
        ]

    elif need == 'MOST 50s':

        batting = batting.sort_values(by=['50s'], ascending=False)
        batting_data = batting[['Player', '50s','Runs', 'HS',  'Country']]#'SR','Ave',
        batting_10 = batting.head(10)
        df1_fig = ff.create_table(batting_data.head(50), index=False)

        fig_1 = px.bar(batting_10, x='Player', y='50s',
                       hover_data=['Country', 'Runs', 'HS'], color='50s',
                       # labels={'pop': 'population of Canada'},
                       height=400)

        return [
            dcc.Graph(figure=fig_1),
            dcc.Graph(figure=df1_fig)
            # bat_table
        ]

    elif need == 'BEST STRIKE RATE IN AN INNINGS':

        batting_in_an_innings = batting_in_an_innings.sort_values(by=['SR'], ascending=False)
        batting_data = batting_in_an_innings[['Player','Runs', 'Balls','4s','6s','SR', 'Country','Opposition']]
        batting_10 = batting_in_an_innings.head(10)
        df1_fig = ff.create_table(batting_data.head(50), index=False)

        fig_1 = px.bar(batting_10, x='Player', y='SR',
                       hover_data=['Runs', 'Balls','4s','6s', 'Country','Opposition'], color='SR',
                       # labels={'pop': 'population of Canada'},
                       height=400)

        return [
            dcc.Graph(figure=fig_1),
            dcc.Graph(figure=df1_fig)
            # bat_table
        ]

    elif need == 'MOST BOUNDARIES IN AN INNINGS':

        batting_in_an_innings = batting_in_an_innings.sort_values(by=['4 and 6'], ascending=False)
        batting_data = batting_in_an_innings[['Player','Runs', 'Balls','4s','6s','SR', 'Country','Opposition']]
        batting_10 = batting_in_an_innings.head(10)
        df1_fig = ff.create_table(batting_data.head(50), index=False)

        fig_1 = go.Figure()
        fig_1.add_trace(go.Bar(
            x=batting_10['Player'],
            y=batting_10['4s'],
            name='FOURS',
            # marker_color='indianred'
        ))
        fig_1.add_trace(go.Bar(
            x=batting_10['Player'],
            y=batting_10['6s'],
            name='SIXES',
            # marker_color='lightsalmon'
        ))

        return [
            dcc.Graph(figure=fig_1),
            dcc.Graph(figure=df1_fig)
            # bat_table
        ]

    elif need == 'MOST RUNS FROM BOUNDARIES IN AN INNINGS':

        batting_in_an_innings = batting_in_an_innings.sort_values(by=['4+6'], ascending=False)
        batting_data = batting_in_an_innings[['Player', 'Runs', 'Balls', '4s', '6s','4+6', 'SR', 'Country', 'Opposition']]
        batting_10 = batting_in_an_innings.head(10)
        df1_fig = ff.create_table(batting_data.head(50), index=False)

        fig_1 = px.bar(batting_10, x='Player', y='4+6',
                       hover_data=['Runs', 'Balls', '4s', '6s', 'Country', 'Opposition'], color='4+6',
                       # labels={'pop': 'population of Canada'},
                       height=400)

        return [
            dcc.Graph(figure=fig_1),
            dcc.Graph(figure=df1_fig)
            # bat_table
        ]
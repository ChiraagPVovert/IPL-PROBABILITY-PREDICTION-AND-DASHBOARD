import dash
from dash import html,dcc, dash_table, Output, Input, State
import dash_bootstrap_components as dbc
from .sidebar_2009_ipl import sidebar
import os
import pandas as pd
import plotly.figure_factory as ff
import plotly.express as px
import plotly.graph_objects as go

dash.register_page(__name__,name = 'BATTING RECORDS',order=2)

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
                    html.H3('BATTING - 2009 IPL', style={'textAlign':'center'}),
                    html.Br(),
                    html.Div([dcc.Dropdown(['MOST RUNS', 'HIGHEST SCORERS IN AN INNINGS', 'BEST AVERAGE',
                                            'BEST STRIKE RATE','MOST BOUNDARIES','MOST RUNS FROM BOUNDARIES','MOST 100S','MOST 50S',
                                            'BEST STRIKE RATE IN AN INNINGS','MOST BOUNDARIES IN AN INNINGS',
                                            'MOST RUNS FROM BOUNDARIES IN AN INNINGS'], id='request_bat_ipl_2009')]),
                    html.Br(),
                    html.Div(
                        [
                            dbc.Button("SUBMIT", id="inp-button", className="data_input", n_clicks=0),
                        ], style={"display": "flex", "justifyContent": "center"},
                    ),
                    html.Br(),
                    html.Div([],id='service_1_ipl_2009_bat'),
                    html.Br(),
                    html.Div([], id='service_2_ipl_2009_bat')
                ], xs=8, sm=8, md=10, lg=10, xl=10, xxl=10)
        ]
    )
])

@dash.callback(

    [
        Output('service_1_ipl_2009_bat','children'),
        Output('service_2_ipl_2009_bat','children'),
    ],

    [
        #Input('teams', "value"),
        Input('inp-button', "n_clicks")
    ],

    [
        State("request_bat_ipl_2009", 'value'),
        State('service_1_ipl_2009_bat','children'),
        State('service_2_ipl_2009_bat','children'),
    ],

        prevent_initial_call=True,

    )

def output(n_clicks,need,o1,o2):

    batting = pd.read_excel('assets/IPL/2009_ipl/bat_most_runs_hs_avg_sr_bf_no_hund_fifties_ducks_sixes_fours_ipl_2009.xlsx')
    batting_in_an_innings = pd.read_excel('assets/IPL/2009_ipl/bat_most_runs_from_fours_and_sixes_in_an_innings_ipl_2009.xlsx')

    if need == 'MOST RUNS':
        batting = batting.sort_values(by=['RUNS'],ascending=False)
        batting_data = batting[['PLAYER','RUNS','HIGHEST', 'AVERAGE','STRIKE RATE','TEAM']]
        batting_10 = batting.head(10)
        #df1_fig = ff.create_table(batting_data, index=False)
        df1_fig = dbc.Table.from_dataframe(batting_data, striped=True, bordered=True, hover=True)

        fig_1 = px.bar(batting_10, x='PLAYER', y='RUNS',
                     hover_data=['TEAM', 'HIGHEST', 'AVERAGE','STRIKE RATE'], color='RUNS',
                     #labels={'pop': 'population of Canada'},
                     height=400)

        return [
            dcc.Graph(figure=fig_1),
            html.Div(df1_fig)
            #bat_table
        ]

    elif need == 'HIGHEST SCORERS IN AN INNINGS':

        batting = batting.sort_values(by=['HIGHEST'], ascending=False)
        batting_data = batting[['PLAYER', 'HIGHEST', 'RUNS', 'AVERAGE','HIGHEST O/NO','STRIKE RATE','TEAM']]
        batting_10 = batting.head(10)
        df1_fig = dbc.Table.from_dataframe(batting_data, striped=True, bordered=True, hover=True)

        fig_1 = px.bar(batting_10, x='PLAYER', y='HIGHEST',
                       hover_data=['TEAM', 'RUNS', 'AVERAGE', 'STRIKE RATE'], color='HIGHEST',
                       # labels={'pop': 'population of Canada'},
                       height=400)

        return [
            dcc.Graph(figure=fig_1),
            html.Div(df1_fig)
            # bat_table
        ]

    elif need == 'BEST AVERAGE':

        batting = batting.sort_values(by=['AVERAGE'], ascending=False)
        batting_data = batting[['PLAYER', 'AVERAGE','RUNS', 'HIGHEST', 'STRIKE RATE', 'TEAM']]
        batting_10 = batting.head(10)
        df1_fig = dbc.Table.from_dataframe(batting_data, striped=True, bordered=True, hover=True)

        fig_1 = px.bar(batting_10, x='PLAYER', y='AVERAGE',
                       hover_data=['TEAM', 'RUNS', 'HIGHEST', 'STRIKE RATE'], color='AVERAGE',
                       # labels={'pop': 'population of Canada'},
                       height=400)

        return [
            dcc.Graph(figure=fig_1),
            html.Div(df1_fig)
            # bat_table
        ]

    elif need == 'BEST STRIKE RATE':

        batting = batting.sort_values(by=['STRIKE RATE'], ascending=False)
        batting_data = batting[['PLAYER', 'STRIKE RATE', 'RUNS', 'HIGHEST', 'AVERAGE', 'TEAM']]
        batting_10 = batting.head(10)
        df1_fig = dbc.Table.from_dataframe(batting_data, striped=True, bordered=True, hover=True)

        fig_1 = px.bar(batting_10, x='PLAYER', y='STRIKE RATE',
                       hover_data=['TEAM', 'RUNS', 'HIGHEST', 'AVERAGE'], color='STRIKE RATE',
                       # labels={'pop': 'population of Canada'},
                       height=400)

        return [
            dcc.Graph(figure=fig_1),
            html.Div(df1_fig)
            # bat_table
        ]

    elif need == 'MOST BOUNDARIES':

        batting = batting.sort_values(by=['BOUNDARIES'], ascending=False)
        batting_data = batting[['PLAYER', '4S', '6S', 'BOUNDARIES','RUNS FROM BOUNDARIES','TEAM']]
        batting_10 = batting.head(10)
        df1_fig = dbc.Table.from_dataframe(batting_data, striped=True, bordered=True, hover=True)

        fig_1 = go.Figure()
        fig_1.add_trace(go.Bar(
            x=batting_10['PLAYER'],
            y=batting['4S'],
            name='FOURS',
            #marker_color='indianred'
        ))
        fig_1.add_trace(go.Bar(
            x=batting_10['PLAYER'],
            y=batting['6S'],
            name='SIXES',
            #marker_color='lightsalmon'
        ))

        return [
            dcc.Graph(figure=fig_1),
            html.Div(df1_fig)
            # bat_table
        ]
    elif need == 'MOST RUNS FROM BOUNDARIES':

        batting = batting.sort_values(by=['RUNS FROM BOUNDARIES'], ascending=False)
        batting_data = batting[['PLAYER', 'RUNS FROM BOUNDARIES', 'RUNS', 'HIGHEST', 'AVERAGE','TEAM']]
        batting_10 = batting.head(10)
        df1_fig = dbc.Table.from_dataframe(batting_data, striped=True, bordered=True, hover=True)

        fig_1 = px.bar(batting_10, x='PLAYER', y='RUNS FROM BOUNDARIES',
                       hover_data=['TEAM', 'RUNS', 'HIGHEST', 'AVERAGE','RUNS FROM BOUNDARIES'], color='RUNS FROM BOUNDARIES',
                       # labels={'pop': 'population of Canada'},
                       height=400)

        return [
            dcc.Graph(figure=fig_1),
            html.Div(df1_fig)
            # bat_table
        ]

    elif need == 'MOST 100S':

        batting = batting.sort_values(by=['100S'], ascending=False)
        batting_data = batting[['PLAYER', '100S','RUNS', 'HIGHEST', 'STRIKE RATE','AVERAGE', 'TEAM']]
        batting_10 = batting.head(2)
        df1_fig = dbc.Table.from_dataframe(batting_data.head(2), striped=True, bordered=True, hover=True)

        fig_1 = px.bar(batting_10, x='PLAYER', y='100S',
                       hover_data=['TEAM', 'RUNS', 'HIGHEST', 'STRIKE RATE','AVERAGE'], color='100S',
                       # labels={'pop': 'population of Canada'},
                       height=400)

        return [
            dcc.Graph(figure=fig_1),
            html.Div(df1_fig)
            # bat_table
        ]

    elif need == 'MOST 50S':

        batting = batting.sort_values(by=['50S'], ascending=False)
        batting_data = batting[['PLAYER', '50S','RUNS', 'HIGHEST', 'STRIKE RATE','AVERAGE', 'TEAM']]
        batting_10 = batting.head(10)
        df1_fig = dbc.Table.from_dataframe(batting_data.head(36), striped=True, bordered=True, hover=True)

        fig_1 = px.bar(batting_10, x='PLAYER', y='50S',
                       hover_data=['TEAM', 'RUNS', 'HIGHEST', 'STRIKE RATE','AVERAGE'], color='50S',
                       # labels={'pop': 'population of Canada'},
                       height=400)

        return [
            dcc.Graph(figure=fig_1),
            html.Div(df1_fig)
            # bat_table
        ]

    elif need == 'BEST STRIKE RATE IN AN INNINGS':

        batting_in_an_innings = batting_in_an_innings.sort_values(by=['STRIKE RATE'], ascending=False)
        batting_data = batting_in_an_innings[['PLAYER','RUNS', 'BALLS','4S','6S','STRIKE RATE', 'TEAM','OPPOSITION']]
        batting_10 = batting_in_an_innings.head(10)
        df1_fig = dbc.Table.from_dataframe(batting_data.head(31), striped=True, bordered=True, hover=True)

        fig_1 = px.bar(batting_10, x='PLAYER', y='STRIKE RATE',
                       hover_data=['RUNS', 'BALLS','4S','6S', 'TEAM','OPPOSITION'], color='STRIKE RATE',
                       # labels={'pop': 'population of Canada'},
                       height=400)

        return [
            dcc.Graph(figure=fig_1),
            html.Div(df1_fig)
            # bat_table
        ]

    elif need == 'MOST BOUNDARIES IN AN INNINGS':

        batting_in_an_innings = batting_in_an_innings.sort_values(by=['RUNS FROM BOUNDARIES'], ascending=False)
        batting_data = batting_in_an_innings[['PLAYER','4+6','RUNS FROM BOUNDARIES','RUNS', 'BALLS','4S','6S','STRIKE RATE', 'TEAM','OPPOSITION']]
        batting_10 = batting_in_an_innings.head(10)
        df1_fig = dbc.Table.from_dataframe(batting_data.head(50), striped=True, bordered=True, hover=True)

        fig_1 = go.Figure()
        fig_1.add_trace(go.Bar(
            x=batting_10['PLAYER'],
            y=batting_10['4S'],
            name='FOURS',
            # marker_color='indianred'
        ))
        fig_1.add_trace(go.Bar(
            x=batting_10['PLAYER'],
            y=batting_10['6S'],
            name='SIXES',
            # marker_color='lightsalmon'
        ))

        return [
            dcc.Graph(figure=fig_1),
            html.Div(df1_fig)
            # bat_table
        ]

    elif need == 'MOST RUNS FROM BOUNDARIES IN AN INNINGS':

        batting_in_an_innings = batting_in_an_innings.sort_values(by=['RUNS FROM BOUNDARIES'], ascending=False)
        batting_data = batting_in_an_innings[['PLAYER', 'RUNS FROM BOUNDARIES', 'BALLS', '4S', '6S','4+6','RUNS','STRIKE RATE', 'TEAM', 'OPPOSITION']]
        batting_10 = batting_in_an_innings.head(10)
        df1_fig = dbc.Table.from_dataframe(batting_data.head(50), striped=True, bordered=True, hover=True)

        fig_1 = px.bar(batting_10, x='PLAYER', y='RUNS FROM BOUNDARIES',
                       hover_data=['RUNS FROM BOUNDARIES', 'BALLS', '4S', '6S','RUNS', 'TEAM', 'OPPOSITION'], color='RUNS FROM BOUNDARIES',
                       # labels={'pop': 'population of Canada'},
                       height=400)

        return [
            dcc.Graph(figure=fig_1),
            html.Div(df1_fig)
            # bat_table
        ]
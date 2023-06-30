import dash
from dash import html, dcc, dash_table, Output, Input, State
import dash_bootstrap_components as dbc
from .sidebar_2009_ipl import sidebar
import pandas as pd
import plotly.figure_factory as ff
import plotly.express as px
import plotly.graph_objects as go

dash.register_page(__name__, name='BOWLING RECORDS', order=3)


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
                        html.H3('BOWLING - 2009 IPL', style={'textAlign': 'center'}),
                        html.Br(),
                        html.Div([dcc.Dropdown(['MOST WICKETS', 'MOST OVERS BOWLED', 'MOST MAIDEN OVERS BOWLED',
                                                'BEST ECONOMY', 'BEST AVERAGE', 'BEST STRIKE RATE',
                                                'BEST BOWLING FIGURES IN AN INNINGS',
                                                'LEAST RUNS CONCEDED IN AN INNINGS',
                                                'MOST RUNS CONCEDED IN AN INNINGS',
                                                'MOST MAIDENS BOWLED IN AN INNINGS', 'MOST WICKETS TAKEN IN AN INNINGS',
                                                'BEST ECONOMY IN AN INNINGS'], id='request_bowl_ipl_2009')]),
                        html.Br(),
                        html.Div(
                            [
                                dbc.Button("SUBMIT", id="inp-button", className="data_input", n_clicks=0),
                            ], style={"display": "flex", "justifyContent": "center"},
                        ),
                        html.Br(),
                        html.Div([], id='service_1_ipl_2009_bowl'),
                        html.Br(),
                        html.Div([], id='service_2_ipl_2009_bowl')
                    ], xs=8, sm=8, md=10, lg=10, xl=10, xxl=10)
            ]
        )
    ])


@dash.callback(

    [
        Output('service_1_ipl_2009_bowl', 'children'),
        Output('service_2_ipl_2009_bowl', 'children'),
    ],

    [
        # Input('teams', "value"),
        Input('inp-button', "n_clicks")
    ],

    [
        State("request_bowl_ipl_2009", 'value'),
        State('service_1_ipl_2009_bowl', 'children'),
        State('service_2_ipl_2009_bowl', 'children'),
    ],

    prevent_initial_call=True,

)
def output(n_clicks, need, o1, o2):
    bowling = pd.read_excel('assets/IPL/2009_ipl/bowl_wkts_avg_econ_sr_4w_5w_bbi_ipl_2009.xlsx')
    bowling_in_an_innings = pd.read_excel('assets/IPL/2009_ipl/bowl_innings_wkts_econ_runsconc_sr_ipl_2009.xlsx')

    if need == 'MOST WICKETS':
        bowling = bowling.sort_values(by=['WICKETS'], ascending=False)
        bowling_data = bowling[['PLAYER', 'WICKETS', 'ECONOMY', 'AVERAGE', 'STRIKE RATE', 'TEAM']]
        bowling_10 = bowling.head(10)
        df1_fig = dbc.Table.from_dataframe(bowling_data, striped=True, bordered=True, hover=True)

        fig_1 = px.bar(bowling_10, x='PLAYER', y='WICKETS',
                       hover_data=['TEAM', 'ECONOMY', 'AVERAGE', 'STRIKE RATE'], color='WICKETS',
                       # labels={'pop': 'population of Canada'},
                       height=400)

        return [
            dcc.Graph(figure=fig_1),
            html.Div(df1_fig)
            # bat_table
        ]

    elif need == 'MOST OVERS BOWLED':
        bowling = bowling.sort_values(by=['OVERS'], ascending=False)
        bowling_data = bowling[['PLAYER', 'OVERS', 'ECONOMY', 'AVERAGE', 'STRIKE RATE', 'WICKETS', 'TEAM']]
        bowling_10 = bowling.head(10)
        df1_fig = dbc.Table.from_dataframe(bowling_data, striped=True, bordered=True, hover=True)

        fig_1 = px.bar(bowling_10, x='PLAYER', y='OVERS',
                       hover_data=['TEAM', 'ECONOMY', 'AVERAGE', 'STRIKE RATE', 'WICKETS'], color='OVERS',
                       # labels={'pop': 'population of Canada'},
                       height=400)

        return [
            dcc.Graph(figure=fig_1),
            html.Div(df1_fig)
            # bat_table
        ]

    elif need == 'MOST MAIDEN OVERS BOWLED':
        bowling = bowling.sort_values(by=['MAIDENS'], ascending=False)
        bowling_data = bowling[['PLAYER', 'MAIDENS', 'ECONOMY', 'AVERAGE', 'STRIKE RATE', 'WICKETS', 'TEAM']]
        bowling_10 = bowling.head(10)
        df1_fig = dbc.Table.from_dataframe(bowling_data, striped=True, bordered=True, hover=True)

        fig_1 = px.bar(bowling_10, x='PLAYER', y='MAIDENS',
                       hover_data=['TEAM', 'ECONOMY', 'AVERAGE', 'STRIKE RATE', 'WICKETS', 'OVERS'], color='MAIDENS',
                       # labels={'pop': 'population of Canada'},
                       # text='pop',
                       height=400)

        return [
            dcc.Graph(figure=fig_1),
            html.Div(df1_fig)
            # bat_table
        ]

    elif need == 'BEST ECONOMY':
        bowling = bowling.sort_values(by=['ECONOMY'])
        bowling_data = bowling[
            ['PLAYER', 'ECONOMY', 'OVERS', 'RUNS', 'MAIDENS', 'AVERAGE', 'STRIKE RATE', 'WICKETS', 'TEAM']]
        bowling_10 = bowling.head(10)
        df1_fig = dbc.Table.from_dataframe(bowling_data, striped=True, bordered=True, hover=True)

        fig_1 = px.bar(bowling_10, x='PLAYER', y='ECONOMY',
                       hover_data=['TEAM', 'MAIDENS', 'OVERS', 'RUNS', 'AVERAGE', 'STRIKE RATE', 'WICKETS', 'OVERS'],
                       color='ECONOMY',
                       # labels={'pop': 'population of Canada'},
                       # text='pop',
                       height=400)

        return [
            dcc.Graph(figure=fig_1),
            html.Div(df1_fig)
            # bat_table
        ]

    elif need == 'BEST AVERAGE':
        bowling = bowling.sort_values(by=['AVERAGE'])
        # bowling = bowling.where(bowling["AVERAGE"] != 0)
        bowling_data = bowling[
            ['PLAYER', 'AVERAGE', 'ECONOMY', 'OVERS', 'RUNS', 'MAIDENS', 'STRIKE RATE', 'WICKETS', 'TEAM']]
        bowling_10 = bowling.head(10)
        df1_fig = dbc.Table.from_dataframe(bowling_data, striped=True, bordered=True, hover=True)

        fig_1 = px.bar(bowling_10, x='PLAYER', y='AVERAGE',
                       hover_data=['TEAM', 'ECONOMY', 'OVERS', 'RUNS', 'MAIDENS', 'STRIKE RATE', 'WICKETS', 'OVERS'],
                       color='AVERAGE',
                       # labels={'pop': 'population of Canada'},
                       # text='pop',
                       height=400)

        return [
            dcc.Graph(figure=fig_1),
            html.Div(df1_fig)
            # bat_table
        ]

    elif need == 'BEST STRIKE RATE':
        bowling = bowling.sort_values(by=['STRIKE RATE'])
        # bowling = bowling.where(bowling["AVERAGE"] != 0)
        bowling_data = bowling[
            ['PLAYER', 'STRIKE RATE', 'ECONOMY', 'OVERS', 'RUNS', 'MAIDENS', 'AVERAGE', 'WICKETS', 'OVERS', 'TEAM']]
        bowling_10 = bowling.head(10)
        df1_fig = dbc.Table.from_dataframe(bowling_data, striped=True, bordered=True, hover=True)

        fig_1 = px.bar(bowling_10, x='PLAYER', y='STRIKE RATE',
                       hover_data=['TEAM', 'ECONOMY', 'MAIDENS', 'AVERAGE', 'WICKETS', 'OVERS'], color='STRIKE RATE',
                       # labels={'pop': 'population of Canada'},
                       # text='pop',
                       height=400)

        return [
            dcc.Graph(figure=fig_1),
            html.Div(df1_fig)
            # bat_table
        ]

    elif need == 'BEST BOWLING FIGURES IN AN INNINGS':
        bowling = bowling_in_an_innings.sort_values(by=['WICKETS'], ascending=False)
        # bowling = bowling.where(bowling["AVERAGE"] != 0)
        bowling_data = bowling[
            ['PLAYER', 'OVERS', 'MAIDENS', 'RUNS', 'WICKETS', 'ECONOMY', 'STRIKE RATE', 'TEAM', 'OPPOSITION']]
        bowling_10 = bowling.head(10)
        df1_fig = dbc.Table.from_dataframe(bowling_data, striped=True, bordered=True, hover=True)

        fig_1 = px.bar(bowling_10, x='PLAYER', y='WICKETS',
                       hover_data=['OVERS', 'MAIDENS', 'RUNS', 'WICKETS', 'ECONOMY', 'STRIKE RATE', 'OPPOSITION', ],
                       color='WICKETS',
                       # labels={'pop': 'population of Canada'},
                       # text='pop',
                       height=400)

        return [
            dcc.Graph(figure=fig_1),
            html.Div(df1_fig)
            # bat_table
        ]

    elif need == 'LEAST RUNS CONCEDED IN AN INNINGS':
        bowling = bowling_in_an_innings.sort_values(by=['RUNS'], ascending=True)
        # bowling = bowling.where(bowling["AVERAGE"] != 0)
        bowling_data = bowling[
            ['PLAYER', 'OVERS', 'MAIDENS', 'RUNS', 'WICKETS', 'ECONOMY', 'STRIKE RATE', 'TEAM', 'OPPOSITION']]
        bowling_10 = bowling.head(10)
        df1_fig = dbc.Table.from_dataframe(bowling_in_an_innings, striped=True, bordered=True, hover=True)

        fig_1 = px.bar(bowling_10, x='PLAYER', y='RUNS',
                       hover_data=['OVERS', 'MAIDENS', 'RUNS', 'WICKETS', 'ECONOMY', 'STRIKE RATE', 'OPPOSITION', ],
                       color='RUNS',
                       # labels={'pop': 'population of Canada'},
                       # text='pop',
                       height=400)

        return [
            dcc.Graph(figure=fig_1),
            html.Div(df1_fig)
            # bat_table
        ]

    elif need == 'MOST RUNS CONCEDED IN AN INNINGS':
        bowling = pd.read_excel('assets/IPL/2009_ipl/bowl_innings_most_runs_conceded_ipl_2009.xlsx')
        bowling = bowling.sort_values(by=['RUNS'], ascending=False)
        # bowling = bowling.where(bowling["AVERAGE"] != 0)
        bowling_data = bowling[['PLAYER', 'OVERS', 'RUNS', 'WICKETS', 'ECONOMY', 'TEAM', 'OPPOSITION']]
        bowling_data = bowling_data.sort_values(by=['RUNS'], ascending=False)
        bowling_10 = bowling.head(10)
        df1_fig = dbc.Table.from_dataframe(bowling_data, striped=True, bordered=True, hover=True)

        fig_1 = px.bar(bowling_10, x='PLAYER', y='RUNS',
                       hover_data=['OVERS', 'RUNS', 'WICKETS', 'ECONOMY', 'OPPOSITION', ],
                       color='RUNS',
                       # labels={'pop': 'population of Canada'},
                       # text='pop',
                       height=400)

        return [
            dcc.Graph(figure=fig_1),
            html.Div(df1_fig)
            # bat_table
        ]

    elif need == 'MOST MAIDENS BOWLED IN AN INNINGS':
        bowling = bowling_in_an_innings.sort_values(by=['MAIDENS'], ascending=False)
        # bowling = bowling.where(bowling["AVERAGE"] != 0)
        bowling_data = bowling[
            ['PLAYER', 'OVERS', 'MAIDENS', 'RUNS', 'WICKETS', 'ECONOMY', 'STRIKE RATE', 'TEAM', 'OPPOSITION']]
        bowling_10 = bowling.head(10)
        df1_fig = dbc.Table.from_dataframe(bowling_data.head(11), striped=True, bordered=True, hover=True)

        fig_1 = px.bar(bowling_10, x='PLAYER', y='MAIDENS',
                       hover_data=['OVERS', 'MAIDENS', 'RUNS', 'WICKETS', 'ECONOMY', 'STRIKE RATE', 'OPPOSITION', ],
                       color='MAIDENS',
                       # labels={'pop': 'population of Canada'},
                       # text='pop',
                       height=400)

        return [
            dcc.Graph(figure=fig_1),
            html.Div(df1_fig)
            # bat_table
        ]

    elif need == 'MOST WICKETS TAKEN IN AN INNINGS':
        bowling = bowling_in_an_innings.sort_values(by=['WICKETS'], ascending=False)
        # bowling = bowling.where(bowling["AVERAGE"] != 0)
        bowling_data = bowling[
            ['PLAYER', 'OVERS', 'MAIDENS', 'RUNS', 'WICKETS', 'ECONOMY', 'STRIKE RATE', 'TEAM', 'OPPOSITION']]
        bowling_10 = bowling.head(10)
        df1_fig = dbc.Table.from_dataframe(bowling_data, striped=True, bordered=True, hover=True)

        fig_1 = px.bar(bowling_10, x='PLAYER', y='WICKETS',
                       hover_data=['OVERS', 'WICKETS', 'MAIDENS', 'RUNS', 'ECONOMY', 'STRIKE RATE', 'OPPOSITION', ],
                       color='WICKETS',
                       # labels={'pop': 'population of Canada'},
                       # text='pop',
                       height=400)

        return [
            dcc.Graph(figure=fig_1),
            html.Div(df1_fig)
            # bat_table
        ]

    elif need == 'BEST ECONOMY IN AN INNINGS':
        bowling = bowling_in_an_innings.sort_values(by=['ECONOMY'], ascending=True)
        # bowling = bowling.where(bowling["AVERAGE"] != 0)
        bowling_data = bowling[
            ['PLAYER', 'OVERS', 'MAIDENS', 'RUNS', 'WICKETS', 'ECONOMY', 'STRIKE RATE', 'TEAM', 'OPPOSITION']]
        bowling_10 = bowling.head(10)
        df1_fig = dbc.Table.from_dataframe(bowling_data, striped=True, bordered=True, hover=True)

        fig_1 = px.bar(bowling_10, x='PLAYER', y='ECONOMY',
                       hover_data=['OVERS', 'ECONOMY', 'MAIDENS', 'RUNS', 'WICKETS', 'STRIKE RATE', 'OPPOSITION', ],
                       color='ECONOMY',
                       # labels={'pop': 'population of Canada'},
                       # text='pop',
                       height=400)

        return [
            dcc.Graph(figure=fig_1),
            html.Div(df1_fig)
            # bat_table
        ]
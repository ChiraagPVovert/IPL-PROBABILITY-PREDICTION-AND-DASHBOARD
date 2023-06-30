import dash
from dash import html,dcc, dash_table, Output, Input, State
import dash_bootstrap_components as dbc
from .sidebar_2009_ipl import sidebar
import pandas as pd
import plotly.figure_factory as ff
import plotly.express as px

dash.register_page(__name__,name = 'WICKET KEEPER RECORDS',order=5)

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
                    html.H3('WICKET KEEPER - 2009 IPL', style={'textAlign':'center'}),
                    html.Br(),
                    html.Div([dcc.Dropdown(['MOST DISMISSALS INVOLVING A WICKET KEEPER',
                                            'MOST DISMISSALS INVOLVING A WICKET KEEPER IN AN INNINGS'], id='request_wk_ipl_2009')]),
                    html.Br(),
                    html.Div(
                        [
                            dbc.Button("SUBMIT", id="inp-button", className="data_input", n_clicks=0),
                        ], style={"display": "flex", "justifyContent": "center"},
                    ),
                    html.Br(),
                    html.Div([], id='service_1_wk_ipl_2009'),
                    html.Br(),
                    html.Div([], id='service_2_wk_ipl_2009')
                ], xs=8, sm=8, md=10, lg=10, xl=10, xxl=10)
        ]
    )
    ])

@dash.callback(

        [
            Output('service_1_wk_ipl_2009', 'children'),
            Output('service_2_wk_ipl_2009', 'children'),
        ],

        [
            # Input('teams', "value"),
            Input('inp-button', "n_clicks")
        ],

        [
            State("request_wk_ipl_2009", 'value'),
            State('service_1_wk_ipl_2009', 'children'),
            State('service_2_wk_ipl_2009', 'children'),
        ],

        prevent_initial_call=True,

    )
def output(n_clicks, need, o1, o2):

    wk = pd.read_excel('assets/IPL/2009_ipl/most_dismissals_by_wk_ipl_2009.xlsx')
    wk_innings = pd.read_excel('assets/IPL/2009_ipl/most_dismissals_in_an_innings_by_wk_ipl_2009.xlsx')

    if need == 'MOST DISMISSALS INVOLVING A WICKET KEEPER':
        wk = wk.sort_values(by=['DISMISSALS'],ascending=False)
        wk = wk[['PLAYER','MATCHES','CATCHES','STUMPS','DISMISSALS']]
        wk_10 = wk.head(10)
        df1_fig = dbc.Table.from_dataframe(wk, striped=True, bordered=True, hover=True)

        fig_1 = px.bar(wk_10, x='PLAYER', y='DISMISSALS',
                     hover_data=['PLAYER','MATCHES','CATCHES','STUMPS','DISMISSALS'], color='DISMISSALS',
                     #labels={'pop': 'population of Canada'},
                     height=400)

        return [
            dcc.Graph(figure=fig_1),
            html.Div(df1_fig)
            #bat_table
        ]

    elif need == 'MOST DISMISSALS INVOLVING A WICKET KEEPER IN AN INNINGS':
        wk_innings = wk_innings.sort_values(by=['DISMISSALS'],ascending=False)
        wk_innings = wk_innings[['PLAYER','CATCHES','STUMPS','DISMISSALS','GROUND','OPPOSITION']]
        wk_innings_10 = wk_innings.head(10)
        df1_fig = dbc.Table.from_dataframe(wk_innings.head(56), striped=True, bordered=True, hover=True)

        fig_1 = px.bar(wk_innings_10, x='PLAYER', y='DISMISSALS',
                     hover_data=['CATCHES','STUMPS','OPPOSITION','GROUND'], color='DISMISSALS',
                     #labels={'pop': 'population of Canada'},
                     height=400)

        return [
            dcc.Graph(figure=fig_1),
            html.Div(df1_fig)
            #bat_table
        ]
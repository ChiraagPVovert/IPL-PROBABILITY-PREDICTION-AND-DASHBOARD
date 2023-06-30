import dash
from dash import html,dcc, dash_table, Output, Input, State
import dash_bootstrap_components as dbc
from .sidebar_2009_ipl import sidebar
import pandas as pd
import plotly.figure_factory as ff
import plotly.express as px

dash.register_page(__name__,name='CATCH RECORDS',order=4)

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
                    html.H3('CATCHES - 2009 IPL', style={'textAlign':'center'}),
                    html.Br(),
                    html.Div([dcc.Dropdown(['MOST CATCHES (EXCLUDING WICKET KEEPER)',
                                            'MOST CATCHES IN A MATCH (EXCLUDING WICKET KEEPER)'], id='request_catch_ipl_2009')]),
                    html.Br(),
                    html.Div(
                        [
                            dbc.Button("SUBMIT", id="inp-button", className="data_input", n_clicks=0),
                        ], style={"display": "flex", "justifyContent": "center"},
                    ),
                    html.Br(),
                    html.Div([], id='service_1_catch_ipl_2009'),
                    html.Br(),
                    html.Div([], id='service_2_catch_ipl_2009')
                ], xs=8, sm=8, md=10, lg=10, xl=10, xxl=10)
        ]
    )
])

@dash.callback(

    [
        Output('service_1_catch_ipl_2009','children'),
        Output('service_2_catch_ipl_2009','children'),
    ],

    [
        #Input('teams', "value"),
        Input('inp-button', "n_clicks")
    ],

    [
        State("request_catch_ipl_2009", 'value'),
        State('service_1_catch_ipl_2009','children'),
        State('service_2_catch_ipl_2009','children'),
    ],

        prevent_initial_call=True,

    )

def output(n_clicks,need,o1,o2):

    catches = pd.read_excel('assets/IPL/2009_ipl/most_catches_ipl_2009.xlsx')
    catches_in_an_innings = pd.read_excel('assets/IPL/2009_ipl/most_catches_in_an_innings_ipl_2009.xlsx')

    if need == 'MOST CATCHES (EXCLUDING WICKET KEEPER)':
        catch = catches.sort_values(by=['CATCHES'],ascending=False)
        catch_data = catch[['PLAYER','MATCHES','CATCHES','TEAM']]
        catch_10 = catch.head(10)
        df1_fig = dbc.Table.from_dataframe(catch_data, striped=True, bordered=True, hover=True)

        fig_1 = px.bar(catch_10, x='PLAYER', y='CATCHES',
                     hover_data=['PLAYER','MATCHES','CATCHES','TEAM'], color='CATCHES',
                     #labels={'pop': 'population of Canada'},
                     height=400)

        return [
            dcc.Graph(figure=fig_1),
            html.Div(df1_fig)
            #bat_table
        ]

    elif need == 'MOST CATCHES IN A MATCH (EXCLUDING WICKET KEEPER)':
        catch = catches_in_an_innings.sort_values(by=['CATCHES'],ascending=False)
        catch_data = catch[['PLAYER','CATCHES','TEAM','OPPOSITION']]
        catch_10 = catch.head(10)
        df1_fig = dbc.Table.from_dataframe(catch_data, striped=True, bordered=True, hover=True)

        fig_1 = px.bar(catch_10, x='PLAYER', y='CATCHES',
                     hover_data=['PLAYER','CATCHES','TEAM','OPPOSITION'], color='CATCHES',
                     #labels={'pop': 'population of Canada'},
                     height=400)

        return [
            dcc.Graph(figure=fig_1),
            html.Div(df1_fig)
            #bat_table
        ]

import dash
from dash import html,dcc, dash_table, Output, Input, State
import dash_bootstrap_components as dbc
from .sidebar_2010_ipl import sidebar
import pandas as pd
import plotly.figure_factory as ff
import plotly.express as px

dash.register_page(__name__,name = 'LARGEST VICTORIES',order=8)

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
                    html.H3('LARGEST VICTORIES - 2010 IPL', style={'textAlign':'center'}),
                    html.Br(),
                    html.Div([dcc.Dropdown(['LARGEST VICTORY BY RUNS', 'LARGEST VICTORY BY WICKETS'], id='request_victory_ipl_2010')]),
                    html.Br(),
                    html.Div(
                        [
                            dbc.Button("SUBMIT", id="inp-button", className="data_input", n_clicks=0),
                        ], style={"display": "flex", "justifyContent": "center"},
                    ),
                    html.Br(),
                    html.Div([], id='service_1_victory_ipl_2010'),
                    html.Br(),
                    html.Div([], id='service_2_victory_ipl_2010')
                ], xs=8, sm=8, md=10, lg=10, xl=10, xxl=10)
        ]
    )
])

@dash.callback(

    [
        Output('service_1_victory_ipl_2010','children'),
        Output('service_2_victory_ipl_2010','children'),
    ],

    [
        #Input('teams', "value"),
        Input('inp-button', "n_clicks")
    ],

    [
        State("request_victory_ipl_2010", 'value'),
        State('service_1_victory_ipl_2010','children'),
        State('service_2_victory_ipl_2010','children'),
    ],

        prevent_initial_call=True,

    )

def output(n_clicks,need,o1,o2):

    victory_by_wickets = pd.read_excel('assets/IPL/2010_ipl/largest_victories_by_wickets_ipl_2010.xlsx')
    victory_by_runs = pd.read_excel('assets/IPL/2010_ipl/largest_victories_by_runs_ipl_2010.xlsx')

    if need == 'LARGEST VICTORY BY RUNS':

        victory_by_runs = victory_by_runs[['WINNER','TARGET','MARGIN','MARGIN RUNS','MATCH','GROUND']]
        victory_by_runs = victory_by_runs.sort_values(by=['MARGIN RUNS'],ascending = False)
        df1_fig = dbc.Table.from_dataframe(victory_by_runs, striped=True, bordered=True, hover=True)

        #victory_by_runs = victory_by_runs.iloc[::-1]
        #victory_by_runs = victory_by_runs

        fig_1 = px.scatter(victory_by_runs.head(10), x='MATCH', y='MARGIN RUNS',
                     hover_data=['WINNER','TARGET','MARGIN RUNS','MATCH','GROUND'], color='MATCH',
                     #labels={'pop': 'population of Canada'},
                     height=400)
        fig_1.update_traces(marker=dict(size=50))

        return [
            dcc.Graph(figure=fig_1),
            html.Div(df1_fig)
            #bat_table
        ]

    if need == 'LARGEST VICTORY BY WICKETS':

        victory_by_wickets = victory_by_wickets[['WINNER','BALLS REMAINING','MARGIN','TARGET','MATCH','GROUND']]
        df1_fig = dbc.Table.from_dataframe(victory_by_wickets, striped=True, bordered=True, hover=True)


        victory_by_wickets = victory_by_wickets.iloc[::-1]
        #victory_by_runs = victory_by_runs

        fig_1 = px.scatter(victory_by_wickets.tail(10), x='MATCH', y='MARGIN',
                     hover_data=['WINNER','BALLS REMAINING','MARGIN','TARGET','MATCH','GROUND'], color='MATCH',
                     #labels={'pop': 'population of Canada'},
                     height=400)
        fig_1.update_traces(marker=dict(size=50))

        return [
            dcc.Graph(figure=fig_1),
            html.Div(df1_fig)
            #bat_table
        ]
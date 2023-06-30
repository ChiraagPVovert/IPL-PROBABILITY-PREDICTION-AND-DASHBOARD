import dash
from dash import dcc, html, callback, Output, Input, State
import plotly.express as px
import dash_bootstrap_components as dbc
import plotly.figure_factory as ff
import pandas as pd
import EDA_TEAM

dash.register_page(__name__,name = 'TEAM ANALYSIS' , order=1100000000000000,
                   meta_tags=[{'name': 'viewport',
                               'content': 'width=device-width, initial-scale=1.0, maximum-scale=1.2, minimum-scale=0.5,'
                             }]
                   )

df = EDA_TEAM.win_percentage()

fig1 = px.bar(df,x = 'TEAM',y = 'WIN-PERCENTAGE',color='WIN-PERCENTAGE',hover_data=['TEAM','TOTAL_MATCHES','TOTAL_WINS'])


layout = [
    html.Div([
    dbc.Row(
        [
            dbc.Col(
                [
                    html.H3('TEAM STATS IN IPL', style={'textAlign': 'center'}),
                    html.Br(),
                    html.Br(),
                    html.H5('WIN PERCENTAGE OF TEAMS IN IPL', style={'textAlign': 'center'}),
                    html.Br(),
                    # dash_table.DataTable(df1.to_dict('records'), [{"name": i, "id": i} for i in df.columns]),
                    dcc.Graph(figure=fig1),
                    html.Br(),
                    html.Br(),
                    html.H5('TEAM STATS IN IPL', style={'textAlign': 'center'}),
                    html.Br(),
                    html.Div([dcc.Dropdown(['MOST MATCHES PLAYED','MOST FINALS PLAYED','MOST FINALS WON',
                                            ], id='request_team_stats_ipl')]),
                    html.Br(),
                    html.Div(
                        [
                            dbc.Button("SUBMIT", id="inp-button", className="data_input", n_clicks=0),
                        ], style={"display": "flex", "justifyContent": "center"},
                    ),
                    html.Div([], id='request_team_stats_fig_ipl'),
                    html.Br(),
                    html.Div([], id='request_team_stats_table_ipl'),
                ], #xs=8, sm=8, md=10, lg=10, xl=10, xxl=10
            ),

        ]
    ),
])
]


@dash.callback(

    [
        Output('request_team_stats_fig_ipl','children'),
        Output('request_team_stats_table_ipl','children'),
    ],

    [
        #Input('teams', "value"),
        Input('inp-button', "n_clicks")
    ],

    [
        State("request_team_stats_ipl", 'value'),
        State('request_team_stats_fig_ipl','children'),
        State('request_team_stats_table_ipl','children'),
    ],

        prevent_initial_call=True,

    )

def output(n_clicks,need,o1,o2):

    if need == 'MOST MATCHES PLAYED':

        df = EDA_TEAM.total_matches()

        df1_fig = dbc.Table.from_dataframe(df, striped=True, bordered=True, hover=True)

        fig_1 = px.bar(df, x='TEAM', y='TOTAL_MATCHES', color='TOTAL_MATCHES',hover_data=['TEAM', 'TOTAL_MATCHES', 'TOTAL_WINS'])


        return [
            dcc.Graph(figure=fig_1),
            html.Div(df1_fig)
            #bat_table
        ]

    elif need == 'MOST FINALS PLAYED':

        df = EDA_TEAM.total_finals_played()

        df1_fig = dbc.Table.from_dataframe(df, striped=True, bordered=True, hover=True)

        fig_1 = px.bar(df, x='TEAM', y='TOTAL_FINALS_PLAYED', color='TOTAL_FINALS_PLAYED',hover_data=['TEAM', 'TOTAL_FINALS_PLAYED'])

        return [
            dcc.Graph(figure=fig_1),
            html.Div(df1_fig)
            #bat_table
        ]

    elif need == 'MOST FINALS WON':

        df = EDA_TEAM.total_finals_won()

        df1_fig = dbc.Table.from_dataframe(df, striped=True, bordered=True, hover=True)

        fig_1 = px.bar(df, x='TEAM', y='TOTAL_FINALS_WON', color='TOTAL_FINALS_WON',hover_data=['TEAM', 'TOTAL_FINALS_WON'])

        return [
            dcc.Graph(figure=fig_1),
            html.Div(df1_fig)
            #bat_table
        ]

    elif need == 'MOST QUALIFIER 1 PLAYED':

        df = EDA_TEAM.most_qualifier1_played()

        df1_fig = dbc.Table.from_dataframe(df, striped=True, bordered=True, hover=True)

        fig_1 = px.bar(df, x='TEAM', y='TOTAL QUALIFIERS 1 PLAYED', color='TOTAL QUALIFIERS 1 PLAYED',hover_data=['TEAM', 'TOTAL QUALIFIERS 1 PLAYED'])

        return [
            dcc.Graph(figure=fig_1),
            html.Div(df1_fig)
            #bat_table
        ]




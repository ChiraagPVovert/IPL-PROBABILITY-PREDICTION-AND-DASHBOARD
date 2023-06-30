import dash
from dash import dash_table
from dash import dcc, html, callback, Output, Input, State
import plotly.express as px
import dash_bootstrap_components as dbc
import Model_data_prediction
from dash.dash_table.Format import Group
import plotly.graph_objects as go
import plotly.figure_factory as ff
import pandas as pd


dash.register_page(__name__, name='TEAM ANALYSIS',order=0)

app = dash.Dash(__name__)


df = pd.read_excel('assets/Country_Stats/country_stats.xlsx')
df.reset_index(drop=True, inplace=True)
df = df.sort_values(by=['WIN-PERCENTAGE'], ascending=False)

fig1 = px.bar(df,x = 'COUNTRY',y = 'WIN-PERCENTAGE',color='GROUP STAGE MATCHES',hover_data=['WON','LOST'])

layout = [
     html.Div([
    dbc.Row(
        [
            dbc.Col(
                [
                    html.H3('TEAM STATS IN WORLD CUPS', style={'textAlign': 'center'}),
                    html.Br(),
                    html.Br(),
                    html.H5('WIN PERCENTAGE OF COUNTRIES IN WORLD CUPS', style={'textAlign': 'center'}),
                    html.Br(),
                    # dash_table.DataTable(df1.to_dict('records'), [{"name": i, "id": i} for i in df.columns]),
                    dcc.Graph(figure=fig1),
                    html.Br(),
                    html.Br(),
                    html.H5('TEAM STATS IN ODI WORLD CUPS', style={'textAlign': 'center'}),
                    html.Br(),
                    html.Div([dcc.Dropdown(['GROUP STAGE MATCHES PLAYED','QUARTER FINALS PLAYED',
                                            'SEMI FINALS PLAYED','FINALS PLAYED','TOTAL MATCHES WON',
                                            'TOTAL MATCHES LOST','TOTAL MATCHES PLAYED'], id='request_team_stats')]),
                    html.Br(),
                    html.Div(
                        [
                            dbc.Button("SUBMIT", id="inp-button", className="data_input", n_clicks=0),
                        ], style={"display": "flex", "justifyContent": "center"},
                    ),
                    html.Div([], id='request_team_stats_fig'),
                    html.Br(),
                    html.Div([], id='request_team_stats_table'),
                ], #xs=8, sm=8, md=10, lg=10, xl=10, xxl=10
            ),

        ]
    ),
])
]


@dash.callback(

    [
        Output('request_team_stats_fig','children'),
        Output('request_team_stats_table','children'),
    ],

    [
        #Input('teams', "value"),
        Input('inp-button', "n_clicks")
    ],

    [
        State("request_team_stats", 'value'),
        State('request_team_stats_fig','children'),
        State('request_team_stats_table','children'),
    ],

        prevent_initial_call=True,

    )

def output(n_clicks,need,o1,o2):

    df = pd.read_excel('assets/Country_Stats/country_stats.xlsx')
    df.reset_index(drop=True, inplace=True)

    if need == 'GROUP STAGE MATCHES PLAYED':
        df = df.sort_values(by=['GROUP STAGE MATCHES'],ascending=False)
        df_data = df[['COUNTRY','GROUP STAGE MATCHES']]
        df_data = df_data.sort_values(['GROUP STAGE MATCHES'],ascending=False)
        df1_fig = ff.create_table(df_data, index=False)

        fig_1 = px.bar(df_data, x='GROUP STAGE MATCHES', y='COUNTRY',
                     #labels={'pop': 'population of Canada'},
                      )

        return [
            dcc.Graph(figure=fig_1),
            dcc.Graph(figure=df1_fig)
            #bat_table
        ]

    elif need == 'QUARTER FINALS PLAYED':
        df = df.sort_values(by=['QUARTER FINALS PLAYED'],ascending=False)
        df_data = df[['COUNTRY','QUARTER FINALS PLAYED']]
        df_data = df_data.sort_values(['QUARTER FINALS PLAYED'],ascending=False)
        df1_fig = ff.create_table(df_data, index=False)

        fig_1 = px.bar(df_data, x='QUARTER FINALS PLAYED', y='COUNTRY',
                     #labels={'pop': 'population of Canada'},
                      )

        return [
            dcc.Graph(figure=fig_1),
            dcc.Graph(figure=df1_fig)
            #bat_table
        ]

    elif need == 'SEMI FINALS PLAYED':
        df = df.sort_values(by=['SEMI FINALS PLAYED'],ascending=False)
        df_data = df[['COUNTRY','SEMI FINALS PLAYED']]
        df_data = df_data.sort_values(['SEMI FINALS PLAYED'],ascending=False)
        df1_fig = ff.create_table(df_data, index=False)

        fig_1 = px.bar(df_data, x='SEMI FINALS PLAYED', y='COUNTRY',
                     #labels={'pop': 'population of Canada'},
                      )

        return [
            dcc.Graph(figure=fig_1),
            dcc.Graph(figure=df1_fig)
            #bat_table
        ]

    elif need == 'FINALS PLAYED':
        df = df.sort_values(by=['FINALS PLAYED'],ascending=False)
        df_data = df[['COUNTRY','FINALS PLAYED']]
        df_data = df_data.sort_values(['FINALS PLAYED'],ascending=False)
        df1_fig = ff.create_table(df_data, index=False)

        fig_1 = px.bar(df_data, x='FINALS PLAYED', y='COUNTRY',
                     #labels={'pop': 'population of Canada'},
                      )

        return [
            dcc.Graph(figure=fig_1),
            dcc.Graph(figure=df1_fig)
            #bat_table
        ]

    elif need == 'TOTAL MATCHES WON':
        df = df.sort_values(by=['WON'],ascending=False)
        df_data = df[['COUNTRY','WON']]
        df_data = df_data.sort_values(['WON'],ascending=False)
        df1_fig = ff.create_table(df_data, index=False)

        fig_1 = px.bar(df_data, x='WON', y='COUNTRY',
                     #labels={'pop': 'population of Canada'},
                      )

        return [
            dcc.Graph(figure=fig_1),
            dcc.Graph(figure=df1_fig)
            #bat_table
        ]

    elif need == 'TOTAL MATCHES LOST':
        df = df.sort_values(by=['LOST'],ascending=False)
        df_data = df[['COUNTRY','LOST']]
        df_data = df_data.sort_values(['LOST'],ascending=False)
        df1_fig = ff.create_table(df_data, index=False)

        fig_1 = px.bar(df_data, x='LOST', y='COUNTRY',
                     #labels={'pop': 'population of Canada'},
                      )

        return [
            dcc.Graph(figure=fig_1),
            dcc.Graph(figure=df1_fig)
            #bat_table
        ]

    elif need == 'TOTAL MATCHES PLAYED':
        df = df.sort_values(by=['TOTAL MATCHES'], ascending=False)
        df_data = df[['COUNTRY', 'TOTAL MATCHES']]
        df_data = df_data.sort_values(['TOTAL MATCHES'], ascending=False)
        df1_fig = ff.create_table(df_data, index=False)

        fig_1 = px.bar(df_data, x='TOTAL MATCHES', y='COUNTRY',
                       # labels={'pop': 'population of Canada'},
                      )

        return [
            dcc.Graph(figure=fig_1),
            dcc.Graph(figure=df1_fig)
            # bat_table
        ]
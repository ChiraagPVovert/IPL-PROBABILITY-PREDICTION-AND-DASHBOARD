import dash
from dash import html, dcc, Input, Output, State, callback,dash_table
import dash_bootstrap_components as dbc
import plotly.express as px
import pandas as pd
from .sidebar_2010_ipl import sidebar
import plotly.graph_objects as go
import plotly.figure_factory as ff

dash.register_page(__name__, name = '2010 IPL', order=1111110000000000000,
                   meta_tags=[{'name': 'viewport',
                               'content': 'width=device-width, initial-scale=1.0, maximum-scale=1.2, minimum-scale=0.5,'
                               }]
                   )

df = pd.read_excel('assets/IPL/2010_ipl/points_table_ipl_2010.xlsx')
df = df.fillna(' ')
df.reset_index(drop=True, inplace=True)

fig = go.Figure(data=[go.Pie(labels=df.TEAMS, values=df.POINTS, pull=[0.1, 0.1, 0.1, 0.1, 0.3, 0.3, 0.3, 0.3])])


#df_fig = ff.create_table(df, index=False)
#for i in range(len(df_fig.layout.annotations)):
    #df_fig.layout.annotations[i].font.size = 8

df_fig = dbc.Table.from_dataframe(df, striped=True, bordered=True, hover=True)

def layout():
    return html.Div([
    dbc.Row(
        [
            dbc.Col(
                [
                    sidebar()
                ], xs=4, sm=4, md=2, lg=2, xl=2, xxl=2
            ),
            dbc.Col(
                [
                    html.H3('POINTS TABLE - 2010 IPL', style={'textAlign': 'center'}),
                    html.Br(),
                    html.Div(df_fig),
                    html.Br(),
                    #html.Div(fig),
                    dcc.Graph(figure=fig),
                    html.Br(),
                ], xs=8, sm=8, md=10, lg=10, xl=10, xxl=10
            ),

        ]
    ),

])






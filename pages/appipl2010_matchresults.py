import dash_bootstrap_components as dbc
from .sidebar_2010_ipl import sidebar
import pandas as pd
import plotly.figure_factory as ff
import plotly.express as px
import dash
from dash import html,dcc

dash.register_page(__name__,name = 'MATCH RESULTS',order=10)

df = pd.read_excel('assets/IPL/2010_ipl/match_results_ipl_2010.xlsx')
df.reset_index(drop=True, inplace=True)

#fig1 = px.line(df.tail(10),x = 'Match',y = 'Runs',hover_data=['Match','Runs','Wkts'])

df1 = df[['MATCH','TEAM WON','GROUND']]
df1_fig = dbc.Table.from_dataframe(df1, striped=True, bordered=True, hover=True)
#df1_fig = ff.create_table(df1, index=False)
#for i in range(len(df1_fig.layout.annotations)):
    #df1_fig.layout.annotations[i].font.size = 15


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
                    html.H3('MATCH RESULTS - 2010 IPL', style={'textAlign':'center'}),
                    html.Br(),
                    html.Div(df1_fig),
                    html.Br(),
                    html.Br(),
                    html.H5(''),
                    html.Br(),
                    html.H5(''),
                ], xs=8, sm=8, md=10, lg=10, xl=10, xxl=10)

        ]
    )
])

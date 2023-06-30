import dash_bootstrap_components as dbc
from .sidebar_2008_ipl import sidebar
import pandas as pd
import plotly.figure_factory as ff
import plotly.express as px
import dash
from dash import html,dcc

dash.register_page(__name__,name = 'MATCH AGGREGATES',order=9)

df = pd.read_excel('assets/IPL/2008_ipl/highest_match_aggregates_ipl_2008.xlsx')
df.reset_index(drop=True, inplace=True)

fig1 = px.scatter(df.head(10),x = 'MATCH',y = 'RUNS',hover_data=['MATCH','RUNS','WICKETS'])
fig1.update_traces(marker_size=20)


df1 = df[['MATCH','RUNS','WICKETS','OVERS','GROUND']]

df1_fig = dbc.Table.from_dataframe(df1, striped=True, bordered=True, hover=True)



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
                    html.H3('MATCH AGGREGATES - 2008 IPL', style={'textAlign': 'center'}),
                    html.Br(),
                    #dash_table.DataTable(df1.to_dict('records'), [{"name": i, "id": i} for i in df.columns]),
                    dcc.Graph(figure=fig1),
                    html.Br(),
                    html.Div(df1_fig),
                    html.Br(),
                ], xs=8, sm=8, md=10, lg=10, xl=10, xxl=10),

        ]
    ),
])
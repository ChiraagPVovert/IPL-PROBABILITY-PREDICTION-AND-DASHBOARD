import dash_bootstrap_components as dbc
from .sidebar_2008_ipl import sidebar
import pandas as pd
import plotly.figure_factory as ff
import plotly.express as px
import dash
from dash import html,dcc

dash.register_page(__name__,name = 'MATCH RESULTS',order=10)

df = pd.read_excel('assets/IPL/2008_ipl/match_results_ipl_2008.xlsx')
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
                    html.H3('MATCH RESULTS - 2008 IPL', style={'textAlign':'center'}),
                    html.Br(),
                    html.Div(df1_fig),
                    html.Br(),
                    html.Br(),
                    html.H5('The Indian Premier League was formed by the BCCI in 2007 and played its inaugural season in 2008. The season began on April 18, 2008, and the final game was played on June 1, 2008. Each of the eight teams in the competition played both home and away matches against every other team during the double round robin league stage of the competition. Following these games, two semi-finals and a final were played.'),
                    html.Br(),
                    html.H5('Rajasthan Royals defeated Chennai Super Kings in the championship game, which came down to the final ball. Yusuf Pathan was chosen player of the match in the Finals, and Shane Watson was voted player of the tournament. For capturing the most wickets in the competition, Sohail Tanvir received the purple cap, and Shaun Marsh received the orange cap for scoring the most runs. The best under-19 player award went to Shreevats Goswami, and the CSK team took up the special Fair Play trophy.'),

                ], xs=8, sm=8, md=10, lg=10, xl=10, xxl=10)

        ]
    )
])

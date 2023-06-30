import dash
from dash import Dash, html, dcc, Input, Output
import dash_bootstrap_components as dbc
from dash_bootstrap_templates import ThemeSwitchAIO

app = dash.Dash(__name__, use_pages=True, external_stylesheets=[dbc.themes.MATERIA,dbc.themes.GRID],
		meta_tags=[{'name': 'viewport',
                    'content': 'width=device-width, initial-scale=1.0, maximum-scale=1.2, minimum-scale=0.5,'
                    }]
                ,)

theme_switch = ThemeSwitchAIO(aio_id="theme", themes=[dbc.themes.MATERIA, dbc.themes.CYBORG])

PLOTLY_LOGO = 'https://overtideasandsolutions.in/wp-content/uploads/2021/11/overt-ideas-logo-1-370x70.png'

SIDEBAR = dbc.Navbar(
    dbc.Container(
        [
            dbc.Row([
                dbc.NavbarToggler(id="navbar-toggler"),
                    dbc.Nav([
                        dbc.Col
                            ([
                        dbc.NavLink(page["name"], href=page["path"])
                        for page in dash.page_registry.values()
                        if not page["path"].startswith("/app")
                            ])
                    ])
            ])
        ],
        fluid=True,
    ),
    color="primary",
    dark=True,
)

#app.layout = dbc.Container([header, dash.page_container], fluid=False)

app.layout = dbc.Container([
    dbc.Row(
        [
            dbc.Col(html.Div(html.H2("CRIC-OVERT | IPL")),align='center'),
            dbc.Col(html.Div(html.Img(src=PLOTLY_LOGO)),align='center'),
            dbc.Col(html.Div(theme_switch), align='center')
        ],style={'textAlign':'center','height':'7rem'}
    ),

    html.Hr(),

    dbc.Row(
        [
            dbc.Col(
                [
                    SIDEBAR
                ], #xs=4, sm=4, md=2, lg=2, xl=2, xxl=2
                   ),

            dbc.Col(
                [
                    dash.page_container
                ], xs=8, sm=8, md=10, lg=10, xl=10, xxl=10
                   )
        ]
    )
],fluid=True)


if __name__ == '__main__':
	app.run_server(debug=True,port = 8053)# host = "0.0.0.0")
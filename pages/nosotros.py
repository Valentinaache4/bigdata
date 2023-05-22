import dash
from dash import html
import dash_bootstrap_components as dbc

app = dash.Dash(__name__, external_stylesheets=[dbc.themes.BOOTSTRAP, "style.css","https://use.fontawesome.com/releases/v5.15.3/css/all.css"])
app.config.suppress_callback_exceptions = True


def layout():
    return html.Div(
        [
            html.H1("Equipo"),
            html.Br(),
            dbc.Row(
                [
                    dbc.Col(
                        [
                            dbc.Card(
                                [
                                    dbc.CardBody(
                                        [
                                            html.H5("Valentina Acosta", className="card-title"),
                                            html.P("Profesión: Ingeniera en Informática", className="card-text"),
                                            html.P("Edad: 23 años", className="card-text"),
                                            html.P("Hobby: Ultimate", className="card-text"),
                                        ]
                                    ),
                                ],
                                className="text-center",
                                style={"width": "18rem", "margin-bottom": "20px", "border-color": "#000080"},
                            ),
                        ],
                        width=4,
                    ),
                    dbc.Col(
                        [
                            dbc.Card(
                                [
                                    dbc.CardBody(
                                        [
                                            html.H5("Diego Andrés Bonilla Perdomo", className="card-title"),
                                            html.P("Profesión: Ingeniero en informática", className="card-text"),
                                            html.P("Edad: 23 años", className="card-text"),
                                            html.P("Hobby: Video juegos", className="card-text"),
                                        ]
                                    ),
                                ],
                                className="text-center",
                                style={"width": "18rem", "margin-bottom": "20px", "border-color": "#000080"},
                            ),
                        ],
                        width=4,
                    ),
                    dbc.Col(
                        [
                            dbc.Card(
                                [
                                    dbc.CardBody(
                                        [
                                            html.H5("Angela Alarcon ", className="card-title"),
                                            html.P("Profesión: Administradora de empresas", className="card-text"),
                                            html.P("Edad: 32 años", className="card-text"),
                                            html.P("Hobby: Jugar tennis", className="card-text"),
                                        ]
                                    ),
                                ],
                                className="text-center",
                                style={"width": "18rem", "margin-bottom": "20px", "border-color": "#000080"},
                            ),
                        ],
                        width=4,
                    ),
                    dbc.Col(
                        [
                            dbc.Card(
                                [
                                    dbc.CardBody(
                                        [
                                            html.H5("Katheryn Tibambre Oviedo", className="card-title"),
                                            html.P("Profesión: Contadora Pública", className="card-text"),
                                            html.P("Edad: 27 años", className="card-text"),
                                            html.P("Hobby: Montar Bici", className="card-text"),
                                        ]
                                    ),
                                ],
                                className="text-center",
                                style={"width": "18rem", "margin-bottom": "20px", "border-color": "#000080"},
                            ),
                        ],
                        width=4,
                    ),
                    dbc.Col(
                        [
                            dbc.Card(
                                [
                                    dbc.CardBody(
                                        [
                                            html.H5("Juan Felipe Garnica Galvis", className="card-title"),
                                            html.P("Estudiante de Ingeniería Industrial", className="card-text"),
                                            html.P("Edad: 20 años", className="card-text"),
                                            html.P("Hobby: Ver películas y series", className="card-text"),
                                        ]
                                    ),
                                ],
                                className="text-center",
                                style={"width": "18rem", "margin-bottom": "20px", "border-color": "#000080"},
                            ),
                        ],
                        width=4,
                    ),
                    dbc.Col(
                        [
                            dbc.Card(
                                [
                                    dbc.CardBody(
                                        [
                                            html.H5("Juan David Fajardo Parra", className="card-title"),
                                            html.P("Profesión: Ingeniero industrial con énfasis en analítica de datos", className="card-text"),
                                            html.P("Edad: 22 años", className="card-text"),
                                            html.P("Hobby: Leer y ver series de ciencia ficción", className="card-text"),
                                        ]
                                    ),
                                ],
                                className="text-center",
                                style={"width": "18rem", "margin-bottom": "20px", "border-color": "#000080"},
                            ),
                        ],
                        width=4,
                    ),
                ],
                className="justify-content-center",
            ),
        ],
        className="container",
    )


if __name__ == "__main__":
    app.layout = layout
    app.run_server(host='localhost', port=8050, debug=True)

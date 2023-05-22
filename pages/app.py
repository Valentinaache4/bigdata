import dash
import csv
from dash import html
from dash import dcc
import dash_bootstrap_components as dbc
from dash.dependencies import Input, Output
import nosotros
import plotly.graph_objects as go
import pandas as pd
import plotly.express as px

app = dash.Dash(__name__, external_stylesheets=[dbc.themes.BOOTSTRAP, "style.css","https://use.fontawesome.com/releases/v5.15.3/css/all.css"])
app.config.suppress_callback_exceptions = True

# Abre el archivo CSV y encuentra el valor máximo en la columna 'revenue'
max_revenue = max(
    csv.DictReader(open('data/movies_metadata.csv', encoding='utf-8')),
    key=lambda x: float(x['revenue']) if x['revenue'] is not None else float('-inf')
)

data = pd.read_csv('data/movies_metadata.csv')

# Convertir las columnas 'budget' y 'revenue' a números
data['budget'] = pd.to_numeric(data['budget'], errors='coerce')
data['revenue'] = pd.to_numeric(data['revenue'], errors='coerce')
data['popularity'] = pd.to_numeric(data['popularity'], errors='coerce')

# Calcular el promedio de las columnas 'budget', 'revenue', 'popularity', 'return'
average_budget = data['budget'].mean()
average_revenue = data['revenue'].mean()
average_popularity = data['popularity'].mean()
average_return = (data['revenue'] - data['budget']).mean()

# Calcular la columna 'return' (retorno de inversión) como la diferencia entre 'revenue' y 'budget'
data['return'] = data['revenue'] - data['budget']

# Ordenar los datos por la columna 'budget' en orden descendente
sorted_data = data.sort_values('budget', ascending=False)

# Tomar las primeras 10 filas (las películas más caras en producir)
top_10_expensive_movies = sorted_data.head(10)

# Crear el gráfico de barras
fig = go.Figure(data=[
    go.Bar(x=top_10_expensive_movies['title'],
           y=top_10_expensive_movies['budget'],
           name='Presupuesto',
           marker=dict(color='#4a90ae')),
    go.Bar(x=top_10_expensive_movies['title'],
           y=top_10_expensive_movies['return'],
           name='Retorno de inversión',
           marker=dict(color='#2ecc71'))
])

# Personalizar el diseño del gráfico
fig.update_layout(
    title='Películas más caras en producir y su retorno de inversión',
    xaxis_title='Película',
    yaxis_title='Valor en millones',
    barmode='group'
)

# Convertir la columna 'release_date' a tipo fecha
data['release_date'] = pd.to_datetime(data['release_date'], errors='coerce')

# Obtener el conteo de películas por día de la semana
movies_by_weekday = data['release_date'].dt.day_name().value_counts().sort_index()

# Obtener el conteo de películas por mes del año
movies_by_month = data['release_date'].dt.month_name().value_counts().sort_index()

movies_by_year = data['release_date'].dt.year.value_counts().nlargest(10).sort_index()

# Calcular el retorno de inversión promedio por idioma original
average_return_by_language = data.groupby('original_language')['return'].mean().reset_index()

# Ordenar los idiomas por el retorno de inversión promedio de manera descendente
sorted_languages = average_return_by_language.sort_values('return', ascending=False)

# Crear el gráfico de barras
bar_fig = px.bar(sorted_languages, x='original_language', y='return',
                 color='original_language',
                 title='Retorno de Inversión por Idioma Original')

# Personalizar el diseño del gráfico
bar_fig.update_layout(
    xaxis_title='Idioma Original',
    yaxis_title='Retorno de Inversión'
)

# Definir el diseño del menú de navegación
navbar = dbc.NavbarSimple(
    children=[
        dbc.NavItem(dbc.NavLink("Inicio", href="/inicio")),
        dbc.NavItem(dbc.NavLink("Nosotros", href="/nosotros")),
    ],
    brand=None,
    brand_href="/",
    color="#000080",
    dark=True,
)

# Definir el diseño de la página Nosotros
nosotros_page = nosotros.layout()

app.layout = html.Div(
    [
        dcc.Location(id="url", refresh=False),
        navbar,
        html.Div(id="page-content"),
        
        html.Br(),
        dbc.Container(
            [
                html.H3(
                    "Visualización para el Mundo del Cine",
                    style={
                        'text-align': 'center',
                        'font-family': 'cursive',
                        'color': '#191970'
                    }
                ),
                html.Br(),
                html.Br(),
                dbc.Row(
                    [
                        dbc.Col(
                            [
                                html.Div(
                                    [
                                        html.P("Presupuesto Promedio", style={"font-weight": "bold"}),
                                        html.P(average_budget)
                                    ],
                                    className='card',
                                    style={
                                        "padding": "20px",
                                        "border": "2px solid #000080",
                                        "box-shadow": "0 2px 4px rgba(0, 0, 0, 0.2)",
                                        "margin-bottom": "20px",
                                        "font-family": "Verdana"  
                                       },
                                )
                            ],
                            className='col-md-3'
                        ),
                        dbc.Col(
                            [
                                html.Div(
                                    [
                                        html.P("Popularidad Promedio", style={"font-weight": "bold"}),
                                        html.P(average_popularity)
                                    ],
                                    className='card',
                                    style={
                                        "padding": "20px",
                                        "border": "2px solid #000080",
                                        "box-shadow": "0 2px 4px rgba(0, 0, 0, 0.2)",
                                        "margin-bottom": "20px",
                                        "font-family": "Verdana"
                                    },
                                )
                            ],
                            className='col-md-3'
                        ),
                        dbc.Col(
                            [
                                html.Div(
                                    [
                                        html.P("Retorno de Inversión Promedio", style={"font-weight": "bold"}),
                                        html.P(average_return)
                                    ],
                                    className='card',
                                    style={
                                        "padding": "20px",
                                        "border": "2px solid #000080",
                                        "box-shadow": "0 2px 4px rgba(0, 0, 0, 0.2)",
                                        "margin-bottom": "20px",
                                        "font-family": "Verdana"
                                    },
                                )
                            ],
                            className='col-md-3'
                        ),
                        dbc.Col(
                            [
                                html.Div(
                                    [
                                        html.P("Ganancia Promedio", style={"font-weight": "bold"}),
                                        html.P(average_revenue)
                                    ],
                                    className='card',
                                    style={
                                        "padding": "20px",
                                        "border": "2px solid #000080",
                                        "box-shadow": "0 2px 4px rgba(0, 0, 0, 0.2)",
                                        "margin-bottom": "20px",
                                        "font-family": "Verdana"
                                    },
                                )
                            ],
                            className='col-md-3'
                        )
                    ],
                    className='row'
                ),
                dbc.Row(
                    [
                        dbc.Col(
                            [
                                dcc.Graph(figure=fig)
                            ],
                            className='col-md-6'
                        ),
                        dbc.Col(
                            [
                                html.Div(
                                    [
                                        dcc.RadioItems(
                                            id='selector',
                                            options=[
                                                {'label': 'Días de la semana', 'value': 'weekday'},
                                                {'label': 'Meses del año', 'value': 'month'},
                                                {'label': 'Años con más películas', 'value': 'year'}
                                            ],
                                            value='weekday',
                                            labelStyle={'display': 'inline-block', 'width': '200px', 'text-align': 'center', 'margin': 'auto'}
                                        ),
                                        dcc.Graph(id='bar-chart')
                                    ],
                                    className='card',
                                    style={
                                        "padding": "20px",
                                        "border": "#4a90ae",
                                        "box-shadow": "0 2px 4px rgba(0, 0, 0, 0.2)",
                                        "margin-bottom": "20px"
                                    }
                                )
                            ],
                            className='col-md-6'
                        )
                    ],
                    className='row'
                ),
                dbc.Row(
                    dbc.Col(
                        html.Div(
                            dcc.Graph(figure=bar_fig),
                        )

                    )
                )
            ]
        )
    ]
)

# Actualizar la página según la URL
@app.callback(Output("page-content", "children"), [Input("url", "pathname")])
def display_page(pathname):
    if pathname == "/nosotros":
        return nosotros_page
    

@app.callback(
    Output('bar-chart', 'figure'),
    [Input('selector', 'value')]
)
def update_bar_chart(selector):
    if selector == 'weekday':
        data_plot = movies_by_weekday
        x_label = 'Día de la semana'
    elif selector == 'month':
        data_plot = movies_by_month
        x_label = 'Mes del año'
    else:
        data_plot = movies_by_year
        x_label = 'Año'

    fig = px.bar(
        title='Películas producidas por día, mes o año',
        x=data_plot.index,
        y=data_plot.values,
        labels={'x': x_label, 'y': 'Cantidad de películas'}
    )

    return fig


if __name__ == "__main__":
    app.run_server(host='localhost', port=8050, debug=True)

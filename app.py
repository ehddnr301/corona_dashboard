
import dash
import dash_core_components as dcc
import dash_html_components as html
import plotly.express as px
from builder import make_table
from data import countries_df
from coronaMap import corona_map
from bar import bar_chart

stylesheets = [
    'https://cdn.jsdelivr.net/npm/reset-css@5.0.1/reset.min.css',
    'https://fonts.googleapis.com/css2?family=Jua&display=swap'
]

app = dash.Dash(__name__, external_stylesheets=stylesheets)

app.layout = html.Div(
    style={
        'minHeight': '100vh',
        'backgroundColor':'#111',
        'color':'white',
        'fontFamily': "Jua"
    },
    children = [
        html.Header(
            style={
                'textAlign': 'center',
                "paddingTop": "50px"
            },
            children=[
                html.H1('Corona Dashboard', style= {"fontSize":50})
            ]
        ),
        html.Div(
            style={
                'display':'grid',
                'gap': 30,
                'gridTemplateColumns':'repeat(4, 1fr)'
            },
            children=[
                html.Div(
                    children = [make_table(countries_df)]
                ),
                html.Div(
                    style={"grid-column": "span 3"},
                    children=[
                        dcc.Graph(figure=corona_map)
                    ]
                )
            ]
        ),
        html.Div(
            style={
                "display": "grid",
                "gap": 50,
                "gridTemplateColumns": "repeat(4, 1fr)",
            },
            children=[
                html.Div(children=[dcc.Graph(figure=bar_chart)])
            ]
        )
    ]
)

if __name__ == '__main__':
    app.run_server(debug=True)
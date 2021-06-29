import plotly.express as px
from data import countries_df

corona_map = px.scatter_geo(countries_df,
                     size='Confirmed',
                     size_max=30,
                     hover_name='Country_Region',
                     color='Confirmed',
                     locations='Country_Region',
                     locationmode='country names',
                     projection='orthographic',
                     color_continuous_scale=px.colors.sequential.Oryel,
                     title='Global Confirmed',
                     hover_data={
                         'Confirmed': ':,2f',
                         'Deaths': ':,2f',
                         'Recovered': ':,2f',
                         'Country_Region': False
                     },
                     template='plotly_dark'
                    )
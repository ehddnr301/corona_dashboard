import plotly.express as px
from data import totals_df

bar_chart = px.bar(totals_df,
            x='condition',
            y='count',
            title='Total Case',
            hover_data={
                'count': ':,'
            },
            labels={
                'condition' : 'Condition',
                'count': 'Count',
                'color': 'Condition'
            },
            # color=['Confirmed', 'Deaths', 'Recovered'],
            template='plotly_dark')

bar_chart.update_traces(
    marker_color=['#EDD491', '#EE4F5A', '#F18E5C']
)
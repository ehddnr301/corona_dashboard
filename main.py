import pandas as pd

daily_df = pd.read_csv('data/daily_report.csv')
daily_df = daily_df[['Confirmed', 'Deaths', 'Recovered']].sum().reset_index(name='count')
daily_df = daily_df.rename(columns={'index': 'condition'})
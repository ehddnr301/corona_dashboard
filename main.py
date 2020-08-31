import pandas as pd

daily_df = pd.read_csv("data/daily_report.csv")

total_df = (
    daily_df[["Confirmed", "Deaths", "Recovered"]].sum().reset_index(name="count")
)
total_df = total_df.rename(columns={"index": "condition"})

countries_df = daily_df[["Country_Region", "Confirmed", "Deaths", "Recovered"]]
countries_df = countries_df.groupby("Country_Region").sum().reset_index()

# time_df

time_df = pd.read_csv('data/time_confirmed.csv')
time_df = time_df.drop(['Province/State', 'Country/Region', 'Lat', 'Long'], axis=1)
time_df = time_df.sum().reset_index(name='total')
time_df = time_df.rename(columns={'index':'data'})
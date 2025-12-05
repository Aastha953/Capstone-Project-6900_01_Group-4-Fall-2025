import pandas as pd

# NOAA example: daily weather from Central Park station
url = "https://www.ncei.noaa.gov/access/services/data/v1?dataset=daily-summaries&stations=USW00094728&startDate=2024-01-01&endDate=2025-12-31&format=csv"
weather_df = pd.read_csv(url)

# Keep relevant columns
weather_df = weather_df[['DATE', 'TMAX', 'TMIN', 'PRCP', 'SNOW', 'AWND']]
weather_df['DATE'] = pd.to_datetime(weather_df['DATE'])

# Save for later merge
weather_df.to_csv("nyc_weather_2024_2025.csv", index=False)
print(weather_df.head())

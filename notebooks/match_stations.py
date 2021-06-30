## Imports

#general imports
import pandas as pd
import numpy as np

#statsmodels for regression
import statsmodels.api as sm
import statsmodels.formula.api as smf
from statsmodels.iolib.summary2 import summary_col

#scipy for testing
from scipy import stats

#for visualization
import matplotlib.pyplot as plt
import seaborn as sns

from datetime import datetime
import googlemaps
import csv
from datetime import datetime

## Bike Data
df_bikes = pd.read_csv('../data/philadelphia_2017.csv')
df_weather = pd.read_csv('../data/weather_hourly_philadelphia.csv')

#Get Station id's Mapped to Name
unique_station_ids = set(df_bikes['start_station_id'])
id_mapped_to_station = []
for id in unique_station_ids:
    this_station = []
    this_station.append(id)
    this_station.append(df_bikes.loc[df_bikes['start_station_id'] == id].iloc[0]['start_station_name'])
    id_mapped_to_station.append(this_station)

#Add Philadelphia to make it easier for Google
for stations in id_mapped_to_station:
    stations[1] += ", Philadelphia, PA"

gmaps = googlemaps.Client(key='MY_API_KEY_WHICH_IM_NOT_PUSHING_TO_GIT')

"""
This for loop makes an API Request for every Name, and fetches the lat and lng, and then writes it to a CSV
"""
for stations in id_mapped_to_station:
    row = gmaps.geocode(stations[1])
    lat = row[0]["geometry"]["location"]["lat"]
    lng = row[0]["geometry"]["location"]["lng"]
    with open('../data/geocodes.csv', 'a') as myfile:
        myfile.write(f'{stations[0]},{lat},{lng}\n')

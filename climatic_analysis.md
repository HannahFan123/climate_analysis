
# Climatic Analysis

Performing climatic analysis of Hawaii based on the temperature recorded on different stations


```python
# Python SQL toolkit and Object Relational Mapper
import sqlalchemy
from sqlalchemy.sql import label
from sqlalchemy import func
from sqlalchemy.ext.automap import automap_base
from sqlalchemy.orm import Session
from sqlalchemy import create_engine
import pandas as pd
from sqlalchemy import Column, Integer, String, Numeric, Text, Float,Table,ForeignKey
from flask import jsonify

import matplotlib.pyplot as plt
from matplotlib import cm
import matplotlib

from datetime import datetime,timedelta
```


```python
engine = create_engine("sqlite:///hawaii.sqlite")
```


```python
# reflect an existing database into a new model
Base = automap_base()
# reflect the tables
Base.prepare(engine, reflect=True)
```


```python
# We can view all of the classes that automap found
Base.classes.keys()
```




    ['measurement', 'station']




```python
# Save references to each table
Measurements = Base.classes.measurement
Stations = Base.classes.station
```


```python
# Create our session (link) from Python to the DB
session = Session(engine)
```

# Precipitation analysis


```python
# Design a query to retrieve the last 12 months of precipitation data and plot the result 

# Calculate the date 1 year ago from today

# Perform a query to retrieve the data and precipitation scores

# Save the query results as a Pandas DataFrame and set the index to the date column

# Sort the dataframe by date

def precipitation_data():
    current_time = datetime.now()

    past_year = current_time - timedelta(days=365)
    
    # Grabs the last date entry in the data table
    #last_date = session.query(Measurements.date).order_by(Measurements.date.desc()).first()
    #print(last_date)

    # to get the last 12 months of data, last date - 365
    #last_year = datetime.date(2017, 8, 23) - datetime.timedelta(days=365)
    
    #everytime I tried to pull from last entry - 365 I'd get a weird datetime error :(

    measurements_year = session.query(Measurements.date,Measurements.prcp).filter(
        Measurements.date > past_year).\
    order_by(Measurements.date.desc()).all()

    measure_list = []
    for measure in measurements_year:
        measure_list.append(measure._asdict())

    measurements_df = pd.DataFrame.from_records(measure_list)

    measurements_df = measurements_df.set_index('date')


    return measurements_df
```


```python
precipitation_data()
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>prcp</th>
    </tr>
    <tr>
      <th>date</th>
      <th></th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>2017-08-23</th>
      <td>0.00</td>
    </tr>
    <tr>
      <th>2017-08-23</th>
      <td>0.00</td>
    </tr>
    <tr>
      <th>2017-08-23</th>
      <td>0.08</td>
    </tr>
    <tr>
      <th>2017-08-23</th>
      <td>0.45</td>
    </tr>
    <tr>
      <th>2017-08-22</th>
      <td>0.00</td>
    </tr>
    <tr>
      <th>2017-08-22</th>
      <td>0.00</td>
    </tr>
    <tr>
      <th>2017-08-22</th>
      <td>0.50</td>
    </tr>
    <tr>
      <th>2017-08-21</th>
      <td>0.00</td>
    </tr>
    <tr>
      <th>2017-08-21</th>
      <td>0.02</td>
    </tr>
    <tr>
      <th>2017-08-21</th>
      <td>NaN</td>
    </tr>
    <tr>
      <th>2017-08-21</th>
      <td>0.56</td>
    </tr>
    <tr>
      <th>2017-08-20</th>
      <td>0.00</td>
    </tr>
    <tr>
      <th>2017-08-20</th>
      <td>0.01</td>
    </tr>
    <tr>
      <th>2017-08-20</th>
      <td>NaN</td>
    </tr>
    <tr>
      <th>2017-08-19</th>
      <td>0.00</td>
    </tr>
    <tr>
      <th>2017-08-19</th>
      <td>0.00</td>
    </tr>
    <tr>
      <th>2017-08-19</th>
      <td>NaN</td>
    </tr>
    <tr>
      <th>2017-08-19</th>
      <td>0.09</td>
    </tr>
    <tr>
      <th>2017-08-18</th>
      <td>0.00</td>
    </tr>
    <tr>
      <th>2017-08-18</th>
      <td>0.00</td>
    </tr>
    <tr>
      <th>2017-08-18</th>
      <td>0.06</td>
    </tr>
    <tr>
      <th>2017-08-18</th>
      <td>NaN</td>
    </tr>
    <tr>
      <th>2017-08-17</th>
      <td>0.00</td>
    </tr>
    <tr>
      <th>2017-08-17</th>
      <td>0.05</td>
    </tr>
    <tr>
      <th>2017-08-17</th>
      <td>0.01</td>
    </tr>
    <tr>
      <th>2017-08-17</th>
      <td>0.13</td>
    </tr>
    <tr>
      <th>2017-08-16</th>
      <td>0.00</td>
    </tr>
    <tr>
      <th>2017-08-16</th>
      <td>0.07</td>
    </tr>
    <tr>
      <th>2017-08-16</th>
      <td>0.12</td>
    </tr>
    <tr>
      <th>2017-08-16</th>
      <td>0.42</td>
    </tr>
    <tr>
      <th>...</th>
      <td>...</td>
    </tr>
    <tr>
      <th>2017-07-17</th>
      <td>0.12</td>
    </tr>
    <tr>
      <th>2017-07-17</th>
      <td>0.16</td>
    </tr>
    <tr>
      <th>2017-07-17</th>
      <td>0.00</td>
    </tr>
    <tr>
      <th>2017-07-17</th>
      <td>0.21</td>
    </tr>
    <tr>
      <th>2017-07-17</th>
      <td>0.39</td>
    </tr>
    <tr>
      <th>2017-07-16</th>
      <td>0.02</td>
    </tr>
    <tr>
      <th>2017-07-16</th>
      <td>0.07</td>
    </tr>
    <tr>
      <th>2017-07-16</th>
      <td>0.12</td>
    </tr>
    <tr>
      <th>2017-07-16</th>
      <td>0.00</td>
    </tr>
    <tr>
      <th>2017-07-16</th>
      <td>0.10</td>
    </tr>
    <tr>
      <th>2017-07-16</th>
      <td>0.50</td>
    </tr>
    <tr>
      <th>2017-07-15</th>
      <td>0.00</td>
    </tr>
    <tr>
      <th>2017-07-15</th>
      <td>0.03</td>
    </tr>
    <tr>
      <th>2017-07-15</th>
      <td>0.01</td>
    </tr>
    <tr>
      <th>2017-07-15</th>
      <td>0.00</td>
    </tr>
    <tr>
      <th>2017-07-15</th>
      <td>0.05</td>
    </tr>
    <tr>
      <th>2017-07-15</th>
      <td>0.10</td>
    </tr>
    <tr>
      <th>2017-07-14</th>
      <td>0.02</td>
    </tr>
    <tr>
      <th>2017-07-14</th>
      <td>0.05</td>
    </tr>
    <tr>
      <th>2017-07-14</th>
      <td>0.00</td>
    </tr>
    <tr>
      <th>2017-07-14</th>
      <td>0.00</td>
    </tr>
    <tr>
      <th>2017-07-14</th>
      <td>0.20</td>
    </tr>
    <tr>
      <th>2017-07-14</th>
      <td>0.68</td>
    </tr>
    <tr>
      <th>2017-07-13</th>
      <td>0.07</td>
    </tr>
    <tr>
      <th>2017-07-13</th>
      <td>0.33</td>
    </tr>
    <tr>
      <th>2017-07-13</th>
      <td>0.30</td>
    </tr>
    <tr>
      <th>2017-07-13</th>
      <td>NaN</td>
    </tr>
    <tr>
      <th>2017-07-13</th>
      <td>0.11</td>
    </tr>
    <tr>
      <th>2017-07-13</th>
      <td>0.32</td>
    </tr>
    <tr>
      <th>2017-07-13</th>
      <td>0.68</td>
    </tr>
  </tbody>
</table>
<p>212 rows × 1 columns</p>
</div>




```python
# Use Pandas Plotting with Matplotlib to plot the data
# Rotate the xticks for the dates

measurements_df = precipitation_data()
measurements_df.plot()#kind="line",LineWidth=4, figsize=(10,5))
plt.xlabel("Date")
plt.ylabel("Prcp in Inches")
plt.title("Precipitation Analysis")
plt.legend(["Precipitation"])
plt.grid()
plt.xticks(rotation=10)
#plt.show()
```




    (array([-50.,   0.,  50., 100., 150., 200., 250.]),
     <a list of 7 Text xticklabel objects>)




![png](output_11_1.png)



```python
# Use Pandas to calcualte the summary statistics for the precipitation data
measurements_df.describe()
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>prcp</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>count</th>
      <td>196.000000</td>
    </tr>
    <tr>
      <th>mean</th>
      <td>0.131531</td>
    </tr>
    <tr>
      <th>std</th>
      <td>0.370424</td>
    </tr>
    <tr>
      <th>min</th>
      <td>0.000000</td>
    </tr>
    <tr>
      <th>25%</th>
      <td>0.000000</td>
    </tr>
    <tr>
      <th>50%</th>
      <td>0.020000</td>
    </tr>
    <tr>
      <th>75%</th>
      <td>0.120000</td>
    </tr>
    <tr>
      <th>max</th>
      <td>4.000000</td>
    </tr>
  </tbody>
</table>
</div>



# Station Analysis


```python
# How many stations are available in this dataset?

total_stations = session.query(Stations).distinct().count()
print(f"Number of stations: {total_stations}")
```

    Number of stations: 9
    


```python
# What are the most active stations?
# List the stations and the counts in descending order.

def stations_frequency():
    active_stations = session.query(Stations.name,Stations.station,label('obersvations',func.count(Measurements.id))).\
                    filter(Measurements.station == Stations.station).\
    group_by(Stations.name,Stations.station).order_by(func.count(Measurements.id).desc())
    
    active_station_records = []
    for station in active_stations:
        active_station_records.append(station._asdict())

    active_station_df = pd.DataFrame.from_records(active_station_records)
    
    return active_station_df

stations_frequency()
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>name</th>
      <th>obersvations</th>
      <th>station</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>WAIHEE 837.5, HI US</td>
      <td>2772</td>
      <td>USC00519281</td>
    </tr>
    <tr>
      <th>1</th>
      <td>WAIKIKI 717.2, HI US</td>
      <td>2724</td>
      <td>USC00519397</td>
    </tr>
    <tr>
      <th>2</th>
      <td>KANEOHE 838.1, HI US</td>
      <td>2709</td>
      <td>USC00513117</td>
    </tr>
    <tr>
      <th>3</th>
      <td>WAIMANALO EXPERIMENTAL FARM, HI US</td>
      <td>2669</td>
      <td>USC00519523</td>
    </tr>
    <tr>
      <th>4</th>
      <td>MANOA LYON ARBO 785.2, HI US</td>
      <td>2612</td>
      <td>USC00516128</td>
    </tr>
    <tr>
      <th>5</th>
      <td>KUALOA RANCH HEADQUARTERS 886.9, HI US</td>
      <td>2202</td>
      <td>USC00514830</td>
    </tr>
    <tr>
      <th>6</th>
      <td>HONOLULU OBSERVATORY 702.2, HI US</td>
      <td>1979</td>
      <td>USC00511918</td>
    </tr>
    <tr>
      <th>7</th>
      <td>PEARL CITY, HI US</td>
      <td>1372</td>
      <td>USC00517948</td>
    </tr>
    <tr>
      <th>8</th>
      <td>UPPER WAHIAWA 874.3, HI US</td>
      <td>511</td>
      <td>USC00518838</td>
    </tr>
  </tbody>
</table>
</div>




```python
# Using the station id from the previous query, calculate the lowest temperature recorded, 
# highest temperature recorded, and average temperature most active station?

def calc_temps(start_date, end_date):
    
    return session.query(func.min(Measurements.tobs), func.avg(Measurements.tobs), func.max(Measurements.tobs)).\
        filter(Measurements.date >= start_date).filter(Measurements.date <= end_date).all()
print(calc_temps('2012-02-28', '2012-03-05'))

```

    [(62.0, 69.57142857142857, 74.0)]
    


```python
# Choose the station with the highest number of temperature observations.

def mostfreq():
    active_station_df = stations_frequency()
    
    freq_station = {'id':"",'name':""}
    freq_station['id'] = active_station_df.iloc[:1]['station'][0]

    freq_station['name'] = active_station_df.iloc[:1]['name'][0]
    
    
    
    return freq_station

mostfreq()
```




    {'id': 'USC00519281', 'name': 'WAIHEE 837.5, HI US'}




```python

# Query the last 12 months of temperature observation data for this station and plot the results as a histogram


def temperature_obs():
    current_time = datetime.now()

    past_year = current_time - timedelta(days=365)
    
    freq_station_id = mostfreq()['id']

    measure_freq_station = session.query(Measurements.date,Measurements.tobs).\
                        filter(Measurements.station == freq_station_id).\
                        filter(Measurements.date > past_year).all()

    station_measures = []
    for measure in measure_freq_station:
        station_measures.append(measure._asdict())

    station_measures_df = pd.DataFrame.from_records(station_measures)

    station_measures_df = station_measures_df.set_index('date')


    return station_measures_df
    

temperature_obs()
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>tobs</th>
    </tr>
    <tr>
      <th>date</th>
      <th></th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>2017-07-13</th>
      <td>74.0</td>
    </tr>
    <tr>
      <th>2017-07-14</th>
      <td>76.0</td>
    </tr>
    <tr>
      <th>2017-07-15</th>
      <td>80.0</td>
    </tr>
    <tr>
      <th>2017-07-16</th>
      <td>80.0</td>
    </tr>
    <tr>
      <th>2017-07-17</th>
      <td>76.0</td>
    </tr>
    <tr>
      <th>2017-07-18</th>
      <td>76.0</td>
    </tr>
    <tr>
      <th>2017-07-19</th>
      <td>76.0</td>
    </tr>
    <tr>
      <th>2017-07-20</th>
      <td>77.0</td>
    </tr>
    <tr>
      <th>2017-07-21</th>
      <td>77.0</td>
    </tr>
    <tr>
      <th>2017-07-22</th>
      <td>77.0</td>
    </tr>
    <tr>
      <th>2017-07-23</th>
      <td>82.0</td>
    </tr>
    <tr>
      <th>2017-07-24</th>
      <td>75.0</td>
    </tr>
    <tr>
      <th>2017-07-25</th>
      <td>77.0</td>
    </tr>
    <tr>
      <th>2017-07-26</th>
      <td>75.0</td>
    </tr>
    <tr>
      <th>2017-07-27</th>
      <td>76.0</td>
    </tr>
    <tr>
      <th>2017-07-28</th>
      <td>81.0</td>
    </tr>
    <tr>
      <th>2017-07-29</th>
      <td>82.0</td>
    </tr>
    <tr>
      <th>2017-07-30</th>
      <td>81.0</td>
    </tr>
    <tr>
      <th>2017-07-31</th>
      <td>76.0</td>
    </tr>
    <tr>
      <th>2017-08-04</th>
      <td>77.0</td>
    </tr>
    <tr>
      <th>2017-08-05</th>
      <td>82.0</td>
    </tr>
    <tr>
      <th>2017-08-06</th>
      <td>83.0</td>
    </tr>
    <tr>
      <th>2017-08-13</th>
      <td>77.0</td>
    </tr>
    <tr>
      <th>2017-08-14</th>
      <td>77.0</td>
    </tr>
    <tr>
      <th>2017-08-15</th>
      <td>77.0</td>
    </tr>
    <tr>
      <th>2017-08-16</th>
      <td>76.0</td>
    </tr>
    <tr>
      <th>2017-08-17</th>
      <td>76.0</td>
    </tr>
    <tr>
      <th>2017-08-18</th>
      <td>79.0</td>
    </tr>
  </tbody>
</table>
</div>




```python
# Choose the station with the highest number of temperature observations.
# Query the last 12 months of temperature observation data for this station and plot the results as a histogram



temp_df=pd.DataFrame(temperature_obs())
plt.figure(figsize=(20,10))
plt.hist(temp_df['tobs'],12)
plt.xlabel("Temperature")
plt.ylabel("Observations")
plt.title("Station Analysis")
plt.show()
```


![png](output_19_0.png)


# Trip analysis


```python
# Write a function called `calc_temps` that will accept start date and end date in the format '%Y-%m-%d' 
# and return the minimum, average, and maximum temperatures for that range of dates


def calc_temps(start_date, end_date):
    """TMIN, TAVG, and TMAX for a list of dates.
    
    Args:
        start_date (string): A date string in the format %Y-%m-%d
        end_date (string): A date string in the format %Y-%m-%d
        
    Returns:
        TMIN, TAVE, and TMAX
    """
    
    return session.query(func.min(Measurements.tobs), func.avg(Measurements.tobs), func.max(Measurements.tobs)).\
        filter(Measurements.date >= start_date).filter(Measurements.date <= end_date).all()
print(calc_temps('2012-02-28', '2012-03-05'))
```

    [(62.0, 69.57142857142857, 74.0)]
    


```python


def calc_temps(startdate,enddate):
    compstart = startdate - timedelta(days=365)
    compend = enddate - timedelta(days=365)
    
    temperature_vacation = session.query(label('max_temp',func.max(Measurements.tobs)),\
                                     label('min_temp',func.min(Measurements.tobs)),\
                                     label('avg_temp',func.avg(Measurements.tobs))).\
                    filter(Measurements.date >= compstart).\
                    filter(Measurements.date <= compend)

# Use your previous function `calc_temps` to calculate the tmin, tavg, and tmax 
# for your trip using the previous year's data for those same dates.    
    
    Max_temp = temperature_vacation[0].max_temp
    Min_temp = temperature_vacation[0].min_temp
    Avg_temp = temperature_vacation[0].avg_temp
    
#print(calc_temps(datetime(2017,1,1),datetime(2017,1,20)))

# Plot the results from your previous query as a bar chart. 
# Use "Trip Avg Temp" as your Title
# Use the average temperature for the y value
# Use the peak-to-peak (tmax-tmin) value as the y error bar (yerr)    
    
    yerror = Max_temp - Min_temp
    
    barvalue = [Avg_temp]
    x = range(len(barvalue))
    
    fig,ax = plt.subplots(figsize=(5,10))
    ax.bar(x, barvalue, yerr=yerror, color='g',alpha=0.6)
    ax.set_xticks([1]) 
    plt.xlabel("Vacation Length of Time")
    plt.ylabel("Temp (F)")
    plt.title("Trip Avg Temp")
    plt.tight_layout()

    
    plt.show()
```


```python
calc_temps(datetime(2017,1,1),datetime(2017,1,20))
```


![png](output_23_0.png)



```python
# Calculate the rainfall per weather station for your trip dates using the previous year's matching dates.
# Sort this in descending order by precipitation amount and list the station, name, latitude, longitude, and elevation


def calcrainfall(startdate,enddate):
    compstart = startdate - timedelta(days=365)
    compend = enddate - timedelta(days=365)
    
    rainfall_per_station = session.query(Stations.name,Stations.station,label('avg_rainfall',func.avg(Measurements.prcp)),Stations.latitude, Stations.longitude, Stations.elevation).\
                    filter(Measurements.station == Stations.station).\
                    filter(Measurements.date >= compstart).\
                    filter(Measurements.date <= compend).\
    group_by(Stations.name,Stations.station).order_by(func.avg(Measurements.prcp))
    
    
    rainfall_measures = []
    for measure in rainfall_per_station:
        rainfall_measures.append(measure._asdict())

    rain_measures_df = pd.DataFrame.from_records(rainfall_measures)

    rain_measures_df = rain_measures_df.set_index('station')


    return rain_measures_df
    
    #df = pd.DataFrame(query_to_dict(rainfall_per_station))
    #df = pd.DataFrame(rainfall_per_station)
       
    
        

```


```python
calcrainfall(datetime(2018,1,1),datetime(2018,1,20))
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>avg_rainfall</th>
      <th>elevation</th>
      <th>latitude</th>
      <th>longitude</th>
      <th>name</th>
    </tr>
    <tr>
      <th>station</th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>USC00517948</th>
      <td>0.000000</td>
      <td>11.9</td>
      <td>21.39340</td>
      <td>-157.97510</td>
      <td>PEARL CITY, HI US</td>
    </tr>
    <tr>
      <th>USC00519397</th>
      <td>0.000000</td>
      <td>3.0</td>
      <td>21.27160</td>
      <td>-157.81680</td>
      <td>WAIKIKI 717.2, HI US</td>
    </tr>
    <tr>
      <th>USC00513117</th>
      <td>0.003158</td>
      <td>14.6</td>
      <td>21.42340</td>
      <td>-157.80150</td>
      <td>KANEOHE 838.1, HI US</td>
    </tr>
    <tr>
      <th>USC00519281</th>
      <td>0.010526</td>
      <td>32.9</td>
      <td>21.45167</td>
      <td>-157.84889</td>
      <td>WAIHEE 837.5, HI US</td>
    </tr>
    <tr>
      <th>USC00516128</th>
      <td>0.035789</td>
      <td>152.4</td>
      <td>21.33310</td>
      <td>-157.80250</td>
      <td>MANOA LYON ARBO 785.2, HI US</td>
    </tr>
    <tr>
      <th>USC00514830</th>
      <td>0.042000</td>
      <td>7.0</td>
      <td>21.52130</td>
      <td>-157.83740</td>
      <td>KUALOA RANCH HEADQUARTERS 886.9, HI US</td>
    </tr>
    <tr>
      <th>USC00519523</th>
      <td>0.061000</td>
      <td>19.5</td>
      <td>21.33556</td>
      <td>-157.71139</td>
      <td>WAIMANALO EXPERIMENTAL FARM, HI US</td>
    </tr>
  </tbody>
</table>
</div>



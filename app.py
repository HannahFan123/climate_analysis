from flask import Flask,jsonify,send_file
from datetime import datetime
import json

app = Flask(__name__)

def currentday():
    today = datetime.now()
    return today.strftime('%m-%d')

@app.route("/")
def home():
    return (
        f"<bold>General data:<br/><br/></bold>"
        f"/api/v1.0/precipitation<br/>"
        f"/api/v1.0/stations<br/>"
        f"/api/v1.0/tobs<br/><br/>"
        f"<bold>Specific trip data:<br/><br/></bold>"
        f"/api/v1.0/trip/\"startdate as mm-dd\"<br/>"
        f"/api/v1.0/trip/\"startdate as mm-dd\"/\"enddate as mm-dd\"<br/><br/>" 
        )
    
@app.route("/api/v1.0/precipitation")
def precipitation_data():
    current_time = datetime.now()

    past_year = current_time - timedelta(days=365)

    measurements_year = session.query(Measurements.date,Measurements.prcp).filter(
        Measurements.date > past_year).\
    order_by(Measurements.date.desc()).all()

    measure_records = []
    for measure in measurements_year:
        measure_records.append(measure._asdict())

    measurements_df = pd.DataFrame.from_records(measure_records)

    measurements_df = measurements_df.set_index('date')

    precipitation_list = precipitation_df.to_dict(orient='index')
    result = jsonify(precipitation_list)
    return result

@app.route("/api/v1.0/stations")
def stationslist():
    active_station_df = stations_frequency()

    stations = active_station_df[['name','station']]

    stations_df = stations.to_dict(orient='records')

    result = jsonify(stations_df)
    return result

@app.route("/api/v1.0/tobs")
def temperature_obs():
    current_time = datetime.now()

    past_year = current_time - timedelta(days=365)
    

    stations_list = session.query(Measurements.date,Measurements.tobs).\
                        filter(Measurements.station == freq_station_id).\
                        filter(Measurements.date > past_year).all()

    station_measures = []
    for measure in stations_list:
        station_measures.append(measure._asdict())

    station_measures_df = pd.DataFrame.from_records(station_measures)

    station_measures_df = station_measures_df.set_index('date')

    station_measures_df = station_measures_df.to_json()
    result = jsonify(station_measures_df)
    return result

@app.route("/api/v1.0/trip/<start>")
@app.route("/api/v1.0/trip/<start>/<end>")


if __name__ == "__main__":
    app.run(debug=True)
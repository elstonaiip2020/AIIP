from flask import Flask,jsonify
import requests

app=Flask(__name__)
@app.route('/')
def home():
    return 'Hello Gbenga ! My first website'
    
@app.route('/maintenance_schedule')
def maintenance_schedule():
    return 'The about page'
    
@app.route('/get_ml_prediction')
def get_ml_prediction():
    latitude =  8.598084
    longitude = 53.556563

    url = ("http://www.7timer.info/bin/meteo.php?lon=" + str(longitude) + "&lat=" + str(latitude)+"&ac=0&unit=metric&output=json&tzshift=0")

    response2 = requests.get(url)

    data2 = response2.json()
    data_size = len(data2["dataseries"])
    dates=[]
    wind_speed=[]
    wind_direction=[]
    wind_value={"1":0.3,'2':21.85,'3':5.7,'4':9.4,'5':14,'6':20.85,'7':28.55,'8':34.65,'9':39.05,'10':43.8,'11':48.55,'12':53.4,'13':55.9}
    for j in range(4):
        dates.append(int(data2["init"][0:8])+j)
        
        
    for i in range(data_size):
        speed=data2["dataseries"][i][ "wind10m"]['speed']
        wind_speed.append(float(wind_value[str(speed)]))
        wind_direction.append(float(data2["dataseries"][i][ "wind10m"]['direction']))
    wind_data = {'dates':dates,
                 'wind_speed': [sum(wind_speed[0:4])/4,sum(wind_speed[4:8])/4,sum(wind_speed[8:12])/4,sum(wind_speed[12:16])/4],
                 'wind_direction':[sum(wind_direction[0:4])/4,sum(wind_direction[4:8])/4,sum(wind_direction[8:12])/4,sum(wind_direction[12:16])/4]}
    return jsonify(wind_data)
    

@app.route('/get_ml_prediction1')
def get_ml_prediction1():
    latitude =   -19.461907
    longitude =  142.110216

    url = ("http://www.7timer.info/bin/meteo.php?lon=" + str(longitude) + "&lat=" + str(latitude)+"&ac=0&unit=metric&output=json&tzshift=0")

    response2 = requests.get(url)

    data2 = response2.json()
    data_size = len(data2["dataseries"])
    dates=[]
    solar_temp=[]
    solar_temp_lo=[]
    solar_cover=[]
    solar_precip=[]
    
    for j in range(4):
        dates.append(int(data2["init"][0:8])+j)
        
    for i in range(data_size):
        solar_temp.append(float(data2["dataseries"][i][ "temp2m"]))
        solar_cover.append(float(data2["dataseries"][i][ "cloudcover"]))
        solar_precip.append(float(data2["dataseries"][i][ "prec_amount"]))
    solar_data = {'dates':dates,
                 'solar_temp': [sum(solar_temp[0:4])/4,sum(solar_temp[4:8])/4,sum(solar_temp[8:12])/4,sum(solar_temp[12:16])/4],
                 'solar_cover':[sum(solar_cover[0:4])/4,sum(solar_cover[4:8])/4,sum(solar_cover[8:12])/4,sum(solar_cover[12:16])/4],
                 'solar_precip':[sum(solar_precip[0:4])/4,sum(solar_precip[4:8])/4,sum(solar_precip[8:12])/4,sum(solar_precip[12:16])/4],
                 }
    return jsonify(solar_data)
  
    
if __name__=='__main__':
    app.run()
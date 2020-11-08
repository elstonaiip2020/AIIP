import requests
response= requests.get("https://freegeoip.app/json/")
data = response.json()
latitude = data["latitude"]
longitude = data["longitude"]
url = ("http://www.7timer.info/bin/meteo.php?lon=" + str(longitude) + "&lat=" + str(latitude)+"&ac=0&unit=metric&output=json&tzshift=0")
response2 = requests.get(url)
data2 = response2.json()
data_size = len(data2["dataseries"])
print(data2)
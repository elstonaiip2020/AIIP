import requests
receive = requests.get('https://imgs.xkcd.com/comics/alternative_energy_revolution.jpg')
with open(r'C:\Users\elston\git\AIIP\AppDev\Lectures\wind.jpg','wb') as f:
    f.write(receive.content)
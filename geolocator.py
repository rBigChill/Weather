import requests

WEBSITE = "https://api.techniknews.net/ipgeo/"

data = requests.get(WEBSITE)

json = data.json()

lat = json['lat']
lon = json['lon']

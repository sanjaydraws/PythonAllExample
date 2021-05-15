import requests

url = "https://shazam.p.rapidapi.com/songs/list-artist-top-tracks"

querystring = {"id":"40008598","locale":"en-US"}

headers = {
    'x-rapidapi-key': "449d7e5678msh9ecc62916b08451p1ce8e2jsnadf7109031fd",
    'x-rapidapi-host': "shazam.p.rapidapi.com"
    }

response = requests.request("GET", url, headers=headers, params=querystring)

print(response.text)


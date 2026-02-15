import requests

OWM_ENDPOINT="https://api.openweathermap.org/data/3.0/onecall"
api_key="37d4e19facca3e2f5a756c1831541898"
weather_params={
    "lat":51.507351,
    "lon":-0.127758,
    "appid":api_key,
}



respons=requests.get(OWM_ENDPOINT,params=weather_params)


print(respons.status_code)
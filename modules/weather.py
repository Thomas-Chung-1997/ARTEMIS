import requests
import json
import os

def GetWeatherData():
    baseUrl = "https://api.openweathermap.org/data/2.5/weather?"
    apiKey = os.environ["API_KEY_OPENWEATHERAPP"]
    cityID = "5946768" #Edmonton Alberta Canada
    
    url = baseUrl + "id=" + cityID + "&appid=" + apiKey
    
    return requests.get(url)

def WeatherSearch():
    response = GetWeatherData()
    
    if response.status_code == 200:
        data = response.json()
        
        return("The weather for today is " + data["weather"][0]["description"] +
              ". With a " + str(data["clouds"]["all"]) + " percent chance of rain and a current temperature of " +
              str(round(data["main"]["temp"] - 273)) + " degrees celcius, a high of " +
              str(round(data["main"]["temp_max"] - 273)) + " and a low of " +
              str(round(data["main"]["temp_min"] - 273)))
    else:
        return("sorry I was unable to retreive current weather report")
    
def TemperatureSearch():
    response = GetWeatherData()
    
    if response.status_code == 200:
        data = response.json()
        
        return("Today's temperature is " + str(round(data["main"]["temp"] - 273)) + 
               " degrees celcius, a high of " + str(round(data["main"]["temp_max"] - 273)) + 
               " and a low of " + str(round(data["main"]["temp_min"] - 273)))
    else:
        return("sorry I was unable to retreive current weather report")

def ForcastSearch():
    response = GetWeatherData()
    
    if response.status_code == 200:
        data = response.json()
        
        return("Today's forcast is " + data["weather"][0]["description"] +
              ". With a " + str(data["clouds"]["all"]) + " percent chance of rain.")
    else:
        return("sorry I was unable to retreive current weather report")
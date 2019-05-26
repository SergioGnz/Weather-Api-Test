from sys import argv
import requests
import json

#This function will get the response from the api in JSON, then convert it to string and print it
#In case the request fails, it'll show an error message
def PrintCityTemp():   
    city = ReadCityAsList()
    convertedCity = ConvertCity(city)
    request = requests.get('http://localhost:5000/weather_forecast/' + convertedCity)

    if(request.status_code == 200):
        temp = json.loads(request.text)
        print('Weather forecast for tomorrow in {city} Temperature: {temp}ºC'.format(city = PrettifyCityName(city), temp = temp))
    else:
        print('An error has occurred, please try again')

#Get the city as the argument in the command line (argv[0] returns the script name)
#We take into account multiple words city names
def ReadCityAsList():
    city = list()
    for arg in argv:
        if arg == argv[0]:
            continue
        city.append(arg)  
    return city

#This function converts the city name into a working string for the weather api
def ConvertCity(cityAsList):
    convertedCity = ''
    for word in cityAsList:
        convertedCity += '+' + word   
    return convertedCity    

#This function just returns the city name in a pretty form
def PrettifyCityName(city):
    cityName = ''
    for word in city:
        if word == city[len(city) - 1]:
            cityName += word
            continue
        cityName += word + ' '
    return cityName        

#Call the function to print the weather forecast
PrintCityTemp()
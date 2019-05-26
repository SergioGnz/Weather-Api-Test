from flask import Flask
from flask_restful import Resource, Api, reqparse
import json
import requests

#We create an instance of the class and feed it to the Api for initialization
app = Flask(__name__)
api = Api(app)

#Url components for ease of reading and modification
weather_api_key = '&APPID=61917a3c3246928f4f7b8828594cdd0b'
weather_api_url = 'http://api.openweathermap.org/data/2.5/forecast?q='
weather_units = '&units=metric'

#Here we can define our HTTP methods
#This class inherits from the base class Resource (Flask-RESTful), which can define the routing for our HTTP methods for a given url
class CityTemp(Resource):
    def get(self, city):
        return getCityTemp(city)

#This function will ensure to return the data requested from the weather api in JSON <-- for code clarity
def getCityTemp(city):
    data = getWeatherData(getCityUrl(city))
    return json.dumps(data['list'][1]['main']['temp'])

#This function returns de complete url of the weather api + the city <-- for code clarity
def getCityUrl(city):
    return weather_api_url + city + weather_units + weather_api_key

def getWeatherData(url):
    return requests.get(url).json()

#Here we add the above resource to the api so it registers the route with the framework
#This will automatically create an endpoint from the class name (can conflict if multiple resources are added)
api.add_resource(CityTemp, '/weather_forecast/<string:city>')

if __name__ == '__main__':
    app.run(debug=True)
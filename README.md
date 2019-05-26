# Weather-Api-Test
A little Python app for a weather forecast test</br>
This project requires:
- Python 3.7.3 ([Python Installation](https://www.python.org/downloads/))
- Flask 1.0.3 ([Flask Installation](http://flask.pocoo.org/docs/1.0/installation/#install-flask))
- Flask-RESTful 0.3.7 ([Flask-RESTful Installation](https://flask-restful.readthedocs.io/en/0.3.5/installation.html))

## How to run the project</br>
This project is composed of two python scripts, one acting as a web service and the other one used to access it.</br>
The web service (api.py) will be running on the local host, on port 5000/weather_forecast, and will accept a given city as a parameter for the requests.</br>
To run it just open a command prompt, navigate to the app directory and type "python api.py"</br>
</br>
![alt-text](https://github.com/SergioGnz/Weather-Api-Test/blob/master/Docu/Resources/Gif%20Api.gif)</br>
</br>
Once you got the api.py running, you can open another command prompt and run the weather.py script.</br>
Navigate to the app directory and run the weather.py script passing the city you want, for example : "python weather.py Palma"</br>
</br>
![alt-text](https://github.com/SergioGnz/Weather-Api-Test/blob/master/Docu/Resources/Gif%20App.gif)</br>
</br>
##Here you can find more examples of the app working with different cities</br>
![alt-text](https://github.com/SergioGnz/Weather-Api-Test/blob/master/Docu/Resources/1%20word.png)</br>
![alt-text](https://github.com/SergioGnz/Weather-Api-Test/blob/master/Docu/Resources/2%20word.png)</br>
![alt-text](https://github.com/SergioGnz/Weather-Api-Test/blob/master/Docu/Resources/3%20word.png)</br>
</br>
![alt-text](https://github.com/SergioGnz/Weather-Api-Test/blob/master/Docu/Resources/Error.png)</br>


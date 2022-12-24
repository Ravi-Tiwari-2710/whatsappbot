import requests, json

def weatherInfo(city):
    api_key = "0a66b3b4817a1f7f6e9b873f8f63eedb"
    city = city.split(' ')
    city = city[-1]
 
# base_url variable to store url
    base_url = "http://api.openweathermap.org/data/2.5/weather?"

    complete_url = base_url + "appid=" + api_key + "&q=" + city
    response = requests.get(complete_url)
    x = response.json()
    if x["cod"] != "404":

 
    # store the value of "main"
    # key in variable y
        y = x["main"]
 
    # store the value corresponding
    # to the "temp" key of y
        current_temperature = y["temp"]
 
    # store the value corresponding
    # to the "pressure" key of y
        current_pressure = y["pressure"]
 
    # store the value corresponding
    # to the "humidity" key of y
        current_humidity = y["humidity"]

        z = x["weather"]
 
    # store the value corresponding
    # to the "description" key at
    # the 0th index of z
        weather_description = z[0]["description"]

        resp = " Temperature (in kelvin unit) = " + str(current_temperature) + "\n atmospheric pressure (in hPa unit) = " +str(current_pressure) +"\n humidity (in percentage) = " +str(current_humidity) +"\n description = " + str(weather_description)
        return resp
    else:
        return 'city not found..'

 
 
 
import pyowm
 
owm = pyowm.OWM('f87466cc5ad3cb431b9e96c7759b45e3')

def get_Weather(city, country):
    observation = owm.weather_at_place (city + "," + country)
    w = observation.get_weather()
    return w

def get_Wind_And_Humidity(weather):
    wind_At = weather.get_wind()
    humidity_At = weather.get_humidity()
    return (wind_At, humidity_At)

def get_Loc_From_User():
    city = raw_input("Enter your city name:")
    country = raw_input("Enter your country name:")
    return (city, country)

city, country = get_Loc_From_User()
weather = get_Weather(city, country)
wind_At, humidity_At = get_Wind_And_Humidity (weather)
print ".................................."
print "Wind: " + str(wind_At) + "\n"
print "Humidity: " + str(humidity_At)
print ".................................."
wind_Speed = wind_At['speed']
wind_Deg = wind_At['deg']
print "Wind Speed: " + str(wind_Speed) + "\n"
print "Wind Degree: " + str(wind_Deg) + "degress"

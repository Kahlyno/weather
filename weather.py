import pyowm
 
owm = pyowm.OWM('f87466cc5ad3cb431b9e96c7759b45e3')
observation = owm.weather_at_place('USA')
w = observation.get_weather()
 
w.get_wind()
w.get_humidity()

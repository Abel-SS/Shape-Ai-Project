import requests,sys
#import os
from datetime import datetime

api_key = 'b8624cd03953122b5f8d15de684d4aa4'
location = input("Enter the city name: ")

complete_api_link = "https://api.openweathermap.org/data/2.5/weather?q="+location+"&appid="+api_key
api_link = requests.get(complete_api_link)
api_data = api_link.json()

#create variables to store and display data
temp_city = ((api_data['main']['temp']) - 273.15)
weather_desc = api_data['weather'][0]['description']
hmdt = api_data['main']['humidity']
wind_spd = api_data['wind']['speed']

print ("\nCurrent Weather Stats of {}\n".format(location.upper()))
print ("Current Temperature   : {:.2f} deg C".format(temp_city))
print ("Current Weather Type  :",format(weather_desc.upper()))
print ("Current Humidity      :",hmdt, '%')
print ("Current Wind Speed    :",wind_spd ,'kmph') 

orginal_stdout = sys.stdout
with open('weather.txt','w') as f:
	sys.stdout = f
	print ("\nCurrent Weather Stats of {}\n".format(location.upper()))
	print ("Current Temperature   : {:.2f} deg C".format(temp_city))
	print ("Current Weather Type  :",format(weather_desc.upper()))
	print ("Current Humidity      :",hmdt, '%')
	print ("Current Wind Speed    :",wind_spd ,'kmph') 

sys.stdout=orginal_stdout
print("The weather information has been written to the file name 'weather.txt'")
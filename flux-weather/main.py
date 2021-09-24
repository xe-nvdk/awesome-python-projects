from datetime import datetime
from time import sleep
from pyowm.owm import OWM
import influxdb_client
from influxdb_client import InfluxDBClient, Point
from influxdb_client.client.write_api import SYNCHRONOUS
from values import *

def temp():
    owm = OWM(api_key)
    get = owm.weather_manager()
        
    villa_rosa = get.weather_at_place('Villa Rosa,AR').weather
    temp_villa_rosa = villa_rosa.temperature(unit='celsius')['temp']
    hum_villa_rosa = villa_rosa.humidity
    condition_villa_rosa = villa_rosa.detailed_status
    wind_speed_villa_rosa = villa_rosa.wind()['speed']
    wind_orientation_villa_rosa = villa_rosa.wind()['deg']
    print("temp:", temp_villa_rosa, "hum:", hum_villa_rosa, "condition:", condition_villa_rosa, "wind speed:", wind_speed_villa_rosa, "wind orientation:", wind_orientation_villa_rosa)
		
    montevideo = get.weather_at_place('Montevideo,UY').weather
    temp_montevideo = montevideo.temperature(unit='celsius')['temp']
    hum_montevideo = montevideo.humidity
    condition_montevideo = montevideo.detailed_status
    wind_speed_montevideo = montevideo.wind()['speed']
    wind_orientation_montevideo = montevideo.wind()['deg']
    print("temp:", temp_montevideo, "hum:", hum_montevideo, "condition:", condition_montevideo, "wind speed:", wind_speed_montevideo, "wind orientation:", wind_orientation_montevideo)

    austin = get.weather_at_place('Austin,US').weather
    temp_austin = austin.temperature(unit='celsius')['temp']
    hum_austin = austin.humidity
    condition_austin = austin.detailed_status
    wind_speed_austin = austin.wind()['speed']
    wind_orientation_austin = austin.wind()['deg']
    print("temp:", temp_austin, "hum:", hum_austin, "condition:", condition_austin, "wind speed:", wind_speed_austin, "wind orientation:", wind_orientation_austin)
    
    seattle = get.weather_at_place('Seattle,US').weather
    temp_seattle = seattle.temperature(unit='celsius')['temp']
    hum_seattle = seattle.humidity
    condition_seattle = seattle.detailed_status
    wind_speed_seattle = seattle.wind()['speed']
    wind_orientation_seattle = seattle.wind()['deg']
    print("temp:", temp_seattle, "hum:", hum_seattle, "condition:", condition_seattle, "wind speed:", wind_speed_seattle, "wind orientation:", wind_orientation_seattle)

    sfo = get.weather_at_place('San Francisco,US').weather
    temp_sfo = sfo.temperature(unit='celsius')['temp']
    hum_sfo = sfo.humidity
    condition_sfo = sfo.detailed_status
    wind_speed_sfo = sfo.wind()['speed']
    wind_orientation_sfo = sfo.wind()['deg']
    print("temp:", temp_sfo, "hum:", hum_sfo, "condition:", condition_sfo, "wind speed:", wind_speed_sfo, "wind orientation:", wind_orientation_sfo)
                
    client = InfluxDBClient(url, token, org)
                
    write_api = client.write_api(write_options=SYNCHRONOUS)
            
    villa_rosa_p = influxdb_client.Point("weather_ttsg").tag("location", "Villa Rosa").field("wind_speed", wind_speed_villa_rosa).field("wind_orientation", wind_orientation_villa_rosa).field("condition", condition_villa_rosa).field("humidity", hum_villa_rosa).field("temperature", temp_villa_rosa).field("lat", -34.4345459).field("lon", -58.889472)
    montevideo_p = influxdb_client.Point("weather_ttsg").tag("location", "Montevideo").field("wind_speed", wind_speed_montevideo).field("wind_orientation", wind_orientation_montevideo).field("condition", condition_montevideo).field("humidity", hum_montevideo).field("temperature", temp_montevideo).field("lat", -34.90215003559578).field("lon", -56.17189882655434)
    austin_p = influxdb_client.Point("weather_ttsg").tag("location", "Austin").field("wind_speed", wind_speed_austin).field("wind_orientation", wind_orientation_austin).field("condition", condition_austin).field("humidity", hum_austin).field("temperature", temp_austin).field("lat", 30.2672).field("lon", -97.7431)
    sfo_p = influxdb_client.Point("weather_ttsg").tag("location", "San Francisco").field("wind_speed", wind_speed_sfo).field("wind_orientation", wind_orientation_sfo).field("condition", condition_sfo).field("humidity", hum_sfo).field("temperature", temp_sfo).field("lat", 37.7749).field("lon", -122.4194)
    seattle_p = influxdb_client.Point("weather_ttsg").tag("location", "Seattle").field("wind_speed", wind_speed_seattle).field("wind_orientation", wind_orientation_seattle).field("condition", condition_seattle).field("humidity", hum_seattle).field("temperature", temp_seattle).field("lat", 47.6062).field("lon", -122.3321)
        
    write_api.write(bucket, org, villa_rosa_p)
    write_api.write(bucket, org, montevideo_p)
    write_api.write(bucket, org, austin_p)
    write_api.write(bucket, org, seattle_p)
    write_api.write(bucket, org, sfo_p)
    
temp()
pass

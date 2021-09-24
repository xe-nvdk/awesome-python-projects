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
    print(temp_villa_rosa)
    print(hum_villa_rosa)
    print(condition_villa_rosa)
    print(wind_speed_villa_rosa)
    print(wind_orientation_villa_rosa)
		
    montevideo = get.weather_at_place('Montevideo,UY').weather
    temp_montevideo = montevideo.temperature(unit='celsius')['temp']
    hum_montevideo = montevideo.humidity
    condition_montevideo = montevideo.detailed_status
    wind_speed_montevideo = montevideo.wind()['speed']
    wind_orientation_montevideo = montevideo.wind()['deg']
    print(temp_montevideo)
    print(hum_montevideo)
    print(condition_montevideo)
    print(wind_speed_montevideo)
    print(wind_orientation_montevideo)

    austin = get.weather_at_place('Austin,US').weather
    temp_austin = austin.temperature(unit='celsius')['temp']
    hum_austin = austin.humidity
    condition_austin = austin.detailed_status
    wind_speed_austin = austin.wind()['speed']
    wind_orientation_austin = austin.wind()['deg']
    print(temp_austin)
    print(hum_austin)
    print(condition_austin)
    print(wind_speed_austin)
    print(wind_orientation_austin)

    seattle = get.weather_at_place('Seattle,US').weather
    temp_seattle = seattle.temperature(unit='celsius')['temp']
    hum_seattle = seattle.humidity
    condition_seattle = seattle.detailed_status
    wind_speed_seattle = seattle.wind()['speed']
    wind_orientation_seattle = seattle.wind()['deg']
    print(temp_seattle)
    print(hum_seattle)
    print(condition_seattle)
    print(wind_speed_seattle)
    print(wind_orientation_seattle)

    sfo = get.weather_at_place('San Francisco,US').weather
    temp_sfo = sfo.temperature(unit='celsius')['temp']
    hum_sfo = sfo.humidity
    condition_sfo = sfo.detailed_status
    wind_speed_sfo = sfo.wind()['speed']
    wind_orientation_sfo = sfo.wind()['deg']
    print(temp_sfo)
    print(hum_sfo)
    print(condition_sfo)
    print(wind_speed_sfo)
    print(wind_orientation_sfo)
                
    client = InfluxDBClient(url, token, org)
                
    write_api = client.write_api(write_options=SYNCHRONOUS)
            
    villa_rosa_p = influxdb_client.Point("weather_ttsg").tag("location", "Villa Rosa").field("temperature", temp_villa_rosa).field("lat", -34.4345459).field("lon", -58.889472)
    montevideo_p = influxdb_client.Point("weather_ttsg").tag("location", "Montevideo").field("temperature", temp_montevideo).field("lat", -34.90215003559578).field("lon", -56.17189882655434)
    austin_p = influxdb_client.Point("weather_ttsg").tag("location", "Austin").field("temperature", temp_austin).field("lat", 30.2672).field("lon", -97.7431)
    seattle_p = influxdb_client.Point("weather_ttsg").tag("location", "Seattle").field("temperature", temp_seattle).field("lat", 47.6062).field("lon", -122.3321)
    sfo_p = influxdb_client.Point("weather_ttsg").tag("location", "San Francisco").field("temperature", temp_sfo).field("lat", 37.7749).field("lon", -122.4194)
    villa_rosa_h = influxdb_client.Point("weather_ttsg").tag("location", "Villa Rosa").field("humidity", hum_villa_rosa).field("lat", -34.4345459).field("lon", -58.889472)
    montevideo_h = influxdb_client.Point("weather_ttsg").tag("location", "Montevideo").field("humidity", hum_montevideo).field("lat", -34.90215003559578).field("lon", -56.17189882655434)
    austin_h = influxdb_client.Point("weather_ttsg").tag("location", "Austin").field("humidity", hum_austin).field("lat", 30.2672).field("lon", -97.7431)
    seattle_h = influxdb_client.Point("weather_ttsg").tag("location", "Seattle").field("humidity", hum_seattle).field("lat", 47.6062).field("lon", -122.3321)
    sfo_h = influxdb_client.Point("weather_ttsg").tag("location", "San Francisco").field("humidity", hum_sfo).field("lat", 37.7749).field("lon", -122.4194)
    villa_rosa_c = influxdb_client.Point("weather_ttsg").tag("location", "Villa Rosa").field("condition", condition_villa_rosa).field("lat", -34.4345459).field("lon", -58.889472)
    montevideo_c = influxdb_client.Point("weather_ttsg").tag("location", "Montevideo").field("condition", condition_montevideo).field("lat", -34.90215003559578).field("lon", -56.17189882655434)
    austin_c = influxdb_client.Point("weather_ttsg").tag("location", "Austin").field("condition", condition_austin).field("lat", 30.2672).field("lon", -97.7431)
    seattle_c = influxdb_client.Point("weather_ttsg").tag("location", "Seattle").field("condition", condition_seattle).field("lat", 47.6062).field("lon", -122.3321)
    sfo_c = influxdb_client.Point("weather_ttsg").tag("location", "San Francisco").field("condition", condition_sfo).field("lat", 37.7749).field("lon", -122.4194)
    villa_rosa_ws = influxdb_client.Point("weather_ttsg").tag("location", "Villa Rosa").field("wind_speed", wind_speed_villa_rosa).field("lat", -34.4345459).field("lon", -58.889472)
    montevideo_ws = influxdb_client.Point("weather_ttsg").tag("location", "Montevideo").field("wind_speed", wind_speed_montevideo).field("lat", -34.90215003559578).field("lon", -56.17189882655434)
    austin_ws = influxdb_client.Point("weather_ttsg").tag("location", "Austin").field("wind_speed", wind_speed_austin).field("lat", 30.2672).field("lon", -97.7431)
    seattle_ws = influxdb_client.Point("weather_ttsg").tag("location", "Seattle").field("wind_speed", wind_speed_seattle).field("lat", 47.6062).field("lon", -122.3321)
    sfo_ws = influxdb_client.Point("weather_ttsg").tag("location", "San Francisco").field("wind_speed", wind_speed_sfo).field("lat", 37.7749).field("lon", -122.4194)
    villa_rosa_wo = influxdb_client.Point("weather_ttsg").tag("location", "Villa Rosa").field("wind_orientation", wind_orientation_villa_rosa).field("lat", -34.4345459).field("lon", -58.889472)
    montevideo_wo = influxdb_client.Point("weather_ttsg").tag("location", "Montevideo").field("wind_orientation", wind_orientation_montevideo).field("lat", -34.90215003559578).field("lon", -56.17189882655434)
    austin_wo = influxdb_client.Point("weather_ttsg").tag("location", "Austin").field("wind_orientation", wind_orientation_austin).field("lat", 30.2672).field("lon", -97.7431)
    seattle_wo = influxdb_client.Point("weather_ttsg").tag("location", "Seattle").field("wind_orientation", wind_orientation_seattle).field("lat", 47.6062).field("lon", -122.3321)
    sfo_wo = influxdb_client.Point("weather_ttsg").tag("location", "San Francisco").field("wind_orientation", wind_orientation_sfo).field("lat", 37.7749).field("lon", -122.4194)

    write_api.write(bucket, org, villa_rosa_p)
    write_api.write(bucket, org, montevideo_p)
    write_api.write(bucket, org, austin_p)
    write_api.write(bucket, org, seattle_p)
    write_api.write(bucket, org, sfo_p)
    write_api.write(bucket, org, villa_rosa_h)
    write_api.write(bucket, org, montevideo_h)
    write_api.write(bucket, org, austin_h)
    write_api.write(bucket, org, seattle_h)
    write_api.write(bucket, org, sfo_h)
    write_api.write(bucket, org, villa_rosa_c)
    write_api.write(bucket, org, montevideo_c)
    write_api.write(bucket, org, austin_c)
    write_api.write(bucket, org, seattle_c)
    write_api.write(bucket, org, sfo_c)
    write_api.write(bucket, org, villa_rosa_ws)
    write_api.write(bucket, org, montevideo_ws)
    write_api.write(bucket, org, austin_ws)
    write_api.write(bucket, org, seattle_ws)
    write_api.write(bucket, org, sfo_ws)
    write_api.write(bucket, org, villa_rosa_wo)
    write_api.write(bucket, org, montevideo_wo)
    write_api.write(bucket, org, austin_wo)
    write_api.write(bucket, org, seattle_wo)
    write_api.write(bucket, org, sfo_wo)

temp()
pass


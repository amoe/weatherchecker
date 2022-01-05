import pyowm
import pdb
import datetime

PEACE_ANGEL_COORDINATES = (50.82257, -0.15690)

def feels_like(weather):
    return weather.temperature('celsius')['feels_like']

def in_bounds(x, y, tolerance):
    return (x > (y - tolerance)) and (x < (y + tolerance))

def time_from_epoch_time(epoch_time):
    timestamp = datetime.datetime.utcfromtimestamp(epoch_time)
    return timestamp.time()
    

def test_foo():
    with open('.owm_key', 'r') as f:
        key = f.read().rstrip()
        print("read key as", key)

    owm = pyowm.OWM(key)

    
    mgr = owm.weather_manager()
    observation = mgr.weather_at_coords(*PEACE_ANGEL_COORDINATES)
    weather = observation.weather

    cloud_coverage = weather.clouds

    print("Overall status is:", weather.status)

    if cloud_coverage >= 50:
        print("It's murky and overcast.")
    elif cloud_coverage >= 20:
        print("There are scattered clouds.")
    else:
        print("There's not a cloud in the sky.")

    feels_like_c = feels_like(weather)
    wind_mph = weather.wind(unit='miles_hour')

    deg = wind_mph['deg']

    if in_bounds(deg, 270, 10) or in_bounds(deg, 90, 10):
        print("Heavily directional wind!  Watch out")
    
    print("wind is", wind_mph)

    if weather.rain:
        print("There's some rain.", weather.rain)
    else:
        print("There's no rain at all.")

    print("Visibility is:", weather.visibility())

    # If a gust hits "strong breeze", complain
    wind_speed = wind_mph['speed']

    if wind_speed >= 25:
        print("It's much too windy for a run.")
    elif wind_speed >= 13:
        print("You're gonna be against the wind, at least one way.")
    elif wind_speed >= 3:
        print("There's some wind, but not enough to care about.")
    else:
        print("There's basically no wind.")

    print(feels_like_c)
    if feels_like_c >= 15:
        print("You're probably going to be sweating in a T-shirt.")
    elif feels_like_c >= 8:
        print("You should be fine in a T-shirt.")
    else:
        print("It's cold, better wear a jumper.")


    # XXX: Not 100% sure this is robust against BST
    sunrise_time = time_from_epoch_time(weather.sunrise_time())
    sunset_time = time_from_epoch_time(weather.sunset_time())

    print("Determined sunrise time as", sunrise_time)
    print("Determined sunset time as", sunset_time)

    # 3h is the finest forecast granularity available.
    forecaster = mgr.forecast_at_coords(*PEACE_ANGEL_COORDINATES, interval='3h')

    
    for weather in forecaster.forecast:
        wind = weather.wind(unit='miles_hour')
        rain = weather.rain
        
        this_ts = datetime.datetime.utcfromtimestamp(weather.reference_time())
        this_time = this_ts.time()
#        print(weather.to_dict())
        if wind['speed'] < 25 and not rain and weather.clouds <= 50 and this_time > sunrise_time and this_time < sunset_time:
            print(weather.reference_time('iso'), weather.detailed_status, weather.clouds)
            
    # check:
    # 270 += 20deg = blowing east
    # 90 += 20deg = blowing west
            
    # clear_intervals = forecaster.when_clear()
    # next_interval = clear_intervals[0]
    
    # print("Maybe wait for:", next_interval.reference_time('iso'), next_interval.detailed_status)
    # print("The wind at this time is:", next_interval.wind(unit='miles_hour'))


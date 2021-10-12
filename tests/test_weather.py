import pyowm
import pdb

PEACE_ANGEL_COORDINATES = (50.82257, -0.15690)

def feels_like(weather):
    return weather.temperature('celsius')['feels_like']

def test_foo():
    with open('.owm_key', 'r') as f:
        key = f.read().rstrip()
        print("read key as", key)

    owm = pyowm.OWM(key)
    mgr = owm.weather_manager()
    observation = mgr.weather_at_coords(*PEACE_ANGEL_COORDINATES)
    weather = observation.weather

    cloud_coverage = weather.clouds

    if cloud_coverage >= 50:
        print("It's murky and overcast.")
    elif cloud_coverage >= 20:
        print("There are scattered clouds.")
    else:
        print("There's not a cloud in the sky.")

    feels_like_c = feels_like(weather)
    wind_mph = weather.wind(unit='miles_hour')

    if weather.rain:
        print("There's some rain.", weather.rain)
    else:
        print("There's no rain at all.")

    # If a gust hits "strong breeze", complain
    gust = wind_mph['gust']

    if gust >= 25:
        print("It's much too windy for a run.")
    elif gust >= 3:
        print("There's some wind, but not too much.")
    else:
        print("There's basically no wind.")
        
    if feels_like_c >= 15:
        print("You're probably going to be sweating in a T-shirt.")
    elif feels_like_c >= 8:
        print("You should be fine in a T-shirt.")
    else:
        print("It's cold, better wear a jumper.")

    assert 2 + 2 == 4

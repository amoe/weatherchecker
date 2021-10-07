import pyowm

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

    feels_like_c = feels_like(weather)
    wind_mph = weather.wind(unit='miles_hour')

    # If a gust hits "strong breeze", complain
    if wind_mph['gust'] >= 25:
        print("It's much too windy.")
    else:
        print("The wind looks OK.")

    if feels_like_c > 10:
        print("You should be fine in a T-shirt.")
    else:
        print("It's cold, better wear a jumper.")

    assert 2 + 2 == 4

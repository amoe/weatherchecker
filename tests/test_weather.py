import pyowm

PEACE_ANGEL_COORDINATES = (50.82257, -0.15690)

def test_foo():
    with open('.owm_key', 'r') as f:
        key = f.read().rstrip()
        print("read key as", key)

    owm = pyowm.OWM(key)
    mgr = owm.weather_manager()
    observation = mgr.weather_at_coords(*PEACE_ANGEL_COORDINATES)
    assert 2 + 2 == 4

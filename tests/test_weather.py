import pyowm


def test_foo():
    with open('.owm_key', 'r') as f:
        key = f.read().rstrip()
        print("read key as", key)

    owm = pyowm.OWM(key)
    mgr = owm.weather_manager()
    observation = mgr.weather_at_coords(50.82257, -0.15690)
    assert 2 + 2 == 4

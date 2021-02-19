from requests import get
from haversine import haversine

lat = 59.93906
lon = 30.31601
api_key = '85400b1ba3d254b6968b3601211515a5'

URL = f'http://api.openweathermap.org/data/2.5/weather?lat={lat}&lon={lon}&appid={api_key}'
response = get(URL)

temp_min = -100
temp_max = -5

def test_distanse():
  assert haversine((lat, lon), (59.93906, 30.31601)) < 10.0
    
def test_status_code():
  assert response.status_code == 200

def test_temp():
  temp = response.json()['main']['temp']

  if 'units=metric' in response.headers['X-Cache-Key']:
    temp = temp
  elif 'units=imperial' in response.headers['X-Cache-Key']:
    temp = (temp - 32) * (5 / 9)
  else:
    temp = temp - 273.15
  assert round(temp) > temp_min and round(temp) < temp_max





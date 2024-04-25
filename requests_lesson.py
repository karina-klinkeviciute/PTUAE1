import json
import os
from pprint import pprint
import dotenv
import webbrowser as wb

dotenv.load_dotenv()

import requests

# response = requests.get("https://www.google.com")

# print(dir(response))

# print(response.text)
#
# r = requests.get('https://www.python.org/static/img/python-logo.png')
#
# print(r.content)
#
# with open("logo.png", "wb") as file:
#     file.write(r.content)

# r = requests.get('http://python.org')
# print(r.status_code)
#
# r = requests.get('http://python.org/blabla')
# if r.status_code not in range(400, 600):
#     print('Pavyko prisijungti! Dirbame toliau...')
# else:
#     print(f'Kažkas ne taip.. Kodas {r.status_code}')

# r = requests.get('https://python.org/')
# print(r.headers)

# r = requests.get('https://www.python.org/search/?q=pep&page=2')
# print(r.text)

# payload = {'q': 'pep', 'page': '2'}
# r = requests.get('https://www.python.org/search/', params=payload)
# print(r.url)


# r = requests.get('http://httpbin.org/ip')
# print(r.text)

# data = {'name': 'Jonas', 'lastname': 'Jonaitis'}
# r = requests.post('http://httpbin.org/post', data=data)
# print(r.text)
#
# people = requests.get('http://api.open-notify.org/astros.json')
# print(people.text)
#
# people_data = people.json()
#
# print(type(people_data))
#
# for person in people_data["people"]:
#     print(person["name"])



# months = ['01', '02', '03', '04', '05', '06', '07', '08', '09', '10', '11', '12']
# for month in months:
#     r = requests.get(f'https://api.ratesapi.io/api/2019-{month}-15')
#     dictionary = json.loads(r.text)
#     print(f"2023-{month}-15     EUR-USD    {dictionary['rates']['USD']}")

# import webbrowser as wb
# import requests
# import json
#
PIXABAY_API_key = os.environ.get("PIXABAY_API_key")
WEATHER_API_KEY = os.environ.get("WEATHER_API_KEY")
IP_API_KEY = os.environ.get("IP_API_KEY")

# def open_first(query):
#    payload = {'key': API_key, 'q': query, 'img_type': 'photo', 'pretty': 'true'}
#    r = requests.get('https://pixabay.com/api/', params=payload)
#    json_str = r.text
#    result = json.loads(json_str)
#    pprint(result)
#    wb.open_new_tab(result['hits'][1]['largeImageURL'])
#
# open_first('rhino')

# response = requests.get("http://api.citybik.es/v2/networks/velib")
#
# pprint(response.text)

from requests import get

# ip = get('https://api.ipify.org').content.decode('utf8')
# print('My public IP address is: {}'.format(ip))

response_ip = requests.get(f"https://api.ipbase.com/v2/info?apikey={IP_API_KEY}&ip=84.15.180.58")

pprint(response_ip.json())

latitude = response_ip.json()["data"]["location"]["latitude"]
longitude = response_ip.json()["data"]["location"]["longitude"]

response = requests.get(f"https://api.openweathermap.org/data/2.5/weather?lat={latitude}&lon={longitude}&appid={WEATHER_API_KEY}")

print(response.text)

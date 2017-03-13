'''
A Python 3 script for requesitng json-weather-data from wwo website according to the yaml-file specification.
The script will then write the server response into a text-/json-file
'''

import yaml
import urllib.request
import os.path

# read the yaml-configuration file and look for the specifications
with open("configurations/project.yaml", "r") as f:
    allConfigData = yaml.load(f)

api_url = allConfigData['service']['api_url']
api_key = allConfigData['service']['api_key']
city = allConfigData['configuration']['denmark']['cities'][0]
start_date = allConfigData['configuration']['denmark']['start_date']
end_date = allConfigData['configuration']['denmark']['end_date']
option = allConfigData['configuration']['denmark']['option']

# build the final URL according to the wwo-API specification
url_request = api_url + "?key=" + "1fc7aec6253e4b558c083428171303" + "&q=" + city + "&format=json&date="+ start_date + "&enddate=" + end_date + "&tp=24"

# write the json- response to 'myWeatherData.json' if it is not in the current path
if os.path.exists('myWeatherData.json'):
    print(" --- myWeatherData.json exist in the current path! --- ")
else:
    with urllib.request.urlopen(url_request) as url:
        s = url.read()
    with open("myWeatherData.json", "wb") as json_file:
        json_file.write(s)



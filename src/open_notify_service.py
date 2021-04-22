from iss_information import *
import datetime
import requests

def get_raw_response(location):
  api_response = requests.get("http://api.open-notify.org/iss-pass.json?lat=%s&lon=%s&n=1" % (location[0],location[1])).json()

  return api_response if 'passes' in api_response['request'].keys() and 'latitude' in api_response['request'].keys() \
    and 'longitude' in api_response['request'].keys() else []

def parse_json(json_request):
  return json_request['response'][0]['risetime']

def get_flyover_time_for_a_location(location):
  return datetime.datetime.fromtimestamp(parse_json(get_raw_response(location))).strftime('%I:%M%p')


def get_number_of_astronauts_on_iss():
  return requests.get("http://api.open-notify.org/astros.json").json()['number']

def get_names_of_astronauts_on_iss():
  return [name['name'] for name in requests.get("http://api.open-notify.org/astros.json").json()['people']]

import requests
import time


def get_flyover_time_for_locations(locations, time_for_location_service):
  return { location: get_flyover_time_for_one_location(location, time_for_location_service) for location in locations }


def get_flyover_time_for_one_location(location, time_for_location_service):

  try:
    return time_for_location_service(location)
  except KeyError as ex:
    return (str(ex))

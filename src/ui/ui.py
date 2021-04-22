import argparse
import sys
sys.path.append("..")

from open_notify_service import *
from iss_information import *

parser = argparse.ArgumentParser(description='Find passtime for ISS given a location')
parser.add_argument("filename")
args = parser.parse_args()


with open(args.filename) as f:
    lines = [line.rstrip() for line in f]

locations = []

for location in lines[1:]:
    coordinate = location.split(",")
    locations.append((coordinate[0], coordinate[1]))

times = get_flyover_time_for_locations(locations, lambda location: get_flyover_time_for_a_location(location))

for key, value in times.items() :
    print(key[0], ",", key[1], ":" , value)

print("\nThere are", get_number_of_astronauts_on_iss(), "people on ISS at this time:\n")

for name in get_names_of_astronauts_on_iss():
    print(name)



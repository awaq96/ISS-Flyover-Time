import unittest
from iss_information import *


class iss_information_test(unittest.TestCase):
  def test_canary(self):
    self.assertTrue(True)

  def test_get_list_of_times_for_locations_empty(self):
    locations = {}

    self.assertEqual(get_flyover_time_for_locations(locations, lambda location: "11:58PM"), {})

  def test_get_list_of_times_for_locations_one(self):
    locations = [(30.2672, -97.743)]

    self.assertEqual({(30.2672, -97.743): '11:58PM'},
      get_flyover_time_for_locations(locations, lambda location: "11:58PM"))

  def test_get_list_of_times_for_locations_two(self):

    locations = [(30.2672, -97.7431),(29.7216, -95.3436)]

    fly_over_time_for_locations = {(30.2672, -97.7431): '11:58PM', (29.7216, -95.3436): "12:15AM"}

    self.assertEqual({(29.7216, -95.3436): '12:15AM', (30.2672, -97.7431): '11:58PM'},
      get_flyover_time_for_locations(locations, lambda location: fly_over_time_for_locations[location]))


  def test_get_list_of_times_for_locations_three(self):
    locations = [(30.2672, -97.7431), (29.7216, -95.3436), (35.2220, -101.831)]

    fly_over_time_for_locations = {(30.2672, -97.7431): '11:58PM', (29.7216, -95.3436): "12:15AM", (35.2220, -101.831): "1:00AM"}
    self.assertEqual({(29.7216, -95.3436): '12:15AM', (30.2672, -97.7431): '11:58PM', (35.2220, -101.831): '1:00AM'},
      get_flyover_time_for_locations(locations, lambda location: fly_over_time_for_locations[location])) 

  def test_get_list_of_times_invalid_location(self):
    locations = [(30.2672, -97.7431), (0, 0), (35.2220, -101.831)]

    fly_over_time_for_locations = {(30.2672, -97.7431): '11:58PM', (35.2220, -101.831): "1:00AM"}

    def raise_exception(self, exception):
      raise exception

    self.assertEqual({(30.2672, -97.7431): '11:58PM', (0, 0): "'Invalid Location'", (35.2220, -101.831): '1:00AM'},
      get_flyover_time_for_locations(locations ,lambda location:fly_over_time_for_locations[location] if location in 
      fly_over_time_for_locations.keys() else raise_exception(self, KeyError('Invalid Location'))))

  def test_get_list_of_times_network_error(self):
    locations = [(30.2672, -97.7431), (0, 0), (35.2220, -101.831)]

    fly_over_time_for_locations = {(30.2672, -97.7431): '11:58PM', (35.2220, -101.831): "1:00AM"}
     
    def raise_exception(self, exception):
      raise exception

    self.assertEqual({(30.2672, -97.7431): '11:58PM', (0, 0): "'Network Error'", (35.222, -101.831): '1:00AM'},
      get_flyover_time_for_locations(locations ,lambda location : fly_over_time_for_locations[location] if location in 
      fly_over_time_for_locations.keys() else raise_exception(self, KeyError('Network Error'))))
  

if __name__ == '__main__':
    unittest.main()

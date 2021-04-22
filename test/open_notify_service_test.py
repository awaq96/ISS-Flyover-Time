import unittest
from open_notify_service import *
from unittest.mock import patch, Mock
import open_notify_service


class open_notify_service_test(unittest.TestCase):

  def test_canary(self):
    self.assertTrue(True)

  def test_get_raw_response(self):
    location = (29.7216, -95.3436)

    api_response = get_raw_response( location)

    self.assertTrue(('passes' in api_response['request'].keys() and 'latitude' in api_response['request'].keys()
                     and 'longitude' in api_response['request'].keys()) or api_response == [])


  def test_parse_json_first(self):
    sample_data = {"message": "success",
                   "request": {
                       "altitude": 100,
                       "datetime": 1602736755,
                       "latitude": 29.72167,
                       "longitude": -95.343631,
                       "passes": 1
                   },
                   "response": [
                       {
                           "duration": 449,
                           "risetime": 1602764987
                       }
                   ]
                   }

    self.assertEqual(1602764987,
                     parse_json(sample_data))


  def test_parse_json_second(self):
    sample_data2 = {
        "message": "success",
        "request": {
            "altitude": 100,
            "datetime": 1602735194,
            "latitude": 30.2672,
            "longitude": -97.7431,
            "passes": 1
        },
        "response": [
            {
                "duration": 368,
                "risetime": 1602765016
            }
        ]
    }

    self.assertEqual(1602765016,
                     parse_json(sample_data2))


  def test_get_raw_response_mock(self):
    fake_json = {
      "message": "success", 
      "request": {
        "altitude": 100, 
        "datetime": 1602875779, 
        "latitude": 29.72167, 
        "longitude": -95.343631, 
        "passes": 1
      }, 
      "response": [
        {
          "duration": 432, 
          "risetime": 1602877884
        }
      ]
    } 

    mock_get_patcher = patch('open_notify_service.requests.get')
    mock_get = mock_get_patcher.start()
    mock_get.return_value.json.return_value = fake_json
    response = get_raw_response((29.7216, -95.3436))
    mock_get_patcher.stop()
    self.assertEqual(response, fake_json)


  def test_parse_json_mock(self):
    fake_json = 1602877884
    json_request = {
      "message": "success", 
      "request": {
        "altitude": 100, 
        "datetime": 1602875779, 
        "latitude": 29.72167, 
        "longitude": -95.343631, 
        "passes": 1
      }, 
      "response": [
        {
          "duration": 432, 
          "risetime": 1602877884
        }
      ]
    } 

    mock_get_patcher = patch('open_notify_service.requests.get')
    mock_get = mock_get_patcher.start()
    mock_get.return_value.json.return_value = fake_json
    response = parse_json(json_request)
    mock_get_patcher.stop()
    self.assertEqual(response, fake_json)

  def test_get_flyover_pass_to_get_raw(self):
    location = (29.7216, -95.3436)
    open_notify_service.get_raw_response = Mock(return_value={
      "message": "success", 
      "request": {
        "altitude": 100, 
        "datetime": 1602875779, 
        "latitude": 29.72167, 
        "longitude": -95.343631, 
        "passes": 1
      }, 
      "response": [
        {
          "duration": 432, 
          "risetime": 1602877884
        }
      ]
    } )
    open_notify_service.parse_json = Mock(return_value=1602877884)
    self.assertEqual('02:51PM',
      get_flyover_time_for_a_location(location))

  def test_get_number_of_astronauts_on_iss(self):
    self.assertEqual(6, get_number_of_astronauts_on_iss())

  def test_get_names_of_astronauts_on_iss(self):
      self.assertEqual(['Chris Cassidy', 'Anatoly Ivanishin', 'Ivan Vagner', 'Sergey Ryzhikov', 'Kate Rubins', 'Sergey Kud-Sverchkov'], get_names_of_astronauts_on_iss())

if __name__ == '__main__':
    unittest.main()

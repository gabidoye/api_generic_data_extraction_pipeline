import unittest
from unittest.mock import MagicMock, patch
import sys
 
# adding project Folder path to the system path
sys.path.append('/Users/gabidoye/Documents/data_Engineering/Generic_API_Pipeline/src')
from config import MyConfiguration



class TestMyConfiguration(unittest.TestCase):
     @patch('config.requests')
     def test_getapi_with_success(self, mock_requests):
          mock_response = MagicMock()
          mock_response.status_code = 200
          # specify the return value of the get() method
          mock_requests.get.return_value = mock_response

        # call the getapi() and test if the status message is 'success'
          wr = MyConfiguration('config.ini', 'cityofcalgary')
          self.assertEqual(wr.getapi(), "SUCCESS")
    

     @patch('config.requests')
     def test_getapi_with_fail(self, mock_requests):
          mock_response = MagicMock()
          mock_response.status_code = 400
          mock_requests.get.return_value = mock_response

          wr = MyConfiguration('config.ini', 'cityofcalgary')
          self.assertEqual(wr.getapi(), "FAILURE")


if __name__ == "__main__":
    unittest.main()


# class TestApiReaderMethods(unittest.TestCase):
#      def test_get_api_check_status_code_equals_200():
#           response = requests.get("https://data.calgary.ca/resource/848s-4m4z.json")
#           assert response.status_code == 200

import unittest
from unittest.mock import MagicMock, patch
import sys
 
# adding project Folder path to the system path
sys.path.append('/Users/gabidoye/Documents/data_Engineering/Generic_API_Pipeline/src')
from api import ApiReader



class TestApi(unittest.TestCase):
     @patch('config.requests')
     def test_getapi_with_success(self, mock_requests):
          mock_response = MagicMock()
          mock_response.status_code = 200
          # specify the return value of the get() method
          mock_requests.get.return_value = mock_response

        # call the getapi() and test if the status message is 'success'
          wr = ApiReader('config.ini', 'cityofcalgary')
          self.assertEqual(wr.validite_schema(), "SUCCESS")
    


if __name__ == "__main__":
    unittest.main()



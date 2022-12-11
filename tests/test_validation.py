  
from jsonschema import validate, ValidationError, SchemaError
import json
import sys
import requests 
import unittest
from unittest.mock import MagicMock, patch
from unittest import mock
import sys
 
# adding project Folder path to the system path
# sys.path.append('/Users/gabidoye/Documents/data_Engineering/Generic_API_Pipeline/src')
# from config import MyConfiguration



schema = json.load(open("/Users/gabidoye/Documents/data_Engineering/Generic_API_Pipeline/schema.json"))

# # adding project Folder path to the system path
sys.path.append('/Users/gabidoye/Documents/data_Engineering/Generic_API_Pipeline/src')
from api import ApiReader

class TestValidateSchema(unittest.TestCase):
    # test function Hi 
    @mock.patch("api.json.load")
    @mock.patch("api.open")
    def test_validate_schema(self,mock_open, mock_json_load):
        mock_response = MagicMock()
        # wr = ApiReader('config.ini', 'cityofcalgary')
                
        mock_json_load.return_value = dict({"the_data": "This is fake data"})
        assert ApiReader.validite_schema(mock_response) == False

            # mock_json_load.return_value = dict({"the_data": "This is real data"})
            # assert ApiReader.validite_schema("filepath") == True
       

    #     try:
    #         new=validate(response_list, schema)
    #  # error message in case if test case got failed
    #     except SchemaError as e:
    #         new = "There is an error with the schema"
     
    #     message = 'Invalid schema'
    #     # assertIsNone() to check that if input value is none
    #     self.assertIsNone(new, message)


  
if __name__ == '__main__':
    unittest.main()
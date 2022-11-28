  
from jsonschema import validate, ValidationError, SchemaError
import json
import requests 
import unittest

schema = json.load(open("/Users/gabidoye/Documents/data_Engineering/Generic_API_Pipeline/schema.json"))


class TestValidateSchema(unittest.TestCase):
    # test function 
    def test_schema_validity(self):
        response = requests.get("https://data.calgary.ca/resource/848s-4m4z.json")
        response_list = response.json() # This method is convenient when the API returns JSON
        
        try:
            new=validate(response_list, schema)
     # error message in case if test case got failed
        except SchemaError as e:
            new = "There is an error with the schema"
     
        message = 'Invalid schema'
        # assertIsNone() to check that if input value is none
        self.assertIsNone(new, message)


  
if __name__ == '__main__':
    unittest.main()
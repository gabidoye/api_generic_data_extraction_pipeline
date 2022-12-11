
import json
from jsonschema import validate, ValidationError, SchemaError
import os

schema = json.load(open("/Users/gabidoye/Documents/data_Engineering/Generic_API_Pipeline/schema.json"))
validfile = '/Users/gabidoye/Documents/data_Engineering/Generic_API_Pipeline/data/raw/data.json'


def validite_schema(validfile):
        """Validates if the json object is valid with the schema provided
        parameters
        ----------
        json file : json object
        schema : json object
        Returns
        -------
        valid json object
        
        """
        with open(validfile, 'r') as j:
            json_data = json.load(j)
            # print(json_data)
        
        try:
            validate(json_data, schema)
            # print("Valid schema and json object")
            return json_data

        except SchemaError as e:
            print("There is an error with the schema, check the log for more details")  
            with open('error.log','w') as f:
              f.write(str(e.context))

        except ValidationError as e:
            print("The json object cannot be validated against the schema, check the log for more details")
            with open('error.log','w') as f:
                f.write(str(e))
        # else:
        #     return json_data

# new = validite_schema(validfile='/Users/gabidoye/Documents/data_Engineering/Generic_API_Pipeline/data/raw/data.json')

# print(new)
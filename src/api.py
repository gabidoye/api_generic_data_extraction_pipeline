import requests
import json
import os
import pandas as pd
from configparser import ConfigParser
from flatten_json import flatten_json
from jsonschema import validate
from utils import validate_schema



class ApiReader(object):
    """
    Generic python class to read data from an API. It reads the specified url from the config
    file, parse the response and write the response to a file
    Parameters
    -----------
    config_file_names : .ini file
    endpoint : URL to read data from
    returns
    --------
    None
    """
    
    def __init__(self, config_file_names,endpoint): #constructor
        parser = ConfigParser()
        found = parser.read(config_file_names)
        if not found:
            raise ValueError('No config file found!')

        self.url = parser.get('url', endpoint)
        self.output_file_name = parser.get('output', 'filename')
        self.valid_file_path = parser.get('valid_json_path', 'folder')
        self.invalid_file_path = parser.get('invalid_json_path', 'folder')
       
        

    def read(self):
        validfile = os.path.join(self.valid_file_path,'data.json')
        # validfile = (self.valid_file_path,'data.json')
        print(validfile)
        invalidfile = os.path.join(self.invalid_file_path,'data.txt')


        try:
            response = requests.get(self.url)
            response_list = response.json()
            with open(validfile, 'w' ) as f:
                json.dump(response_list, f, indent=4)

        except requests.exceptions.Timeout:
            print('Request to url timed out')
        except requests.exceptions.TooManyRedirects:
            print(" Bad url please try a different one")
        except TypeError:
            print('Response could not be serialized')
            with open(invalidfile,'w') as f:
                f.write(response.text)
        except requests.exceptions.RequestException as e:
            raise SystemExit(e)
        
        else:
            return validfile
           
        

    def check_schema(self):
        validjsonfile = self.read()

        try:    
            goodjsonfile = validate_schema(validjsonfile)
            print("Valid schema and json object")
            return goodjsonfile
        except FileNotFoundError:
            print('Input File not available for the read instance method')
        

    def flaten(self):
        """This flattens the valid json object
        Parameters: valid json object
        Returns: flattened csv file
        """
       
        data = self.check_schema()
        # print(type(data))
        df = pd.json_normalize(data)
        df.to_csv(self.output_file_name, sep='\t')

        # if isinstance(data, dict):
        #     df = pd.DataFrame([flatten_json(data)])
        #     df.to_csv(self.output_file_name, sep='\t')

        # elif isinstance(data, list):
        #     df = pd.DataFrame.from_records(data)
        #     # df = pd.DataFrame([flatten_json(x) for x in data])
        #     df.to_csv(self.output_file_name, sep='\t')

        return 
        

if __name__ == "__main__":
    config=ApiReader('config.ini', 'cityofcalgary')
    (config.flaten())


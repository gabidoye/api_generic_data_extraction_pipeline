import requests
import json
import os
import pandas as pd
from configparser import ConfigParser
from flatten_json import flatten_json
from jsonschema import validate, ValidationError, SchemaError
from utils import validite_schema


absolute_path = os.path.dirname(__file__)
relative_path = "../"
full_path = os.path.join(absolute_path, relative_path)
schema = json.load(open("/Users/gabidoye/Documents/data_Engineering/Generic_API_Pipeline/schema.json"))





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
        found = parser.read(full_path + config_file_names)
        if not found:
            raise ValueError('No config file found!')

        self.url = parser.get('url', endpoint)
        self.output_file_name = parser.get('output', 'filename')
        self.valid_file_path = parser.get('valid_json_path', 'folder')
        self.invalid_file_path = parser.get('invalid_json_path', 'folder')
       
        

    def read(self):
        validfile = os.path.join(self.valid_file_path,'data.json')
        invalidfile = os.path.join(self.invalid_file_path,'data.txt')
        try:
            """Serialize the response and write to json formatedfile"""
            response = requests.get(self.url)
            response_list = response.json()
        
            with open(validfile, 'w' ) as f:
                json.dump(response_list, f, indent=4)
        
        except TypeError:
            print('Response could not be serialized')
            with open(invalidfile,'w') as f:
                f.write(response.text)
        else:
            return validfile
            print("ok")
        

    def check_schema(self):
        validjsonfile = self.read()

        try:    
            goodjsonfile = validite_schema(validjsonfile)
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
        print(data)
        if isinstance(data, dict):
            df = pd.DataFrame([flatten_json(data)])
            df.to_csv(self.output_file_name, sep='\t')

        elif isinstance(data, list):
            df = pd.DataFrame([flatten_json(x) for x in data])
            df.to_csv(self.output_file_name, sep='\t')

        return 
        


# config = MyConfiguration('config.ini', 'ilorin')
# print(config.url)

# class MyDatabase():
#     def __init__(self, db="mydb", user="postgres"):
#         self.conn = psycopg2.connect(database=db, user=user)
#         self.cur = self.conn.cursor()

#     def query(self, query):
#         self.cur.execute(query)

#     def close(self):
#         self.cur.close()
#         self.conn.close()

# db = MyDatabase()
# db.query("SELECT * FROM table;")
# db.close()

# import bitcoin_api
# result = bitcoin_api.BitcoinAPI('COINDESK').get()
# result = bitcoin_api.BitcoinAPI('BITSTAMP').get()

if __name__ == "__main__":
    config=ApiReader('config.ini', 'cityofcalgary')
    print(config.flaten())


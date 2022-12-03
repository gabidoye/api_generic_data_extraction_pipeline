import requests
import json
from json import JSONDecodeError
import pandas as pd
from configparser import ConfigParser
from flatten_json import flatten_json
from config import MyConfiguration
import os

absolute_path = os.path.dirname(__file__)
relative_path = "../"
full_path = os.path.join(absolute_path, relative_path)




class ApiReader(object):
    
    def __init__(self, file_names,endpoint): #constructor
        parser = ConfigParser()
        found = parser.read(full_path + file_names)
        self.url = parser.get('url', endpoint)
        self.output_file_name = parser.get('output', 'filename')
        self.valid_json_path = parser.get('valid_json_path', 'folder')
        validfile_path=os.path.join(self.valid_json_path,'data.json')
        self.invalid_json_path = parser.get('invalid_json_path', 'folder')
        invalidfile_path=os.path.join(self.invalid_json_path,'data.txt')
        if not found:
            raise ValueError('No config file found!')
        else:
            try:
                """Serialize the response and write to json formatedfile"""
                response = requests.get(self.url)
                response_list = response.json()
                with open(validfile_path, 'w') as f:
                    json.dump(response_list, f, indent=4)
            except TypeError:
                print('Response could not be serialized')
                with open(invalidfile_path,'w') as f:
                    f.write(response.text)

       

    def read(self) -> dict:

        response = requests.get(self.url)
        
        # print(response)
        response_list= response.json()
        new =json.dumps(response_list)
        print(new)
        return new

    def validate(self):
        data = self.read()
        try:
            return json.loads(data)
        except ValueError as e:
            print('invalid json: %s' % e)
        return None # or: raise

    def flaten(self):
       
        data = self.read()
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
    print(config)


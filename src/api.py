from asyncore import read
import requests
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
        if not found:
            raise ValueError('No config file found!')
        

    def read(self) -> dict:

        """Queries the weather API and returns the weather data for a particular city."""
        response = requests.get(self.url)
        response_list= response.json()
        print(response_list)
        return response_list

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
    print(config.flaten())


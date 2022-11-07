from asyncore import read
import requests
import pandas as pd
from configparser import ConfigParser


class ApiReader(object):
    
    def __init__(self, file_names,endpoint): #constructor
        parser = ConfigParser()
        found = parser.read(file_names)
        self.url = parser.get('url', endpoint)
        self.output_file_name = parser.get('output', 'filename')
        if not found:
            raise ValueError('No config file found!')
        

    def read(self) -> dict:

        """Queries the weather API and returns the weather data for a particular city."""
        response = requests.get(self.url)
        response_list= response.json()
        return response_list

    def flaten(self):
        data=[]
        data2 = self.read()
        for response in data2:  #list comprehenshion, map better optimized
            data.append({
            "sector": response.get('sector'),
            "community_name": response.get('community_name'),
            "group_category": response.get('group_category'),
            "category": response.get('category'),
            "count": response.get('count'),
            "resident_count": response.get('resident_count'),
            "date": response.get('date'),
            "year": response.get('year')

        })

        # print(data)
        df=pd.DataFrame(data)
        # df1=df.head(10)
        df.to_csv(self.output_file_name, sep='\t')

config = ApiReader('config.ini', 'cityofcalgary')
print(config.flaten())

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
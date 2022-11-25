from configparser import ConfigParser
import os
import requests

absolute_path = os.path.dirname(__file__)
relative_path = "../"
full_path = os.path.join(absolute_path, relative_path)


class MyConfiguration(object):

    def __init__(self, file_names,endpoint):
        self.file_names = file_names
        self.endpoint = endpoint

    def getapi(self):
        parser = ConfigParser()
        found = parser.read(full_path + self.file_names)
        self.url = parser.get('url', self.endpoint)
        response = requests.get(self.url)
        if response.status_code == 200: 
            return "SUCCESS"

        return "FAILURE"




if __name__ == "__main__":
    config = MyConfiguration('config.ini', 'cityofcalgary')
    print(config.getapi())



from configparser import ConfigParser
import os

absolute_path = os.path.dirname(__file__)
relative_path = "../"
full_path = os.path.join(absolute_path, relative_path)


class MyConfiguration(object):

    def __init__(self, file_names,endpoint):
        parser = ConfigParser()
        found = parser.read(full_path + file_names)
        self.url = parser.get('url', endpoint)
        self.output_file_name = parser.get('output', 'filename')
        if not found:
            raise ValueError('No config file found!')



if __name__ == "__main__":
    config = MyConfiguration('config.ini', 'ilorin')
    # print(config.url)



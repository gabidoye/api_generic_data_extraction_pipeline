from configparser import ConfigParser


class MyConfiguration(object):

    def __init__(self, file_names,endpoint):
        parser = ConfigParser()
        # parser.optionxform = str  # make option names case sensitive
        found = parser.read(file_names)
        self.url = parser.get('url', endpoint)
        self.output_file_name = parser.get('output', 'filename')
        if not found:
            raise ValueError('No config file found!')
        # for name in section_names:
        #     self.__dict__.update(parser.items(name))  # <-- here the magic happens

config = MyConfiguration('config.ini', 'cityofcalgary')
# import unittest

# class ObjectTypeTests(unittest.TestCase):
#     def test_is_instance(self):
#         self.assertIsInstance(1, int)
#         self.assertIsInstance(8.765, float)
#         self.assertIsInstance([], list)
#         self.assertIsInstance({ "a": 1 }, dict)

#         # self.assertIsInstance({ "a": 1 }, list)

#     def test_not_is_instance(self):
#         self.assertNotIsInstance(5, list)
    

#         # self.assertNotIsInstance(5, int)

# if __name__ == "__main__":
#     unittest.main()

# import requests module
import requests

# Making a get request
response = requests.get('https://api.github.com')

# print response
print(response)

# print json content
print(type(response.json()))

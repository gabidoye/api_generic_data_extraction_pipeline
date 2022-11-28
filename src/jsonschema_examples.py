# https://towardsdatascience.com/how-to-use-json-schema-to-validate-json-documents-ae9d8d1db344

from jsonschema import validate, ValidationError, SchemaError
 
import unittest

# schema = {
#     "type": "object",
#     "properties": {
#         "name": {"type": "string"},
#         "age": {"type": "number"},
#     },
#     "required": ["name"],
# }

# validate(instance={"name": "John", "age": 30}, schema=schema)
# # No error, the JSON is valid.

# # validate(instance={"name": "John", "age": "30"}, schema=schema)
# # # ValidationError: '30' is not of type 'number'

# validate(instance={"name": "John"}, schema=schema)
# # No error, the JSON is valid.

# # validate(instance={"age": 30}, schema=schema)
# # # ValidationError: 'name' is a required property

# validate(instance={"name": "John", "age": 30, "job": "Engineer"}, schema=schema)
# # No error, the JSON is valid. By additional fields are allowed.

schema = {
  "$schema": "http://json-schema.org/draft-04/schema#",
  "type": "array",
  "items": [
    {
      "type": "object",
      "properties": {
        "sector": {
          "type": "string"
        },
        "community_name": {
          "type": "string"
        },
        "group_category": {
          "type": "string"
        },
        "category": {
          "type": "string"
        },
        "count": {
          "type": "string"
        },
        "resident_count": {
          "type": "string"
        },
        "date": {
          "type": "string"
        },
        "year": {
          "type": "string"
        },
        "month": {
          "type": "string"
        },
        "id": {
          "type": "string"
        },
        "geocoded_column": {
          "type": "object",
          "properties": {
            "latitude": {
              "type": "string"
            },
            "longitude": {
              "type": "string"
            },
            "human_address": {
              "type": "string"
            }
          },
          "required": [
            "latitude",
            "longitude",
            "human_address"
          ]
        },
        ":@computed_region_4a3i_ccfj": {
          "type": "string"
        },
        ":@computed_region_p8tp_5dkv": {
          "type": "string"
        },
        ":@computed_region_4b54_tmc4": {
          "type": "string"
        },
        ":@computed_region_kxmf_bzkv": {
          "type": "string"
        }
      },
      "required": [
        "sector",
        "community_name",
        "group_category",
        "category",
        "count",
        "resident_count",
        "date",
        "year",
        "month",
        "id",
        "geocoded_column",
        ":@computed_region_4a3i_ccfj",
        ":@computed_region_p8tp_5dkv",
        ":@computed_region_4b54_tmc4",
        ":@computed_region_kxmf_bzkv"
      ]
    }
  ]
}

import requests
response = requests.get("https://data.calgary.ca/resource/848s-4m4z.json")
response_list = response.json() # This method is convenient when the API returns JSON
# print(respons_list)
try:
    new=validate(response_list, schema)
 
except SchemaError as e:
        print("There is an error with the schema")     
except ValidationError as e:
            print(e)
            print("---------")
            print(e.absolute_path) 
            print("---------")
            print(e.absolute_schema_path)
new=validate(response_list, schema=schema)






# ### Test the whole JSON is valid against the Schema
# def test_valid__JSON_against_schema(self):
#     global test_schema
#     global test_json
#     validate(test_json, test_schema)
# import json
# def validate(filename):
#     with open(filename) as file:
#         try:
#             return json.load(file) # put JSON-data to a variable
#         except json.decoder.JSONDecodeError:
#             print("Invalid JSON") # in case json is invalid
#         else:
#             print("Valid JSON") # in case json is valid



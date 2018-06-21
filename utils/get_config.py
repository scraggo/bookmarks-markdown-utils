import json

def get_json_config():
  with open("../config.json", "r") as read_file:
      return json.load(read_file)

import requests
import json
import os

token = os.environ.get("INPUT_API-TOKEN")
headers = {'Authorization': 'token ' + token}

url = requests.get('https://api.github.com/user', headers=headers)

json_formatted_str = json.dumps(url.json(), indent=2)

print(json_formatted_str)

print(f"::set-output name=user::{json_formatted_str}")
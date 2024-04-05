import json

try:
    with open('settings.json', 'r') as json_file:
        json_data = json.load(json_file)
        print('JSON is valid.')
except json.JSONDecodeError as e:
    print('Invalid JSON:', e)

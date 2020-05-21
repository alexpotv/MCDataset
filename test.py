import json

a = {'Name': 'Alex'}
b = {'Name': 'Arianne'}

with open('names.json') as json_file:
    data = json.load(json_file)

print(data['Name'])
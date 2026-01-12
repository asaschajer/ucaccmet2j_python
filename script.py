import json

with open('precipitation.json') as file:
    data = json.load(file)

print(type(data))
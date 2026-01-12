import json

with open('precipitation.json') as file:
    data = json.load(file)
    
    seattle_data = []
    
    for measurement in data:
        if measurement['station'] == 'GHCND:US1WAKG0038':
            seattle_data.append(measurement)
    print(seattle_data)
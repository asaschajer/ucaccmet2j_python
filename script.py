import json

with open('precipitation.json') as file:
    data = json.load(file)
    
    #Filtering to keep only the data from seattle
    seattle_data = []
    
    for measurement in data:
        if measurement['station'] == 'GHCND:US1WAKG0038':
            seattle_data.append(measurement)
    print(seattle_data)


    splitted_date = []
    for measurement in seattle_data:
        split_by_month = measurement['date'].split('-')[1]
        splitted_date.append(split_by_month)

        new_dic={
            'month': split_by_month,
            'value': measurement['value']
        }
        splitted_date.append(new_dic)

    print(splitted_date)

    # grouped_months = {}
    # for date in splitted_date:
    #     month = date['month']
    #     if month not in grouped_months:
    #         grouped_months[month] = []
    #     grouped_months[month].append(splitted_date)
    #     print(grouped_months)


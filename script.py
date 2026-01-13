import json

precipitation = {}

with open('precipitation.json') as file:
    data = json.load(file)
    
    #Filtering to keep only the data from seattle
    seattle_data = []
    
    for measurement in data:
        if measurement['station'] == 'GHCND:US1WAKG0038':
            seattle_data.append(measurement)
    # print(seattle_data)


    splitted_date = []
    for measurement in seattle_data:
        measurement['date'].split('-')[1]
        split_by_month = measurement['date'].split('-')[1]

        new_dic={
            'month': split_by_month,
            'value': measurement['value']
        }
        splitted_date.append(new_dic)

    # print(splitted_date)

    total_monthly_precipitation = {}
    for value in splitted_date:
        month = value['month']
        if month not in total_monthly_precipitation:
            total_monthly_precipitation[month] = 0
            total_monthly_precipitation[month] += value['value']
        else:
            total_monthly_precipitation[month] += value['value']
    print(total_monthly_precipitation)

    values_list = list(total_monthly_precipitation.values())
    total_yearly_precipitation = 0
    for monthly_precipitation in values_list:
        total_yearly_precipitation = total_yearly_precipitation + monthly_precipitation
    print(total_yearly_precipitation)

    relative_monthly_precipitation = {}
    for month in total_monthly_precipitation:
        result_relative_monthly_pre = total_monthly_precipitation[month]/total_yearly_precipitation
        relative_monthly_precipitation[month] = result_relative_monthly_pre
    print(relative_monthly_precipitation)


    import json   
    precipitation['Seattle'] = {
        'station': 'GHCND:US1WAKG0038',
        'state': 'WA',
        'total_monthly_precipitation': total_monthly_precipitation,
        'relative_monthly_precipitation': relative_monthly_precipitation
    }

#write the result output
with open('results.json', 'w', encoding='utf-8') as file:
    json.dump(precipitation, file, indent=4)

import json

precipitation = {}

# calculate the total precipitation for the 4 cities together
with open('precipitation.json') as file:
    data = json.load(file)
    overall_yearly_precipitation = 0
    for value in data:
        overall_yearly_precipitation = overall_yearly_precipitation + value['value']
    print(overall_yearly_precipitation) 


with open('stations.csv') as file:
    lines = file.readlines()
    print(lines)
    lines.pop(0)
    for line in lines:
        station_info = line.strip().split(',') #separating the list per station
        print(station_info)
        code = station_info[2]
        city = station_info[0]
        state = station_info[1]
        with open('precipitation.json') as file:
            data = json.load(file)
            
            #Filtering to keep only the data from the station studied
            station_data = []
            
            for measurement in data:
                if measurement['station'] == code:
                    station_data.append(measurement)
            # print(station_data)

            #splitting the date to get measurements based on the month
            splitted_date = []
            for measurement in station_data:
                measurement['date'].split('-')[1]
                split_by_month = measurement['date'].split('-')[1]

                new_dic={
                    'month': split_by_month,
                    'value': measurement['value']
                }
                splitted_date.append(new_dic)

            # print(splitted_date)
            
            # calculate the total monthly precipitation 
            total_monthly_precipitation = {}
            for value in splitted_date:
                month = value['month']
                if month not in total_monthly_precipitation:
                    total_monthly_precipitation[month] = 0
                    total_monthly_precipitation[month] += value['value']
                else:
                    total_monthly_precipitation[month] += value['value']
            print(total_monthly_precipitation)

            # calculate the total yearly precipitation
            values_list = list(total_monthly_precipitation.values())
            total_yearly_precipitation = 0
            for monthly_precipitation in values_list:
                total_yearly_precipitation = total_yearly_precipitation + monthly_precipitation
            print(total_yearly_precipitation)

            #calculate the relative monthly precipitation
            relative_monthly_precipitation = {}
            for month in total_monthly_precipitation:
                result_relative_monthly_pre = total_monthly_precipitation[month]/total_yearly_precipitation
                relative_monthly_precipitation[month] = result_relative_monthly_pre
            print(relative_monthly_precipitation)

            #calculate the relative yearly precipitation
            relative_yearly_precipitation = 0
            for month in total_monthly_precipitation:
                relative_yearly_precipitation = total_yearly_precipitation/overall_yearly_precipitation
            print(relative_yearly_precipitation)

            import json   
            precipitation[city] = {
                'station': code,
                'state': state,
                'total_monthly_precipitation': list(total_monthly_precipitation.values()),
                'total_yearly_precipitation': total_yearly_precipitation,
                'relative_monthly_precipitation': list(relative_monthly_precipitation.values()),
                'relative_yearly_precipitation': relative_yearly_precipitation
            }

#write the result output in JSON
with open('results.json', 'w', encoding='utf-8') as file:
    json.dump(precipitation, file, indent=4)

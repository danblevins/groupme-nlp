import time
from datetime import datetime as dt

def filter_columns(data):
    data = data[['created_at','favorited_by','nickname','name','sender_id','text','attachment']]

    return data

def filter_by_year(data, year: int):
    data['DateStr'] = data['send_time'].dt.strftime('%m/%d/%Y')
    filtered_year = "/" + str(year)
    data = data[data['DateStr'].str.contains(filtered_year)]

    return data

def filter_name_counts(data, count=60):
    data['name_counts'] = data['name'].value_counts()
    data['name_counts'] = data.groupby(['name']).transform('count')
    data = data[data['name_counts'] >= count]
    data = data[data['name'] != 'GroupMe']

    return data

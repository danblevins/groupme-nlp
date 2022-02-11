import json
import pandas as pd

def read_data(data_path: str):
    data = pd.read_json(data_path)

    return data

def clean_and_update_attachments(data) -> list:
    values = []
    for attachment in data["attachments"]:
        if len(attachment) > 0:
            value = 1
        else:
            value = 0
        values.append(value)

    return values

def include_nickname_column(data):
    return data['name']

def randomize_names(data) -> dict:
    names = []
    unique_sender_ids = data['sender_id'].unique()

    for sender_id in unique_sender_ids:
        temp_df = data[data['sender_id'] == sender_id]
        name = temp_df['name']
        if len(name) > 0:
            name = name.iloc[0]
        else:
            name = "Blank"
        names.append(name)
        
    dictionary = dict(zip(unique_sender_ids, names))
    dictionary['20319308'] = 'Matt'
    dictionary['13050665'] = 'Mark'
    dictionary['9271670'] = 'Luke'
    dictionary['11981553'] = 'John'
    dictionary['75249601'] = 'Steve'
    dictionary['12930615'] = 'Tom'
    dictionary['39072848'] = 'Sean'
    dictionary['13050668'] = 'James'
    dictionary['8494082'] = 'Ryan'
    dictionary['19824317'] = 'Aaron'
    dictionary['calendar'] = 'Calendar'
    dictionary['22277434'] = 'Rick'
    dictionary['19660209'] = 'Andrew'
    dictionary['17646615'] = 'Jason'
    dictionary['9653467'] = 'Tim'
    dictionary['41652535'] = 'Nick'
    dictionary['10250745'] = 'Dave'

    return dictionary

def rename_columns(data):
    data.columns = ['send_time','liked_by','nickname','name','sender_id','message','attachment']

    return data

def clean_and_update_liked_by(data) -> list:
    lengths = []
    for like in data["liked_by"]:
        lengths.append(len(like))

    return lengths

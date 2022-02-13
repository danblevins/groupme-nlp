import pandas as pd

def analyze_time_series_data(data, column_name):
    data = pd.DataFrame(data)
    data.columns = [column_name]
    data.reset_index(inplace=True)
    data['month'] = data['send_time'].dt.month

    return data

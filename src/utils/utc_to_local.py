from datetime import datetime as dt
import time

def utc_to_local(utc_datetime_column):
    now_timestamp = time.time()
    offset = dt.fromtimestamp(now_timestamp) - dt.utcfromtimestamp(now_timestamp)
    return utc_datetime_column + offset
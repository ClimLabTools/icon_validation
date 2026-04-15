import pandas as pd

def format_datetime64(val, format_str='%Y-%m-%d %H:%M:%S'):
    dt = pd.to_datetime(str(val))
    return dt.strftime(format_str)

def get_daterange_str(ds):
    t = pd.to_datetime(ds.time.values,utc=True)
    return f'{t[0].strftime("%Y%m%d")}-{t[-1].strftime("%Y%m%d")}'
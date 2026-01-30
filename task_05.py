import datetime

def date_in_future(integer):
    time = datetime.datetime.now()
    if isinstance(integer, int):
        time = time + datetime.timedelta(days=integer)
    return time.strftime('%Y-%m-%d %H:%M:%S')


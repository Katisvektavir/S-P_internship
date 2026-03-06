import datetime

def date_in_future(integer):
    time = datetime.datetime.now()
    if isinstance(integer, int):
        time = time + datetime.timedelta(days=integer)
    return time.strftime('%d-%m-%Y %H:%M:%S')

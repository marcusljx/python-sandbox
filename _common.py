import datetime

def timestamp():
    return datetime.datetime.strftime(datetime.datetime.now(), "%Y%m%d-%H%M%S.%f")
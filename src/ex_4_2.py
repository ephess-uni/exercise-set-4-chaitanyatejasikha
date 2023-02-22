""" ex_4_2.py """
from datetime import datetime


def logstamp_to_datetime(datestr):
    """
    logstamp_to_datetime return a datetime object from datetime string
    """
    return datetime.strptime(datestr,'%Y-%m-%dT%H:%M:%S')


# >>>> The code below will call your function and print the results
if __name__ == "__main__":
    test_date = '2022-12-01T01:02:03'
    print(f'{logstamp_to_datetime(test_date)=}')

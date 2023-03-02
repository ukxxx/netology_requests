import requests
from pprint import pprint
import datetime
import time
# import logging

# logging.basicConfig(level=logging.DEBUG)

LINK = 'https://api.stackexchange.com/2.3/questions?'
TAG = 'Python'
DAYS = 2

def get_dates(days):
    start_date = datetime.datetime.now() - datetime.timedelta(days=days)
    unix_start_date = int(time.mktime(start_date.timetuple()))
    end_date = datetime.datetime.now()
    unix_end_date = int(time.mktime(end_date.timetuple()))
    return {
            'fromdate': unix_start_date,
            'todate': unix_end_date
        }

def get_questions(link, tag, days):
    params = {'site' : 'stackoverflow', 'tagged': TAG, 'fromdate' : get_dates(DAYS)['fromdate'], 'todate' : get_dates(DAYS)['todate']}
    response = requests.get(url = link, params=params,)
    return response.json()['items']

if __name__ == '__main__':
    questions = get_questions(LINK, TAG, DAYS)
    print(f'\nQuestions for last {DAYS} day(s): \n')
    for question in questions:
        print(question['title'])
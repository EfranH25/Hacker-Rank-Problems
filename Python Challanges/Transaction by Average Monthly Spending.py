#!/bin/python3

import math
import os
import random
import re
import sys
import requests
import datetime
import calendar
import pytz
import time
#
# Complete the 'getUserTransaction' function below.
#
# The function is expected to return an INTEGER_ARRAY.
# The function accepts following parameters:
#  1. INTEGER uid
#  2. STRING txnType
#  3. STRING monthYear
#
#  https://jsonmock.hackerrank.com/api/transactions/search?txnType=
#

def getUserTransaction(uid, txnType, monthYear):

    month, year = monthYear.split('-')

    month_end_date = calendar.monthrange(int(year), int(month))[1]
    dt_start = datetime.datetime(int(year), int(month), 1)
    dt_end = datetime.datetime(int(year), int(month), month_end_date)

    url = 'https://jsonmock.hackerrank.com/api/transactions/search?userId=' + str(uid) + '&txnType=' + txnType
    r = requests.get(url)
    total_pages = r.json()['total_pages']

    average_list = []


    for i in range(1, total_pages + 1):
        new_url = url + '&page=' + str(i)
        r = requests.get(new_url)

        for i in range(len(r.json()['data'])):
            #print(r.json()['data'][i]['timestamp'])

            utc = r.json()['data'][i]['timestamp']/1000

            checker = time.strftime('%Y-%m-%d %H:%M:%S', time.gmtime(utc))

            time_stamp = datetime.datetime.fromtimestamp(utc)

            print((checker, r.json()['data'][i]['id'], r.json()['data'][i]['timestamp'], ()))

            if time_stamp >= dt_start and time_stamp <= dt_end:
                #print(r.json()['data'][i]['id'])
                average_list.append((float(r.json()['data'][i]['amount'][1:].replace(',', '')),r.json()['data'][i]['id']))

    if len(average_list) == 0:
        #print('caught')
        return [-1]

    print(average_list)
    sum = 0

    for i in average_list:
        sum += i[0]

    average = sum/ len(average_list)

    print(average)

    answer = []
    for i in average_list:
        if i[0] > average:
            answer.append(i[1])

    print(answer)
    final_answer = []

    for i in answer:
        if i not in final_answer:
            final_answer.append(i)

    #print(final_answer)

    return final_answer



if __name__ == '__main__':

    uid = 4

    txnType = 'debit'

    monthYear = '02-2019'

    result = getUserTransaction(uid, txnType, monthYear)

    print(result)

'''
4
debit
02-2019
'''

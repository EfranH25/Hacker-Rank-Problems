#!/bin/python3

import math
import os
import random
import re
import sys
import requests

def getUsernames(threshold):

    answer = []
    total_pages = test = requests.get('https://jsonmock.hackerrank.com/api/article_users?page=1').json()['total_pages']

    for i in range(1, total_pages + 1):
        url = 'https://jsonmock.hackerrank.com/api/article_users?page=' + str(i)
        r = requests.get(url)

        j = r.json()['data']

        for x in j:
            if x['submission_count'] > threshold:
                answer.append(x['username'])

    print(answer)
    return answer





if __name__ == '__main__':
    threshold = int(input().strip())

    result = getUsernames(threshold)


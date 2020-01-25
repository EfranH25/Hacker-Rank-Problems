import math
import os
import random
import re
import sys

def mathstuff(n):
    if n % 2 != 0:
        print('Weird')
    else:
        if n >=6 and n <= 20:
            print('Weird')
        elif n >= 2 and n <= 5 or n > 20:
            print('Not Weird')


if __name__ == '__main__':
    n = int(input().strip())
    mathstuff(n)

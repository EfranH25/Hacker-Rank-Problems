import numpy as np
import pandas as pd
import math

def calcMissing(readings):
    df = pd.DataFrame(readings, columns=['date', 'time', 'temp'])
    i = 0
    tracker = []
    df['temp'] = df['temp'].astype(float)

    while i < len(readings):
        if math.isnan(df['temp'].iloc[i]):
            tracker.append(i)
        i+=1


    df['temp'] = df['temp'].interpolate()
    df['temp'] = df['temp'].replace([np.nan], df['temp'].mean())

    for i in tracker:
        print(df.temp .iloc[i])




if __name__ == '__main__':
    readings_count = int(input().strip())

    readings = []

    for _ in range(readings_count):
        readings_item = input().split()

        if 'Missing' in readings_item[2]:
            readings_item[2] = np.nan

        readings.append(readings_item)


    calcMissing(readings)
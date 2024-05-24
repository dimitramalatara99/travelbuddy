import pandas as pd
import random

from pandas import read_csv

from Classes import *

class CSVManager:
    def __init__(self, **kwargs):
        for key, value in kwargs.items():
            setattr(self, key, value)

    def pd.read_csv('tb.csv')






df = pd.read_csv('tb.csv')
# print(df.head())

new_row = {
    'u_id': 3,
    'tv_name': 'Charlie'
}

new_row_df = pd.DataFrame([new_row])

df = pd.concat([df, new_row_df], ignore_index=True)

# print(df)

df.to_csv('tb_updated.csv', index=False)


def bookTrip():
    print('Welcome to Home Screen')


def getAccomodation(a, date_start, date_end, people):
    accoms = []
    for instance in Business.instances:
        if instance.b_destination == a:
            if random.choice([0, 1]):
                accoms.append(instance.b_name)
    print(accoms, 'done')


b1 = Business(1, 'lallala', 6987157140, 'ded', 'athens', 3)
b2 = Business(2, 'ououoou', 6987157140, 'tb', 'patra', 2)
b3 = Business(3, 'puf', 6987157140, 'travel', 'athens', 1)

getAccomodation('athens')

# def saveInfo(a, b, c, d):
#     max = df['tr_id'].max()
#     id = max + 1
#     traveler = a
#     status =




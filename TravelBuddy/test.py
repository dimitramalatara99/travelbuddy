import pandas as pd
import random

from pandas import read_csv

from Classes import *

with open('tb_updated.csv', newline='') as csvfile:
    reader = csv.DictReader(csvfile)
    for row in reader:
        if row['b_destination'] == 'athens':
            # print(row)
            Business(
                u_id=row['u_id'],
                u_email=row['u_email'],
                u_phone=row['u_phone'],
                b_name=row['b_name'],
                b_destination=row['b_destination'],
                b_bookings=row['b_bookings']
            )

for instance in Business.instances:
    print(instance)



# def bookTrip():
#     print('Welcome to Home Screen')
#
#
# def getAccomodation(a, date_start, date_end, people):
#     accoms = []
#     for instance in Business.instances:
#         if instance.b_destination == a:
#             if random.choice([0, 1]):
#                 accoms.append(instance.b_name)
#     print(accoms, 'done')
#
#
# b1 = Business(1, 'lallala', 6987157140, 'ded', 'athens', 3)
# b2 = Business(2, 'ououoou', 6987157140, 'tb', 'patra', 2)
# b3 = Business(3, 'puf', 6987157140, 'travel', 'athens', 1)
#
# getAccomodation('athens')

# def saveInfo(a, b, c, d):
#     max = df['tr_id'].max()
#     id = max + 1
#     traveler = a
#     status =




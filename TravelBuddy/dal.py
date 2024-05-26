from models import *
import csv
import pandas as pd


class CSVController:
    def __init__(self, csv_file_path):
        self.csv_file_path = csv_file_path
        self.df = pd.read_csv(self.csv_file_path)

    def get_business_by_dest(self, b_dest):
        businesses = []
        self.df = pd.read_csv(self.csv_file_path)
        for index, row in self.df.iterrows():
            if row['b_destination'] == str(b_dest):
                row['u_id'] = int(row['u_id'])
                row['b_bookings'] = int(row['b_bookings'])
                business = Business(
                    u_id=row['u_id'],
                    u_email=row['u_email'],
                    u_phone=row['u_phone'],
                    b_name=row['b_name'],
                    b_destination=row['b_destination'],
                    b_bookings=row['b_bookings']

                )

                businesses.append(business)
        return businesses

    def get_max_trip_id(self):
        max_id = self.df['tr_id'].max()
        return max_id.astype(int)

    def add_trip(self, trip):
        new_row = {
            'tr_id': trip.tr_id,
            'tr_traveler': trip.tr_traveler,
            'tr_status': trip.tr_status,
            'tr_people': trip.tr_people,
            'tr_date': trip.tr_date,
            'tr_destination': trip.tr_destination,
            'tr_accommodation': trip.tr_accommodation,
            'tr_options': trip.tr_options,
            'tr_phone': trip.tr_phone,
            'tr_advance_pay': trip.tr_advance_pay,
            'tr_payment_type': trip.tr_payment_type,
            'tr_payment_status': trip.tr_payment_status
        }
        new_df = pd.DataFrame([new_row])
        self.df = pd.concat([self.df, new_df], ignore_index=True)
        self.df.to_csv(self.csv_file_path, index=False)

    def get_basket(self, traveler):
        basket = []
        self.df = pd.read_csv(self.csv_file_path)
        for index, row in self.df.iterrows():
            if pd.notna(row['tr_traveler']):
                row['tr_traveler'] = int(row['tr_traveler'])
                if pd.notna(row['tr_id']):
                    row['tr_id'] = int(row['tr_id'])
                while True:
                    if pd.notna(row['tr_people']):
                        row['tr_people'] = int(row['tr_people'])
                        break
                    else:
                        row['tr_people'] = 1
                if pd.notna(row['tr_accommodation']):
                    row['tr_accommodation'] = int(row['tr_accommodation'])
                if row['tr_traveler'] == int(traveler) and row['tr_status'] == 'pending_pay':
                    trip = Trip(
                        tr_id=row['tr_id'],
                        tr_traveler=row['tr_traveler'],
                        tr_status=row['tr_status'],
                        tr_people=row['tr_people'],
                        tr_date=row['tr_date'],
                        tr_destination=row['tr_destination'],
                        tr_accommodation=row['tr_accommodation'],
                        tr_options=row['tr_options'],
                        tr_phone=row['tr_phone'],
                        tr_advance_pay=row['tr_advance_pay'],
                        tr_payment_type=row['tr_payment_type'],
                        tr_payment_status=row['tr_payment_status']
                    )
                    basket.append(trip)
        return basket

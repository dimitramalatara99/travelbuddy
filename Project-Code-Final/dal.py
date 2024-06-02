# Data Access Layer
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

    def get_max_tb_id(self):
        max_id = self.df['tb_id'].max()
        return max_id.astype(int)

    def get_dest_id(self, dest):
        dest_row = self.df[self.df['dst_name'] == dest]
        dest_id = dest_row['opt_id'].values[0]
        return dest_id

    def add_TB(self, tb):
        new_row = {
            'tb_id': tb.tb_id,
            'tb_status': tb.tb_status,
            'tb_traveler': tb.tb_traveler,
            'tb_dest': tb.tb_dest,
            'tb_min_age': tb.tb_min_age,
            'tb_max_age': tb.tb_max_age,
            'tb_vibe': tb.tb_vibe,
            'tb_request': tb.tb_request,
            'tb_buddies': tb.tb_buddies
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
                        row['tr_people'] = int(float(row['tr_people']))
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

    def load_all_dest(self):
        self.df = pd.read_csv(self.csv_file_path)
        destinations = []
        for index, row in self.df.iterrows():
            if pd.notna(row['dst_name']):
                if pd.notna(row['opt_id']):
                    row['opt_id'] = int(row['opt_id'])
                if pd.notna(row['opt_post_id']):
                    row['opt_post_id'] = int(row['opt_post_id'])
                if pd.notna(row['opt_average_age']):
                    row['opt_average_age'] = int(row['opt_average_age'])
                dest = Destination(
                    opt_id=row['opt_id'],
                    opt_post_id=row['opt_post_id'],
                    opt_vibe=row['opt_vibe'],
                    opt_best_season=row['opt_best_season'],
                    opt_average_age=row['opt_average_age'],
                    opt_average_budget=row['opt_average_budget'],
                    dst_name=row['dst_name']
                )
                destinations.append(dest)
        return destinations

    def get_TB(self, traveler, tb_dest, tb_vibe, tb_min_age, tb_max_age):
        buddies = []
        self.df = pd.read_csv(self.csv_file_path)

        dest = self.get_dest_id(tb_dest)

        filtered_df = self.df[(self.df['tb_dest'] == dest) & (self.df['tb_vibe'] == str(tb_vibe))]
        travelers_dict = {row['u_id']: row for index, row in self.df.iterrows()}

        for index, row in filtered_df.iterrows():
            tb_id = int(row['tb_id'])
            if tb_id in travelers_dict:
                row1 = travelers_dict[tb_id]
                u_id = int(row1['u_id']) if pd.notna(row1['u_id']) else None
                if (u_id != int(traveler)) & (int(tb_min_age) < int(row1['tv_age']) < int(tb_max_age)):
                    tv_age = int(row1['tv_age']) if pd.notna(row1['tv_age']) else None
                    tv_tb = int(row1['tv_tb']) if pd.notna(row1['tv_tb']) else None
                    buddy = Traveler(
                        u_id=u_id,
                        u_email=row1['u_email'],
                        u_phone=row1['u_phone'],
                        tv_name=row1['tv_name'],
                        tv_last_name=row1['tv_last_name'],
                        tv_age=tv_age,
                        tv_hobbies=row1['tv_hobbies'],
                        tv_wallet=row1['tv_wallet'],
                        tv_tb=tv_tb,
                        tv_friends=row1['tv_friends'],
                        tv_authentication=row1['tv_authentication']
                        )
                    buddies.append(buddy)
        return buddies


    def get_experiences_by_dest(self, dest_name, filters=None):
        experiences = []
        with open(self.csv_file_path, newline='') as csvfile:
            reader = csv.DictReader(csvfile)
            for row in reader:
                if row['exp_destination'] == dest_name:
                    experience = Experience(
                        opt_id=row['opt_id'],
                        opt_post_id=row['opt_post_id'],
                        opt_vibe=row['opt_vibe'],
                        opt_best_season=row['opt_best_season'],
                        opt_average_age=row['opt_average_age'],
                        opt_average_budget=row['opt_average_budget'],
                        exp_name=row['exp_name'],
                        exp_destination=row['exp_destination'],
                        exp_bookings=row['exp_bookings'],
                        exp_info=row['exp_info']
                    )
                    if self.apply_filters(experience, filters):
                        experiences.append(experience)

        return experiences

    def apply_filters(self, experience, filters):
        if filters:
            if filters.get('opt_vibe') and filters['opt_vibe'] != experience.opt_vibe:
                return False
            if filters.get('opt_best_season') and filters['opt_best_season'] != experience.opt_best_season:
                return False
            if filters.get('opt_average_age') and filters['opt_average_age'] != experience.opt_average_age:
                return False
            if filters.get('opt_average_budget') and filters['opt_average_budget'] != experience.opt_average_budget:
                return False
        return True
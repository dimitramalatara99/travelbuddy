from models import *
import csv
import pandas as pd


class CSVController:
    def __init__(self, csv_file_path):
        self.csv_file_path = csv_file_path
        self.df = pd.read_csv(self.csv_file_path)

    def get_all_destinations(self):
        destinations = set()
        with open(self.csv_file_path, newline='') as csvfile:
            reader = csv.DictReader(csvfile)
            for row in reader:
                destinations.add(row['dst_name'])

        return list(destinations)

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


    def get_max_trip_id(self):
        trips = self.df['tr_id']
        return trips.max() if not trips.empty else 0
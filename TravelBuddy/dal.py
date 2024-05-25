from models import Business
import csv


class CSVController:
    def __init__(self, csv_file_path):
        self.csv_file_path = csv_file_path

    def get_business_by_dest(self, b_dest):
        businesses = []
        with open(self.csv_file_path, newline='') as csvfile:
            reader = csv.DictReader(csvfile)
            for row in reader:
                if row['b_destination'] == str(b_dest):
                    business = Business(
                        u_id=row['u_id'],
                        u_email=row['u_email'],
                        u_phone=row['u_phone'],
                        b_name=row['b_name'],
                        b_destination=row['b_destination'],
                        b_bookings=row['b_bookings']

                    )
                    # print(business)
                    businesses.append(business)
        return businesses

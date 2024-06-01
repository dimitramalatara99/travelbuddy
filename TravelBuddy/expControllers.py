from expDal import CSVController
from models import *


class DestinationController:
    def __init__(self, dal):
        self.dal = dal

    def get_all_destinations(self):
        return self.dal.get_all_destinations()


class ExperienceController:
    def __init__(self, dal):
        self.dal = dal

    def get_experiences_by_dest(self, dest_name, filters=None):
        return self.dal.get_experiences_by_dest(dest_name, filters)


class TripController:
    def __init__(self, dal):
        self.dal = dal

    # def add_trip(self, traveler, people, date, destination, accommodation, options, phone):
    #     trip_id = self.dal.get_max_trip_id() + 1
    #     new_trip = Trip(
    #         tr_id=trip_id, tr_traveler=traveler, tr_status='pending_pay', tr_people=people, tr_date=date,
    #         tr_destination=destination, tr_accommodation=accommodation, tr_options=options, tr_phone=phone,
    #         tr_advance_pay='unknown', tr_payment_type='unknown', tr_payment_status='unknown'
    #     )
    #     self.dal.add_trip(new_trip)

    def add_trip(self, traveler, people, date, destination, options, phone):
        trip_id = self.dal.get_max_trip_id() + 1
        new_trip = Trip(
            tr_id=trip_id, tr_traveler=traveler, tr_status='pending_pay', tr_people=people, tr_date=date,
            tr_destination=destination, tr_accommodation='', tr_options=options, tr_phone=phone,
            tr_advance_pay='unknown', tr_payment_type='unknown', tr_payment_status='unknown'
        )
        self.dal.add_trip(new_trip)

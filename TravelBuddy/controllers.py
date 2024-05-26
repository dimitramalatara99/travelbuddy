from dal import CSVController
from models import Trip
from views import AccommodationScreen


class BusinessController:
    def __init__(self, dal):
        self.dal = dal

    def get_businesses_by_dest(self, b_dest):
        return self.dal.get_business_by_dest(b_dest)


class TripController:
    def __init__(self, dal):
        self.dal = dal

    def add_trip(self, traveler, people, date, destination, accommodation, options, phone):
        new_id = self.dal.get_max_trip_id() + 1
        new_trip = Trip(tr_id=new_id, tr_traveler=traveler, tr_status='pending_pay', tr_people=people, tr_date=date, tr_destination=destination, tr_accommodation=accommodation, tr_options=options, tr_phone=phone, tr_advance_pay='unknown', tr_payment_type='unknown', tr_payment_status='unknown')
        self.dal.add_trip(new_trip)

    def get_traveller_basket(self, traveler):
        return self.dal.get_basket(traveler)

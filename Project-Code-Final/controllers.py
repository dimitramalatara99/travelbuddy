from models import *


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


class DestinationController:
    def __init__(self, dal):
        self.dal = dal
        self.destinations = []

    def create_all_destinations(self):
        self.destinations = self.dal.load_all_dest()

    def check_destination(self, b_dest):
        name = b_dest.lower()
        return any(dest.dst_name == name for dest in self.destinations)

    def get_all_destinations(self):
        dests = []
        for dst in self.destinations:
            dest = dst.dst_name
            dests.append(dest)
        return dests

    # might delete
    # def get_all_destinations(self):
    #     return self.dal.get_all_destinations()


class TBController:
    def __init__(self, dal):
        self.dal = dal

    def findTravelers(self, traveler, tb_dest, tb_vibe, tb_min_age, tb_max_age):
        return self.dal.get_TB(traveler, tb_dest, tb_vibe, tb_min_age, tb_max_age)

    def check_tb_id(self, tbs, tb_id):
        return any(int(tb.u_id) == int(tb_id) for tb in tbs)

    def add_tb(self, tbs, tb_traveler, tb_dest, tb_min_age, tb_max_age, tb_vibe):
        dest = self.dal.get_dest_id(tb_dest)
        new_id = self.dal.get_max_tb_id() + 1
        for index, tb in enumerate(tbs, start=1):
            new_TB = TB(tb_id=new_id, tb_status='pending', tb_traveler=tb_traveler, tb_dest=dest,
                        tb_min_age=tb_min_age, tb_max_age=tb_max_age, tb_vibe=tb_vibe, tb_request=index, tb_buddies=tb)
            self.dal.add_TB(new_TB)


class ExperienceController:
    def __init__(self, dal):
        self.dal = dal

    def get_experiences_by_dest(self, dest_name, filters=None):
        return self.dal.get_experiences_by_dest(dest_name, filters)

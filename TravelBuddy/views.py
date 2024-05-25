from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.button import Button
# from kivy.uix.listview import ListView


class TripForm:
    def __init__(self, controller):
        self.controller = controller

    def getAccomodation(self, b_dest):
        businesses = self.controller.get_businesses_by_dest(b_dest)
        if businesses:
            for business in businesses:
                print(f"ID: {business.u_id}\nName: {business.b_name}\nBookings: {business.b_bookings}\n")
        else:
            print("No businesses found in that destination.")

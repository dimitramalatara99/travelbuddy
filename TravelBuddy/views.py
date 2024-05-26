from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.button import Button
# from kivy.uix.listview import ListView


class TripForm:
    def __init__(self, controller):
        self.controller = controller

    def getAccomodation(self, b_dest):
        return self.controller.get_businesses_by_dest(b_dest)


class AccommodationScreen:
    def __init__(self, controller):
        self.controller = controller

    def showMatchingAccomodations(self, businesses, b_dest, traveler, people, date, options, phone):
        if businesses:
            for business in businesses:
                print(f"ID: {business.u_id}\nName: {business.b_name}\nBookings: {business.b_bookings}\n")
        else:
            print(f"No businesses found in {b_dest}.")
            return

        accom = input("\nEnter your accommodation's name of choice: ")
        self.saveInfo(accom, businesses, b_dest, traveler, people, date, options, phone)

    def saveInfo(self, accom, businesses, b_dest, traveler, people, date, options, phone):
        accom_id = None
        for business in businesses:
            if business.b_name == accom:
                accom_id = business.u_id
                break

        if accom_id:
            self.controller.add_trip(traveler, people, date, b_dest, accom_id, options, phone)

            completion_screen = CompletionScreen()
            completion_screen.chooseComplete(self.controller, traveler)

        else:
            print("Selected accommodation not found.")
            return


class CompletionScreen:
    def chooseComplete(self, controller, traveler):
        while True:
            compl = input("\nIf you want to pay in advance write 'pay', else if you want to complete write 'okay': ")
            if compl == "okay":
                basket_screen = Basket(controller)
                basket_screen.goToBasket(traveler)
                break
            elif compl == 'pay':
                print('Continuing to advance payment...')
                break
            else:
                print("Invalid input. Please write 'pay' or 'okay'.")



class Basket:
    def __init__(self, controller):
        self.controller = controller

    def goToBasket(self, traveler):
        trips = self.controller.get_traveller_basket(traveler)
        if trips:
            print('Welcome to your Basket! Here are your trips.')
            for trip in trips:
                print(f"Trip ID: {trip.tr_id}\n")
        else:
            print('No Trips in Basket')

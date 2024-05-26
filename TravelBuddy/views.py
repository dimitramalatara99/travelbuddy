from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.button import Button
# from kivy.uix.listview import ListView


class TripForm:
    def __init__(self, trip_controller, destination_controller, business_controller):
        self.trip_controller = trip_controller
        self.destination_controller = destination_controller
        self.business_controller = business_controller

    def getTripForm(self):
        print("Fill Trip Form:")
        traveler = input("Enter Traveler ID: ")
        people = input("Enter Number of Travelers: ")
        while True:
            dest = input("Enter Destination: ")
            if self.destination_controller.check_destination(dest):
                break
            else:
                print('Destination not available. Please choose another Destination.')
                self.destination_controller.show_dests()
        date = input("Enter Date: ")
        options = input("Enter Options: ")
        phone = input("Enter Phone for Trip: ")

        print(f"\nAccommodations in '{dest}':")
        businesses = self.getAccomodation(dest)

        accommodation_screen = AccommodationScreen(self.trip_controller)
        accommodation_screen.showMatchingAccomodations(businesses, dest, traveler, people, date, options, phone)

    def getAccomodation(self, b_dest):
        return self.business_controller.get_businesses_by_dest(b_dest)


class AccommodationScreen:
    def __init__(self, controller):
        self.controller = controller

    def showMatchingAccomodations(self, businesses, b_dest, traveler, people, date, options, phone):
        print('Welcome to Accommodation Screen')
        if businesses:
            for business in businesses:
                print(f"ID: {business.u_id}\nName: {business.b_name}\nBookings: {business.b_bookings}\n")
        else:
            print(f"No businesses found in {b_dest}.")
            return
        while True:
            accom = input("\nEnter your accommodation's name of choice: ")
            found = False
            for business in businesses:
                if business.b_name == accom:
                    self.saveInfo(accom, businesses, b_dest, traveler, people, date, options, phone)
                    found = True
                    break
            if found:
                break
            else:
                print('Please choose one of the printed accommodations')

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
            compl = input("\nWelcome to Completion Screen\nIf you want to pay in advance write 'pay', else if you want to complete write 'okay': ")
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

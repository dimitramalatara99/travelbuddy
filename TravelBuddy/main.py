# main.py
from controllers import *
from dal import CSVController
from views import TripForm


def main():

    dal = CSVController('tb_updated.csv')
    business_controller = BusinessController(dal)
    trip_controller = TripController(dal)
    view = TripForm(business_controller)

    print("Fill Trip Form:")
    traveler = input("Enter Traveler ID: ")
    people = input("Enter Number of Travelers: ")
    dest = input("Enter Destination: ")
    date = input("Enter Date: ")
    options = input("Enter Options: ")
    phone = input("Enter Phone for Trip: ")

    print(f"\nAccommodations in '{dest}':")
    businesses = view.getAccomodation(dest)

    accommodation_screen = AccommodationScreen(trip_controller)
    accommodation_screen.showMatchingAccomodations(businesses, dest, traveler, people, date, options, phone)


if __name__ == "__main__":
    main()

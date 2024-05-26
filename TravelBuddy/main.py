# main.py
from controllers import *
from dal import CSVController
from views import TripForm


def main():

    dal = CSVController('tb_updated.csv')
    business_controller = BusinessController(dal)
    trip_controller = TripController(dal)
    destination_controller = DestinationController(dal)
    destination_controller.create_all_destinations()
    trip_form = TripForm(trip_controller, destination_controller, business_controller)
    trip_form.getTripForm()


if __name__ == "__main__":
    main()

# main.py
from controllers import *
from dal import CSVController
from views import HomeScreen


def main():
    dal = CSVController('tb_updated.csv')
    business_controller = BusinessController(dal)
    trip_controller = TripController(dal)
    destination_controller = DestinationController(dal)
    home_screen = HomeScreen(dal, business_controller, trip_controller, destination_controller)
    home_screen.homeInit()



if __name__ == "__main__":
    main()

# main.py
from controllers import BusinessController
from dal import CSVController
from views import TripForm


def main():
    dal = CSVController('tb_updated.csv')
    controller = BusinessController(dal)
    view = TripForm(controller)

    # Search for businesses by name
    dest = input("\nEnter a destination to search: ")
    print(f"\nBusinesses with name '{dest}':")
    view.getAccomodation(dest)


if __name__ == "__main__":
    main()

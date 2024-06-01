# main.py
from expControllers import DestinationController, ExperienceController, TripController
from expDal import CSVController
from expView import SuggestedExperiencesScreen


def main():
    dal = CSVController('tb.csv')
    destination_controller = DestinationController(dal)
    experience_controller = ExperienceController(dal)
    trip_controller = TripController(dal)
    view = SuggestedExperiencesScreen(destination_controller, experience_controller, trip_controller)

    # Display all available destinations
    print("\nFind Experiences for your dream Destination")
    view.display_destinations()

    # Choose destination in order to find (generic) experiences

    while True:
        dest = input("\nEnter a destination to see all available experiences: ").lower()
        if view.get_experiences(dest):
            filters = view.findCuratedExp()
            if filters is not None:
                view.get_experiences(dest, filters)
            else:
                # user choose no filters go back to all experiences
                view.get_experiences(dest)
            break
        else:
            print("! Invalid Destination or no experiences found with the specified filters.\nPlease try again !")


if __name__ == "__main__":
    main()

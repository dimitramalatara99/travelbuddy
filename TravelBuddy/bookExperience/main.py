# main.py
from expControllers import DestinationController
from expDal import CSVController
from expView import SuggestedExperiencesScreen


def main():
    dal = CSVController('tb.csv')
    destination_controller = DestinationController(dal)
    view = SuggestedExperiencesScreen(destination_controller)


    #Display all available destinations
    print("\nFind Experiences for your dream Destination")
    view.display_destinations()

    #Choose destination in order to find (generic) experiences

    while True:
        dest = input("\nEnter a destination to see all available experiences: ")
        if  view.get_experiences(dest):
                filters = view.findCuratedExp()
                if filters is not None:
                    view.get_experiences(dest, filters)
                else:
                    #user ch0zose no filters go back to all experiences
                    view.get_experiences(dest)
                break
        else:
            print("! Invalid Destination or no experiences found with the specified filters.\nPlease try again !")

if __name__ == "__main__":
    main()

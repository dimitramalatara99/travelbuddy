from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.button import Button
# from kivy.uix.listview import ListView


class HomeScreen:
    def __init__(self, dal, business_controller, trip_controller, destination_controller, tb_controller):
        self.dal = dal
        self.business_controller = business_controller
        self.trip_controller = trip_controller
        self.destination_controller = destination_controller
        self.tb_controller = tb_controller

    def homeInit(self):
        self.destination_controller.create_all_destinations()
        print('Welcome to Travel Buddy!')
        while True:
            action = input(
                "Actions:\nBook Trip\nBook Experience\nInvite\nAdd Business\nTravel Buddy\nChoose Action: ")
            action = action.lower()
            if action == 'book trip':
                self.bookTrip()
                break
            elif action == 'travel buddy':
                self.chooseTB()
                break
            else:
                print("Invalid input. Please choose a valid action.")

    def bookTrip(self):
        trip_form = TripForm(self.trip_controller, self.destination_controller, self.business_controller)
        trip_form.getTripForm()

    def chooseTB(self):
        tb_form = TravelBuddyForm(self.dal, self.business_controller, self.trip_controller, self.destination_controller, self.tb_controller)
        tb_form.getTBForm()


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

            completion_screen = CompletionScreen(self.controller)
            completion_screen.goToCompletion(traveler)

        else:
            print("Selected accommodation not found.")
            return


class CompletionScreen:
    def __init__(self, controller):
        self.controller = controller

    def goToCompletion(self, traveler):
        while True:
            compl = input("\nWelcome to Completion Screen\nIf you want to pay in advance write 'pay', else if you want to complete write 'okay': ")
            if compl == "okay":
                self.chooseComplete(traveler)
                break
            elif compl == 'pay':
                print('Continuing to advance payment...')
                break
            else:
                print("Invalid input. Please write 'pay' or 'okay'.")

    def chooseComplete(self, traveler):
        basket_screen = Basket(self.controller)
        basket_screen.goToBasket(traveler)


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


class TravelBuddyForm:
    def __init__(self, dal, business_controller, trip_controller, destination_controller, tb_controller):
        self.dal = dal
        self.business_controller = business_controller
        self.trip_controller = trip_controller
        self.destination_controller = destination_controller
        self.tb_controller = tb_controller

    def getTBForm(self):
        print("Fill Travel Buddy Form:")
        traveler = input("Enter Traveler ID: ")
        while True:
            destination = input("Enter Destination of Interest: ")
            if self.destination_controller.check_destination(destination):
                break
            else:
                print('Destination not available. Please choose another Destination.')
        min_age = input("Enter Minimum Age: ")
        max_age = input("Enter Maximum Age: ")
        while True:
            vibe = input("Enter Vacation Vide(chill/party/adventurous): ").lower()
            if vibe == "chill" or vibe == 'party' or vibe == 'adventurous':
                tbs = self.tb_controller.findTravelers(traveler, destination, vibe, min_age, max_age)
                posTb = PossibleTB(self.dal, self.business_controller, self.trip_controller, self.destination_controller, self.tb_controller)
                posTb.showTBs(tbs, traveler, destination, vibe, min_age, max_age)
                break
            else:
                print("Invalid input. Please write 'chill', 'party' or 'adventurous'.")


class PossibleTB:
    def __init__(self, dal, business_controller, trip_controller, destination_controller, tb_controller):
        self.dal = dal
        self.business_controller = business_controller
        self.trip_controller = trip_controller
        self.destination_controller = destination_controller
        self.tb_controller = tb_controller
        self.tbs = []

    def showTBs(self, tbs, traveler, destination, vibe, min_age, max_age):
        selected = []
        if tbs:
            print('Lets see your possible Travel Buddies!')
            for tb in tbs:
                print(f"Travel Buddy Number: {tb.u_id},\n \tName: {tb.tv_name},\n \tAge: {tb.tv_age}\n")
                print("\n")
            while True:
                select = input('Choose Travel Buddy with number, enter info to know more about a traveler: ')
                if select.lower() == 'done':
                    conf_screen = ConfirmationScreen(self.dal, self.business_controller, self.trip_controller, self.destination_controller, self.tb_controller)
                    conf_screen.showConfirmation(selected, traveler, destination, vibe, min_age, max_age)
                    break
                elif select.lower() == 'info':
                    found = True
                    while found:
                        tv_id = input('Which Travel Buddies are you looking for? : ')
                        if self.tb_controller.check_tb_id(tbs, tv_id):
                            for tb in tbs:
                                if int(tb.u_id) == int(tv_id):
                                    print(f"Hobbies: {tb.tv_hobbies}")
                                    found = False
                        else:
                            print("Please choose valid travel buddy.")
                elif select.isdigit():
                    if self.tb_controller.check_tb_id(tbs, select):
                        selected.append(select)
                        print("yoy can enter 'done' if you do not want to choose any more travel buddies")
                    else:
                        print("Please choose valid travel buddy.")
        else:
            print("No matches found.")


class ConfirmationScreen:
    def __init__(self, dal, business_controller, trip_controller, destination_controller, tb_controller):
        self.dal = dal
        self.business_controller = business_controller
        self.trip_controller = trip_controller
        self.destination_controller = destination_controller
        self.tb_controller = tb_controller

    def showConfirmation(self, selected, traveler, destination, vibe, min_age, max_age):
        print("Welcome to your Confirmation Screen!")
        while True:
            conf = input("Enter 'Confirm' to  complete or 'Cancel' to cancel.\n")
            if conf.lower() == 'confirm':
                self.tb_controller.add_tb(selected, traveler, destination, min_age, max_age, vibe)
                print('Completed')
                break
            elif conf.lower() == 'cancel':
                home_screen = HomeScreen(self.dal, self.business_controller, self.trip_controller, self.destination_controller, self.tb_controller)
                home_screen.homeInit()
                break
            else:
                print("Invalid input. Please write 'Confirm' or 'Cancel'.")

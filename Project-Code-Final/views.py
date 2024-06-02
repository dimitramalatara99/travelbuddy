# Boundary Objects
class HomeScreen:
    def __init__(self, dal, business_controller, trip_controller, destination_controller, tb_controller, experience_controller):
        self.dal = dal
        self.business_controller = business_controller
        self.trip_controller = trip_controller
        self.destination_controller = destination_controller
        self.tb_controller = tb_controller
        self.experience_controller = experience_controller

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
            elif action == 'book experience':
                self.bookExp()
                break
            elif action == 'invite':
                print("Use-case 'Invite' not done yet.")
                break
            elif action == 'add business':
                print("Use-case 'Add Business' not done yet.")
                break
            else:
                print("Invalid input. Please choose a valid action.")

    def bookTrip(self):
        trip_form = TripForm(self.trip_controller, self.destination_controller, self.business_controller)
        trip_form.getTripForm()

    def chooseTB(self):
        tb_form = TravelBuddyForm(self.dal, self.business_controller, self.trip_controller, self.destination_controller, self.tb_controller, self.experience_controller)
        tb_form.getTBForm()

    def bookExp(self):
        sug_exp = SuggestedExperiencesScreen(self.destination_controller, self.experience_controller, self.trip_controller)
        sug_exp.sug_exp_init()


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
    def __init__(self, dal, business_controller, trip_controller, destination_controller, tb_controller, experience_controller):
        self.dal = dal
        self.business_controller = business_controller
        self.trip_controller = trip_controller
        self.destination_controller = destination_controller
        self.tb_controller = tb_controller
        self.experience_controller = experience_controller

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
            vibe = input("Enter Vacation Vibe(chill/party/adventurous): ").lower()
            if vibe == "chill" or vibe == 'party' or vibe == 'adventurous':
                tbs = self.tb_controller.findTravelers(traveler, destination, vibe, min_age, max_age)
                posTb = PossibleTB(self.dal, self.business_controller, self.trip_controller, self.destination_controller, self.tb_controller, self.experience_controller)
                posTb.showTBs(tbs, traveler, destination, vibe, min_age, max_age)
                break
            else:
                print("Invalid input. Please write 'chill', 'party' or 'adventurous'.")


class PossibleTB:
    def __init__(self, dal, business_controller, trip_controller, destination_controller, tb_controller, experience_controller):
        self.dal = dal
        self.business_controller = business_controller
        self.trip_controller = trip_controller
        self.destination_controller = destination_controller
        self.tb_controller = tb_controller
        self.experience_controller = experience_controller
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
                    conf_screen = ConfirmationScreen(self.dal, self.business_controller, self.trip_controller, self.destination_controller, self.tb_controller, self.experience_controller)
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
    def __init__(self, dal, business_controller, trip_controller, destination_controller, tb_controller, experience_controller):
        self.dal = dal
        self.business_controller = business_controller
        self.trip_controller = trip_controller
        self.destination_controller = destination_controller
        self.tb_controller = tb_controller
        self.experience_controller = experience_controller

    def showConfirmation(self, selected, traveler, destination, vibe, min_age, max_age):
        print("Welcome to your Confirmation Screen!")
        while True:
            conf = input("Enter 'Confirm' to  complete or 'Cancel' to cancel.\n")
            if conf.lower() == 'confirm':
                self.confirmTB(selected, traveler, destination, min_age, max_age, vibe)
                break
            elif conf.lower() == 'cancel':
                self.rejectTB()
                break
            else:
                print("Invalid input. Please write 'Confirm' or 'Cancel'.")

    def confirmTB(self, selected, traveler, destination, min_age, max_age, vibe):
        self.tb_controller.add_tb(selected, traveler, destination, min_age, max_age, vibe)
        fres = FinalResultScreen()
        fres.goToFinalRS()

    def rejectTB(self):
        home_screen = HomeScreen(self.dal, self.business_controller, self.trip_controller, self.destination_controller,
                                 self.tb_controller, self.experience_controller)
        home_screen.homeInit()


class FinalResultScreen:
    def goToFinalRS(self):
        print('Welcome to Final Result Screen!')
        print('Completed')


class SuggestedExperiencesScreen:
    def __init__(self, destination_controller, experience_controller, trip_controller):
        self.destination_controller = destination_controller
        self.experience_controller = experience_controller
        self.booking_form = BookingForm(trip_controller)

    def sug_exp_init(self):
        # Display all available destinations
        print("\nFind Experiences for your dream Destination")
        self.display_destinations()

        # Choose destination in order to find (generic) experiences

        while True:
            dest = input("\nEnter a destination to see all available experiences: ").lower()
            if self.get_experiences(dest):
                filters = self.findCuratedExp()
                if filters is not None:
                    self.get_experiences(dest, filters)
                else:
                    # user choose no filters go back to all experiences
                    self.get_experiences(dest)
                break
            else:
                print("! Invalid Destination or no experiences found with the specified filters.\nPlease try again !")

    def display_destinations(self):
        destinations = self.destination_controller.get_all_destinations()
        if destinations:
            print("\n\nAll available destinations:")
            for destination in destinations:
                print(destination)
        else:
            print("No destinations available for choosing experience.")

    def get_experiences(self, dest_name, filters=None):
        experiences = self.experience_controller.get_experiences_by_dest(dest_name, filters)
        if experiences:
            if filters:
                print(f"Curated Experiences in '{dest_name}':")
                for idx, experience in enumerate(experiences, start=1):
                    print(
                        f"{idx}. Name: {experience.exp_name}\n   Vibe: {experience.opt_vibe}\n   Best Season: {experience.opt_best_season}\n   Average Age: {experience.opt_average_age}\n   Average Budget: {experience.opt_average_budget}\n   Bookings: {experience.exp_bookings}\n")

                # Prompt user to choose an experience
                while True:
                    try:
                        choice = int(input("Choose an experience by number, to learn more: ")) - 1
                        if 0 <= choice < len(experiences):
                            selected_experience = experiences[choice]
                            print(
                                f"\nSelected Experience Details:\nName: {selected_experience.exp_name}\nInfo: {selected_experience.exp_info}")
                            go_back = input(
                                "Do you want to go back to the list of experiences? (yes/no): ").strip().lower()
                            if go_back != 'yes':
                                self.booking_form.accept_booking(selected_experience)
                                return True
                        else:
                            print("Invalid choice. Please select a valid experience number.")
                    except ValueError:
                        print("Invalid input. Please enter a number.")
            else:
                print(f"\nExperiences in '{dest_name}':")
                for experience in experiences:
                    print(
                        f"Name: {experience.exp_name}\nVibe: {experience.opt_vibe}\nBest Season: {experience.opt_best_season}\nAverage Age: {experience.opt_average_age}\nAverage Budget: {experience.opt_average_budget}\nBookings: {experience.exp_bookings}\n")
        else:
            if filters:
                print(f"No experiences found in '{dest_name}' with the specified filters.")
            else:
                print(f"No experiences found in '{dest_name}'.")
            return False
        return True

    def findCuratedExp(self):
        apply_filters = input("Do you want to apply filters? (yes/no): ").strip().lower()
        if apply_filters == 'yes':
            filters = {}
            opt_vibe = input("Choose vibe (Adventure, Culture, Relaxation) - or press Enter to skip: ")
            if opt_vibe:
                filters['opt_vibe'] = opt_vibe
            opt_best_season = input("Choose preferred season (Winter, Spring, Summer) - or press Enter to skip: ").strip().lower()
            if opt_best_season:
                filters['opt_best_season'] = opt_best_season
            opt_average_age = input("Choose average age (20s, 30s, 40s, 60s) - or press Enter to skip: ").strip().lower()
            if opt_average_age:
                filters['opt_average_age'] = opt_average_age
            opt_average_budget = input("Choose preferred budget (500+, 1000+, 1500+, 2000+) - or press Enter to skip: ").strip().lower()
            if opt_average_budget:
                filters['opt_average_budget'] = opt_average_budget
            return filters
        return None


class BookingForm:
    def __init__(self, trip_controller):
        self.trip_controller = trip_controller

    def accept_booking(self, selected_experience):
        accept_booking = input("Do you accept booking? (yes/no): ").strip().lower()
        if accept_booking == 'yes':
            self.go_to_booking_form(selected_experience)

    def go_to_booking_form(self, selected_experience):
        print("Please fill the booking form below:")
        traveler = input("Enter traveler id: ")
        people = input("Enter number of people: ")
        date = input("Enter trip date (YYYY-MM-DD): ")
        phone = input("Enter contact phone number: ")

        self.save_info(traveler, people, date, selected_experience.exp_destination, selected_experience.exp_name, phone)

    def save_info(self, traveler, people, date, destination, options, phone):
        self.trip_controller.add_trip(
            traveler, people, date, destination, '', options, phone
        )
        print("Trip information saved successfully.")
        basket_screen = Basket(self.trip_controller)
        basket_screen.goToBasket(traveler)



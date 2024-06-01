class SuggestedExperiencesScreen:
    def __init__(self, destination_controller, experience_controller, trip_controller):
        self.destination_controller = destination_controller
        self.experience_controller = experience_controller
        self.booking_form = BookingForm(trip_controller)

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
        traveler = input("Enter traveler name: ")
        people = input("Enter number of people: ")
        date = input("Enter trip date (YYYY-MM-DD): ")
        phone = input("Enter contact phone number: ")

        self.save_info(traveler, people, date, selected_experience.exp_destination, selected_experience.exp_name, phone)

    def save_info(self, traveler, people, date, destination, options, phone):
        self.trip_controller.add_trip(
            traveler, people, date, destination, options, phone
        )
        print("Trip information saved successfully.")


class SuggestedExperiencesScreen:
    def __init__(self,destination_controller):
        self.destination_controller = destination_controller



    def display_destinations(self):
        destinations = self.destination_controller.get_all_destinations()
        if destinations:
            print("\n\nAll available destinations:")
            for destination in destinations:
                print(destination)
        else:
            print("No destinations available for choosing experience.")


    def get_experiences(self, dest_name, filters=None):
        experiences = self.destination_controller.get_experiences_by_dest(dest_name, filters)
        if experiences:
            if filters:
                print(f"Curated Experiences in '{dest_name}':")
            else:
                print(f"\nExperiences in '{dest_name}':")
            for experience in experiences:
                print(f"Name: {experience.exp_name}\nVibe: {experience.opt_vibe}\nBest Season: {experience.opt_best_season}\nAverage Age: {experience.opt_average_age}\nAverage Budget: {experience.opt_average_budget}\n")
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
            opt_best_season = input("Choose preferred season (Winter, Spring, Summer) - or press Enter to skip: ")
            if opt_best_season:
                filters['opt_best_season'] = opt_best_season
            opt_average_age = input("Choose average age (20s, 30s, 40s, 60s) - or press Enter to skip: ")
            if opt_average_age:
                filters['opt_average_age'] = opt_average_age
            opt_average_budget = input("Choose preferred budget (500+, 1000+, 1500+, 2000+) - or press Enter to skip: ")
            if opt_average_budget:
                filters['opt_average_budget'] = opt_average_budget
            return filters
        return None
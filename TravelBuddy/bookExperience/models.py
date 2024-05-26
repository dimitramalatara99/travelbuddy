class User:
    def __init__(self, u_id, u_email, u_phone):
        self.u_id = u_id
        self.u_email = u_email
        self.u_phone = u_phone


class Business(User):
    instances = []

    def __init__(self, u_id, u_email, u_phone, b_name, b_destination, b_bookings):
        super().__init__(u_id, u_email, u_phone)
        self.b_name = b_name
        self.b_destination = b_destination
        self.b_bookings = b_bookings
        Business.instances.append(self)

    def __repr__(self):
        # Provide a string representation of the object for debugging
        return f"Business(b_name={self.b_name}, b_destination={self.b_destination}, b_bookings={self.b_bookings})"


class Options:
    def __init__(self, opt_id, opt_post_id, opt_vibe, opt_best_season, opt_average_age, opt_average_budget):
        self.opt_id = opt_id
        self.opt_post_id = opt_post_id
        self.opt_vibe = opt_vibe
        self.opt_best_season = opt_best_season
        self.opt_average_age = opt_average_age
        self.opt_average_budget = opt_average_budget


class Destination(Options):
    def __init__(self, opt_id, opt_post_id, opt_vibe, opt_best_season, opt_average_age, opt_average_budget, dst_name):
        super().__init__(opt_id, opt_post_id, opt_vibe, opt_best_season, opt_average_age, opt_average_budget)
        self.dst_name = dst_name

    def __repr__(self):
        return f"Destination(dst_name={self.dst_name})"

class Experience(Options):

    def __init__(self, opt_id, opt_post_id, opt_vibe, opt_best_season, opt_average_age, opt_average_budget, exp_name, exp_destination, exp_bookings, exp_info):
        super().__init__(opt_id, opt_post_id, opt_vibe, opt_best_season, opt_average_age, opt_average_budget)
        self.exp_name = exp_name
        self.exp_destination = exp_destination
        self.exp_bookings = exp_bookings
        self.exp_info = exp_info

    def __repr__(self):
        return f"Experience(exp_name={self.exp_name})"
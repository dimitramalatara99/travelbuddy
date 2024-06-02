# Classes
class User:
    def __init__(self, u_id, u_email, u_phone):
        self.u_id = u_id
        self.u_email = u_email
        self.u_phone = u_phone


class Traveler(User):
    def __init__(self, u_id, u_email, u_phone, tv_name, tv_last_name, tv_age, tv_hobbies, tv_wallet, tv_tb, tv_friends, tv_authentication):
        super().__init__(u_id, u_email, u_phone)
        self.tv_name = tv_name
        self.tv_last_name = tv_last_name
        self.tv_age = tv_age
        self.tv_hobbies = tv_hobbies
        self.tv_wallet = tv_wallet
        self.tv_tb = tv_tb
        self.tv_friends = tv_friends
        self.tv_authentication = tv_authentication

    def __repr__(self):
        return (f"Traveler(tv_name={self.tv_name}, tv_last_name={self.tv_last_name}, tv_age={self.tv_age}, "
                f"tv_wallet={self.tv_wallet}, tv_tb={self.tv_tb}, tv_friends={self.tv_friends}, tv_authentication={self.tv_authentication})")


class Business(User):
    instances = []

    def __init__(self, u_id, u_email, u_phone, b_name, b_destination, b_bookings):
        super().__init__(u_id, u_email, u_phone)
        self.b_name = b_name
        self.b_destination = b_destination
        self.b_bookings = b_bookings
        Business.instances.append(self)

    def __repr__(self):
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
    _destinations = []

    def __init__(self, opt_id, opt_post_id, opt_vibe, opt_best_season, opt_average_age, opt_average_budget, dst_name):
        super().__init__(opt_id, opt_post_id, opt_vibe, opt_best_season, opt_average_age, opt_average_budget)
        self.dst_name = dst_name

    def __repr__(self):
        return (f"Destination(opt_id={self.opt_id}, opt_post_id={self.opt_post_id}, opt_vibe={self.opt_vibe}, "
                f"opt_best_season={self.opt_best_season}, opt_average_age={self.opt_average_age}, opt_average_budget={self.opt_average_budget}, dst_name={self.dst_name})")


class Experience(Options):

    def __init__(self, opt_id, opt_post_id, opt_vibe, opt_best_season, opt_average_age, opt_average_budget, exp_name, exp_destination, exp_bookings, exp_info):
        super().__init__(opt_id, opt_post_id, opt_vibe, opt_best_season, opt_average_age, opt_average_budget)
        self.exp_name = exp_name
        self.exp_destination = exp_destination
        self.exp_bookings = exp_bookings
        self.exp_info = exp_info

    def __repr__(self):
        return f"Experience(exp_name={self.exp_name})"


class Trip:
    def __init__(self, tr_id, tr_traveler, tr_status, tr_people, tr_date, tr_destination, tr_accommodation, tr_options, tr_phone, tr_advance_pay, tr_payment_type, tr_payment_status):
        self.tr_id = tr_id
        self.tr_traveler = tr_traveler
        self.tr_status = tr_status
        self.tr_people = tr_people
        self.tr_date = tr_date
        self.tr_destination = tr_destination
        self.tr_accommodation = tr_accommodation
        self.tr_options = tr_options
        self.tr_phone = tr_phone
        self.tr_advance_pay = tr_advance_pay
        self.tr_payment_type = tr_payment_type
        self.tr_payment_status = tr_payment_status

    def __repr__(self):
        # Provide a string representation of the object for debugging
        return (f"Trip=(tr_id={self.tr_id}, tr_traveler={self.tr_traveler}, tr_status={self.tr_status}, "
                f"tr_people={self.tr_people}, tr_date={self.tr_date}, tr_destination={self.tr_destination}, "
                f"tr_accommodation={self.tr_accommodation}, tr_options={self.tr_options},tr_phone={self.tr_phone}, "
                f"tr_advance_pay={self.tr_advance_pay}, tr_payment_type ={self.tr_payment_type},tr_payment_status ={self.tr_payment_status})")


class TB:
    def __init__(self, tb_id, tb_status, tb_traveler, tb_dest, tb_min_age, tb_max_age, tb_vibe, tb_request, tb_buddies):
        self.tb_id = tb_id
        self.tb_status = tb_status
        self.tb_traveler = tb_traveler
        self.tb_dest = tb_dest
        self.tb_min_age = tb_min_age
        self.tb_max_age = tb_max_age
        self.tb_vibe = tb_vibe
        self.tb_request = tb_request
        self.tb_buddies = tb_buddies

    def __repr__(self):
        return (f"Business(tb_id={self.tb_id}, tb_status={self.tb_status}, tb_traveler={self.tb_traveler}, "
                f"tb_dest={self.tb_dest}, tb_min_age={self.tb_min_age}, tb_max_age={self.tb_max_age}, "
                f"tb_vibe={self.tb_vibe}, tb_request={self.tb_request}, tb_buddies={self.tb_buddies})")


class Review:
    def __init__(self, r_id, r_options, r_traveler):
        self.r_id = r_id
        self.r_options = r_options
        self.r_traveler = r_traveler


class Wallet:
    def __init__(self, w_id, w_balance):
        self.w_id = w_id
        self.w_balance = w_balance


class Invite:
    def __init__(self, invite_id, invite_type, invite_status):
        self.invite_id = invite_id
        self.invite_type = invite_type
        self.invite_status = invite_status

class User:
    def __init__(self, u_id, u_email, u_phone):
        self.u_id = u_id
        self.u_email = u_email
        self.u_phone = u_phone


class Traveler(User):
    def __init__(self, u_id, u_email, u_phone, tv_name, tv_last_name, tv_age, tv_wallet, tv_tb, tv_friends, tv_authentication):
        super().__init__(u_id, u_email, u_phone)
        self.tv_name = tv_name
        self.tv_last_name = tv_last_name
        self.tv_age = tv_age
        self.tv_wallet = tv_wallet
        self.tv_tb = tv_tb
        self.tv_friends = tv_friends
        self.tv_authentication = tv_authentication


class Business(User):
    instances = []

    def __init__(self, u_id, u_email, u_phone, b_name, b_destination, b_bookings):
        super().__init__(u_id, u_email, u_phone)
        self.b_name = b_name
        self.b_destination = b_destination
        self.b_bookings = b_bookings
        Business.instances.append(self)


class TB:
    def __init__(self, tb_id, tb_status, tb_trip, tb_info, tb_request, tb_buddies):
        self.tb_id = tb_id
        self.tb_status = tb_status
        self.tb_trip = tb_trip
        self.tb_info = tb_info
        self.tb_request = tb_request
        self.tb_buddies = tb_buddies


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


class Trip:
    def __init__(self, tr_id, tr_traveler, tr_status, tr_date, tr_options, tr_phone, tr_advance_pay, tr_payment_type, tr_payment_status):
        self.tr_id = tr_id
        self.tr_traveler = tr_traveler
        self.tr_status = tr_status
        self.tr_date = tr_date
        self.tr_options = tr_options
        self.tr_phone = tr_phone
        self.tr_advance_pay = tr_advance_pay
        self.tr_payment_type = tr_payment_type
        self.tr_payment_status = tr_payment_status


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


class Experience(Options):
    def __init__(self, opt_id, opt_post_id, opt_vibe, opt_best_season, opt_average_age, opt_average_budget, exp_name, exp_destination, exp_bookings):
        super().__init__(opt_id, opt_post_id, opt_vibe, opt_best_season, opt_average_age, opt_average_budget)
        self.exp_name = exp_name
        self.exp_destination = exp_destination
        self.exp_bookings = exp_bookings

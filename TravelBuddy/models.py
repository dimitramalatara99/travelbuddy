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
                f"tr_advance_pay={self.tr_advance_pay}, tr_payment_type ={self.tr_payment_type},tr_payment_status ={self.tr_payment_status}")

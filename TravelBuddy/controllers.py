from dal import CSVController


class BusinessController:
    def __init__(self, dal):
        self.dal = dal

    def get_businesses_by_dest(self, b_dest):
        return self.dal.get_business_by_dest(b_dest)

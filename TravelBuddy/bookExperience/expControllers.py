from expDal import CSVController

class DestinationController:
    def __init__(self,dal):
        self.dal = dal

    def get_all_destinations(self):
        return self.dal.get_all_destinations()

    def get_experiences_by_dest(self, dest_name, filters=None):
        return self.dal.get_experiences_by_dest(dest_name, filters)
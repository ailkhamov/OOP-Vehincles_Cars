from Vehicle import *

class Bike(Vecihle):

    def __init__(self, wheels, capacity, color, year, gears,bask_sign, handle_type = "Automatic"):
        super().__init__(wheels, capacity, color, year)
        self.handle_type = handle_type
        self.gear = gears
        self.bask_sign = bask_sign


    def peddle(self):
        return "You are now peddling"

    def wheely(self):
        return "You are wheelying"

    def chain_it(self):
        return "You have now locked your bike"

    def change_handle_type(self, change):
        self.handle_type = change
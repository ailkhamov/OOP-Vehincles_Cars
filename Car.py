from Vehicle import *

class Car(Vecihle):

    def __init__(self, wheels, capacity, color, year, brand, model, plate, airbag):
        super().__init__(wheels, capacity, color, year)
        self.brand = brand
        self.model = model
        self.plate = plate
        self.airbag = airbag


    def play_music(self):
        return ""

    def horn(self):
        return ""

    def lock_it(self):
        return ""

from Vehcle2 import *

class Car2(Vehicle2):


    def __init__(self,wheels, capacity, color, make, model,plate):
        super().__init__(wheels, capacity, color)
        self.make = make
        self.model = model
        self._accidents = 0  # Visibility is limited
        self.__miles = 0 # Visibility and Acces is restricted
        self.plate = plate

    def make_sound(self):
        return 'Removing my car VRROM'

    def play_music(self, song):
        return "The car is playing a song" + song


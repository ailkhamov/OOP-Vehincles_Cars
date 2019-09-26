class Vecihle ():

    def __init__(self, wheels, capacity, color, year):
        self.wheels = wheels
        self.capactiy = capacity
        self.color = color
        self.year = year


    def accelarate(self):
        return "WHOOOOMMM... CAREFUL YOU MIGHT CRASH!"

    def car_break(self):
        return "Break done"

    def turn(self, option):
        if option == "left":
            return "You have turned left"
        elif option == "right":
            return  "You have turned right"
        else:
            "You have chosen the wrong option"

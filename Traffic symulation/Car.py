class Car:

    def __init__(self, velocity, id):
        self.v = velocity
        self.id = id

    def change_velocity(self, velocity):
        self.v = velocity

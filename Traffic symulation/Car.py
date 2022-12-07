class Car:

    def __init__(self, velocity, id, vehicle_type):
        self.v = velocity
        self.id = id
        self.vehicle_type = vehicle_type

    def change_velocity(self, velocity):
        self.v = velocity

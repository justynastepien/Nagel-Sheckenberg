class Car:

    def __init__(self, velocity, id, vehicle_type):
        self.v = velocity
        self.id = id
        self.vehicle_type = vehicle_type
        self.time = 0

    def change_velocity(self, velocity):
        self.v = velocity

class Bus:

    def __init__(self, velocity, id, vehicle_type):
        self.v = velocity
        self.id = id
        self.vehicle_type = vehicle_type
        self.counter = 0
        self.time = 0

    def change_velocity(self, velocity):
        self.v = velocity

    def change_counter(self, i):
        self.counter = i

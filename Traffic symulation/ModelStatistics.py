class ModelStatistics():
    def __init__(self):
        self.total_cars = 0
        self.total_buses = 0
        self.time_cars = 0
        self.time_buses = 0

    def add_car(self, time):
        self.time_cars += time
        self.total_cars += 1

    def add_bus(self, time):
        self.time_buses += time
        self.total_buses += 1

    def get_avg_car(self) -> float:
        if self.total_cars == 0:
            return 0
        return self.time_cars/self.total_cars
    
    def get_avg_bus(self) -> float:
        if self.total_buses == 0:
            return 0
        return self.time_buses/self.total_buses

stats = ModelStatistics()
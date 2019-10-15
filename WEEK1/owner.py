from car import Car

class Owner(Car):
    def __init__(self,car_data):
        Car.__init__(self,car_data)  #super().__init__(slef)
        self.car_data = car_data
    def ownerinformation(self):
        return f'The owner is {self.car_data[0]["owner_name"]}'


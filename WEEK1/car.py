class Car:
    def __init__(self,car_data):
        self.color = car_data[0]["car_color"]  #オブジェクト
        self.brand = car_data[0]["car_name"]
        self.speedlimit = car_data[0]["speed_limit"]
        self.speed = 0
        self.fuellimit = car_data[0]["fuel_limit"]
        self.fuel = 0
    def information(self):
        return f"color: {self.color} brand: {self.brand}"
    def startUp(self):
        self.speed += 1
        return f"Car is Starting and Speed is now {self.speed}"
    def speedUp(self):
        if self.speed > 0 and self.fuel > 0:
            self.speed += 30
            self.fuel -= 1
            if self.speed > self.speedlimit:
                self.speed = self.speedlimit
                return f"Speed is now {self.speed}"
            else:
                return f"Speed is now {self.speed}"
        else:
            return f"Please startup before speedup or fuel is nothing. Speed is now {self.speed}. Fuel is now {self.fuel}"
    def speedDown(self):
        if self.speed > 0 and self.fuel > 0:
            self.speed -= 30
            self.fuel -= 1
            if self.speed < 0:
                self.speed = 0
                return f" Speed is now {self.speed}.It's Stopped."
            else:
                return f"Speed is now {self.speed}"
        else:
            return f"Please startup before speeddown or fuel is nothing. Speed is now {self.speed}. Fuel is now {self.fuel}"
    def fuelUp(self):
        self.fuel =self.fuellimit
        return f"Fuel is full.it is {self.fuel}"
    def stop(self):
        self.speed =0
        return "Car is stopped."



# Car1 = Car("red","Toyota",200,20) #インスタンス
# Car2 = Car("black","Ferrari",280,25)


# def f(x=2):
#     y = x**2 + x*3 +2
#     print(y)

# number = int(input("enter a number:"))
# f(number)

# def add(x, y):
#     return x+y

# num1 = int(input("enter 1st number:"))
# num2 = int(input("enter 2nd number:"))

# answer = add(num1, num2)
# print(f"the answer is {answer}.")

"""
function for 
subtract
multiply
divide
"""

# def subtract(x,y):
#     return x-y

# def multiply(x,y):
#     return x*y

# def divide(x,y):
#     return x/y


# num1 = int(input("enter 1st number:"))
# num2 = int(input("enter 2nd number:"))

# sub = subtract(num1, num2)
# mul = multiply(num1, num2)
# # div = divide(num1, num2)


# # print(f"substract is {sub}")
# # print(f"multiply is {mul}")
# # print(f"divide is {div}")

# time = input("is it time after 15:00? yes/no:")
# name = input("What do you buy?:")
# num = int(input("How many do you buy it?:"))
# price = int(input("How much is it?"))

# def sum(x,y,z):
#     sum_pri = x * y * z
#     print(f"Total amount of {name} is {sum_pri}.")


# if time == "yes":
#     if num > 5:
#         sum(num,price,0.8)
#     elif num <=5 and num >= 1:
#         sum(num,price,0.9)
#     else:
#         print("number is error:(")
# elif time == "no":
#     if num > 5:
#         sum(num,price,0.9)
#     elif num <=5 and num >= 1:
#         sum(num,price,1)
#     else:
#         print("number is error:(")
# else:
#     print("time is error:(")

import os

class Car:
    def __init__(self,car,brand,speedlimit,fuellimit):
        self.color = car  #オブジェクト
        self.brand = brand
        self.speedlimit = speedlimit
        self.speed = 0
        self.fuellimit = fuellimit
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
            return "Please startup before speedup or fuel is nothing"
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
            return "Please startup before speeddown or fuel is nothing"
    def fuelUp(self):
        self.fuel =self.fuellimit
        return f"Fuel is full.it is {self.fuel}"
    def stop(self):
        self.speed =0
        return "Car is stopped."



Car1 = Car("red","Toyota",200,20) #インスタンス
Car2 = Car("black","Ferrari",280,25)

# print(Car2.information())
# print(Car2.startUp())
# print(Car2.speedUp())

while True:
    print("Welcome to My Car")
    print(" [1]information")
    print(" [2]startup")
    print(" [3]speedup")
    print(" [4]speeddown")
    print(" [5]fuelup")
    print(" [6]stop")
    print(" [0]stop and exit")
    choice = int(input("Make Your Choice"))

    if choice ==1:
        os.system("clear")
        print(Car2.information())
        continue
    elif choice ==2:
        os.system("clear")
        print(Car2.startUp())
        continue
    elif choice ==3:
        os.system("clear")
        print(Car2.speedUp())
        continue
    elif choice ==4:
        os.system("clear")
        print(Car2.speedDown())
        continue
    elif choice ==5:
        os.system("clear")
        print(Car2.fuelUp())
        continue
    elif choice ==6:
        os.system("clear")
        print(Car2.stop())
        continue
    if choice ==0:
        os.system("clear")
        break
    else:
        break
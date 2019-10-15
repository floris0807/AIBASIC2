# class Car:
#     def __init__(self):
#         self.__engine_code = "test"
#         self.engine_code_pub = "test"

#     def setEngineCode(self,engine_code):
#         self.__engine_code = engine_code
#     def getEngineCode(self):
#         return self.__engine_code

# car1 = Car()
# car1.engine_code_pub = "XXXc124"
# car1.__engine_code = "XXXc124"  

# # print(car1.engine_code_pub)
# # print(car1.__engine_code)

# print(car1.getEngineCode())
# car1.setEngineCode("XXXc222")
# car1.__engine_code = "XXXc124" 
# print(car1.getEngineCode())
# print(car1.__engine_code)
# car1.setEngineCode("XXXc333")

# class Car:
#     def __init__(self,car_data):
#         self.__engine_code = "test"
#         self.engine_code_pub = "test"
#         self.car_data = car_data
#         self.speed = 0
#         self.speed_limit = 0


#     def setEngineCode(self,engine_code):
#         self.__engine_code = engine_code
#     def getEngineCode(self):
#         return self.__engine_code
#     # def information(self):
#     #     return self.car_data[0]["car_name"]

import os


from owner import Owner



car_data = [
    {"owner_id":1,"car_name":"Ferrari","car_color":"red","owner_name":"Jan","speed_limit":200,"fuel_limit":30}
]

Owner1 = Owner(car_data)
# print(onwer1.ownerinformation())






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
        print(Owner1.ownerinformation())
        continue
    elif choice ==2:
        os.system("clear")
        print(Owner1.startUp())
        continue
    elif choice ==3:
        os.system("clear")
        print(Owner1.speedUp())
        continue
    elif choice ==4:
        os.system("clear")
        print(Owner1.speedDown())
        continue
    elif choice ==5:
        os.system("clear")
        print(Owner1.fuelUp())
        continue
    elif choice ==6:
        os.system("clear")
        print(Owner1.stop())
        continue
    if choice ==0:
        os.system("clear")
        break
    else:
        break
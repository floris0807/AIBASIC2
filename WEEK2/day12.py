# import math as mt
# import statistics as st

# x =  mt.pow(2,3.5)

# print(x)

# y = [1,2,3,4,5,6,7,8,8,8]

# print(st.median(y))

# from model import model

# from model.model import module1 as hll

# print(hll())



import csv


# # datas = open("data/book.csv","r")
# # print(datas)

# header = []
# body = []


# with open("data/book.csv","r") as rf:
#     reader = csv.reader(rf)
#     header = next(reader)
#     # print(header)
#     # print(next(reader))

#     for row in reader:
#         # print(row)
#         body.append(row)

# name = input("Enter the book Name :")
# author = input("Enter the Author :")
# isbn = input("Enter isbn :")
# body.append([len(body)+1,name,author,isbn])


# # header = ["id","name","author","isbn"]
# # body = [
# #     ["1","python101","jan","1233456"],
# #     ["2","python102","jan","3571456"],
# # ]

# with open("data/book.csv","w") as wf:
#     writer = csv.writer(wf)
#     writer.writerow(header)
#     writer.writerows(body)


import model.model as mdl

data1 = mdl.readdata("data/book.csv")

# data1 = [
#     [4,"python101","jan",1233456],
#     [5,"python102","jan",3571456],
#     [6,"ad","ds",123]
# ]
# data1 = [4,"new","data",1233456]

path = input("Enter the path :")
name = input("Enter the book Name :")
author = input("Enter the Author :")
isbn = input("Enter isbn :")
data1.append([len(data1)+1,name,author,isbn])

mdl.writedata(path,data1)


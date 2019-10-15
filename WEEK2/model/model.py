# def module1():
#     return "Hello World"

# def module2():
#     return "Good Bye"

import csv

def readdata(path):
    with open(path,"r") as rf:
        book_data = []
        reader = csv.reader(rf)
        for row in reader:
            book_data.append(row)
        return book_data








def writedata(path,data):

    with open(path,"w") as wf:
        writer = csv.writer(wf)
        writer.writerows(data)
    return True






# Arithmetics Operetor

# print(2 * "3")
# >str
"""
print(11//3)
商

if 3 == 3:
    print("yes")

"===???????????????????

x=[1,2,3,4,5]
print( 2 in x)

print((3 == 3 or 3 >= 4) or not( 4 > 5 and 5 > 10))

name = input("What is your name:")
age = int(input("How are you?"))
# print("Hi {} you are already {}?".format(name, age))
print(f"HI {name} you are already {age}")
"""

# word = "Lorem Ipsum Dolor"
# print(word[:-5])
# >Lorem Ipsum_
# print(len(word))

# word[0] = "G"
# >cannot

# print(word.split(" "))
# >['Lorem', 'Ipsum', 'Dolor']

# word= ["I am","jan","cebu"]
# print("/".join(word))

# word = "Lorem Ipsum Dolor"
# new_word = word.replace("o","a")

# if


"""
You will ask the user for his/her age:
first if the age is less than 18
 you are underage
if age is greaterthan or equal 18
 you are in legal age
if age is greaterthan or equal 60 but not greaterthan 120
 you are in Senior age
else
 age is invalid or you are not a human
"""

# age = int(input("How old are you?:"))

# if age < 18 and age >= 0:
#     print("you are underage")
# elif age >= 18 and age < 60:
#     print("you are in legal age")
# elif age >= 60 and age <= 120:
#     print("you are in Senior age")
# else:
#     print("age is invalid or you are not a human")

# print(range(1,10))
# for i in range(1, 10):
    # print(i)
# >~19

# count = 20
# for i in range(1, count+1):
#     if i%2 != 0:
#         print(f"odd number{i}")
#     else:
#         print(f"even number {i}")

students = ["Taka","Hiro","Ayaka"]

# for student in students:
#     print(student)

# for i,student in enumerate(students):
#     print(f"[{i}]{student}")

# x = 0
# while x <= 10:
#     print(x)
#     x += 1

# while True:
#     answer = input("input x to break and c to continue")
#     if answer == "c":
#         count = input("enter a number")
#         for i in range(1,int(count)+1): #intにするのを忘れずに
#             print(i)
#         continue
#     else:
#         print("stopped")
#         break

# numbers = [i*2 for i in range(1,10) if i%2==0]
# print(numbers)

i = 1
while i <= 5:
    if i !=3:
        print(i)
    i += 1
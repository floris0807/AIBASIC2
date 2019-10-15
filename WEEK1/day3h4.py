a = 0
b = 1
i = 1
n = int(input("enter a number:"))
if n == 1:
    print(a)
elif n == 2:
    print(b)
elif n >= 3:
    while i <= n-2:
        c = a + b
        a = b
        b = c
        i += 1
    print(c)
else:
    print("number is unvalid")

a = 0
b = 1
i = 1
n = int(input("enter a number:"))
if n == 1:
    print(a)
elif n == 2:
    print(b)
elif n >= 3:
    while i <= n-2:
        c = a + b
        a = b
        b = c
        i += 1
    print(c)
else:
    print("number is unvalid")

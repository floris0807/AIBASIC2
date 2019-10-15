import random

money = 0

def roulette():
    a = random.randint(0,36)
    return a
    

def run(money1):
    num = roulette()
    if num >= 1 and num <= 18:
        return [money1, 1]
    else:
        money1 = -1 * money1
        return [money1, 0]


def method31():
    routine = [1,1,1,2,2,4,4,8,8]
    result = [0,0,0,0,0,0,0,0,0]
    num = 0
    money = 0
    while (result[num] == 0 or result[num-1] == 0) or num != 8 :
        money1,count1 = run(routine[num])
        result[num] = count1
        money += money1
        num += 1
    print(money)


play = method31()

print(play)
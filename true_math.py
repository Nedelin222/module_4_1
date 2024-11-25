import math
def divide(first, second):
    #a = int(first) / int(second)
    # input(float(first))
    # input(float(second))
    if second == 0:
        print(math.inf)
    else:
        a = float(first) / float(second)
        print(a)
        return (a)

#divide(float(input('first: ')), float(input('second: ')))

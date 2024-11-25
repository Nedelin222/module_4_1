def divide(first, second):
    #a = int(first) / int(second)
    # input(float(first))
    # input(float(second))
    if second == 0:
        print("Ошибка")
    else:
        a = int(first) / float(second)
        print(a)
        return (a)

#divide(float(input('first: ')), float(input('second: ')))

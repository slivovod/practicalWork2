x = int(input())
y = int(input())

if(x >= 0 and y >= 0):
    print("x и y положительные числа")
elif(x < 0 and y < 0):
    print("x и y отрицательные числа")
elif(x < 0 and y >= 0):
    print("x отрицательное число, y - положительное")
elif(x >= 0 and y < 0):
    print("x положительное число, y - отрицательное")

if((x >= 0 and y >= 0) or (x < 0 and y < 0)):
    print("x и y имеют один знак")
elif((x >= 0 and y < 0) or (x < 0 and y >= 0)):
    print("x и y имеют разные знаки")
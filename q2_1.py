x1 = float(input())
y1 = float(input())
x2 = float(input())
y2 = float(input())

l = ((x2 - x1)**2 + (y2 - y1)**2)**0.5

#if(x2 - x1 == 0):
try:
    slope = (y2 - y1) / (x2 - x1)
except:
    slope = 0

isSameLine = False
if((x1 == x2 and x1 == 0) or (y1 == y2 and y1 == 0)): #недеюсь правильно понял, что требуется найти
    isSameLine = True
isPoint1Above = False
if(y1 > y2):
    isPoint1Above = True

quadrantPoint1 = 0
if(x1 > 0 and y1 > 0):
    quadrantPoint1 = 1
elif(x1 < 0 and y1 > 0):
    quadrantPoint1 = 2
elif(x1 < 0 and y1 < 0):
    quadrantPoint1 = 3
elif(x1 > 0 and y1 < 0):
    quadrantPoint1 = 4


quadrantPoint2 = 0
if(x2 > 0 and y2 > 0):
    quadrantPoint2 = 1
elif(x2 < 0 and y2 > 0):
    quadrantPoint2 = 2
elif(x2 < 0 and y2 < 0):
    quadrantPoint2 = 3
elif(x2 > 0 and y2 < 0):
    quadrantPoint2 = 4


print("Расстояние между точками: ", l)
print("Угловой коэффициент равен: ", slope)
if(isSameLine):
    print("Обе точки находятся на одной оси")
if(isPoint1Above):
    print("Точка 1 выше, чем точка 2")
else:
    print("Точка 1 не выше, чем точка 2")

if(quadrantPoint1 == 0):
    print("Точка 1 лежит в начале координат")
else:
    print("Точка 1 находится в ", quadrantPoint1, " четверти")

if(quadrantPoint1 == quadrantPoint2 and quadrantPoint1 == 0):
    print("Обе точки лежат в начале координат")
elif(quadrantPoint1 == quadrantPoint2):
    print("Обе точки лежат в одной четверти ", "(", quadrantPoint1, ")")
else:
    print("Точки расположены в разных четвертях:")
    print("Первая(1) точка в ", quadrantPoint1, ", а вторая(2) в ", quadrantPoint2, " четверти")
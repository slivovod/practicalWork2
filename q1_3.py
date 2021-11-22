x = int(input())
y = int(input())
z = int(input())

if(x == y and y == z):
    print("x, y, z равны между собой")
elif((x == y and y != z) or (x == z and z != y) or (y == z and z != x)):
    print("Одна из переменных не равна другим")
else:
    print("x, y, z разные числа")

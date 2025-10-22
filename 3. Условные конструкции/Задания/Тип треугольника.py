a = int(input())
b = int(input())
c = int(input())
h = max(a, b, c)
c1= min(a, b, c)
c2= (a + b + c) - (h + c1)
if c1 + c2 <= h:
    print (f'Не существует')
elif c1**2 + c2**2 == h**2:
    print(f'Прямоугольный')
elif c1**2 + c2**2 > h**2:
    print(f'Остроугольный')
else:
    print(f'Тупоугольный')
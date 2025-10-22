x1 = int(input())
y1 = int(input())
x2 = int(input())
y2 = int(input())
if ((x1 - x2) == (y1 - y2)):
    print(f'YES')
elif ((x1 - x2) == (y2 - y1)):
    print(f'YES')
else:
    print(f'NO')
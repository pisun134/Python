x1 = int(input())
y1 = int(input())
x2 = int(input())
y2 = int(input())
if abs(x2 - x1) <= 1 and abs (y2 - y1) <= 1 and not (x1 == x2 and y1 == y1):
    print(f'YES')
else:
    print(f'NO')
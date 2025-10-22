a = int(input())
if a % 10 == 1 and a % 100 != 11:
    print(f'гриб')
elif 2 <= a % 10 <= 4 and 12 < a % 100 > 14:
    print(f'гриба')
else:
    print(f'грибов')
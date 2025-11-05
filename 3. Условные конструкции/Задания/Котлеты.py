k=int(input())
m=int(input())
n=int(input())
if n <= k:
    print(m * 2)
elif 2 * n % k == 0:
    print(2 * n // k * m)
else:
    print((( 2 * n // k + 1) * m ))
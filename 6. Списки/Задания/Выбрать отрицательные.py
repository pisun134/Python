nums = list(map(int,input().split()))
nums = [ n for n in nums if n < 0]
print(*nums)
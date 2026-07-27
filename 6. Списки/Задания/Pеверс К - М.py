n = int(input())
nums = list(map(int,input().split()))
k, m = list(map(int,input().split()))
before = nums[:k - 1]
mid = nums[k - 1:m]
after = nums[m::]
reversed = mid[::-1]
p = before + reversed + after
print(*p)
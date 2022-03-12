import sys
n,k=map(int,input().split())
nums=[]

#한 줄에 여러개 입력
nums = [int(x) for x in input().split()]

nums.sort()

print(nums[k-1])

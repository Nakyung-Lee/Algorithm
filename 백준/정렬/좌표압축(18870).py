from collections import Counter
import sys

N = int(input())

dic={}

nums = list(map(int, sys.stdin.readline().split()))

num = list(sorted(set(nums)))

'''
시간초과 오류 

for i in range(N):
    cnt=0
    for j in range(len(num)):
        if nums[i]>num[j]:
            cnt+=1
    dic[nums[i]]=cnt
'''

# 리스트안에서 자기보다 작은 숫자의 개수를 세는 것이므로, 자신이 리스트 안에서의 크기 순서를 출력하면 된다는 아이디어
# 시간초과 해결

for i in range(len(num)):
    dic[num[i]]=i
    
for i in nums:
    print(dic[i],end=' ')

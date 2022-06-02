from collections import Counter
import sys

N = int(sys.stdin.readline())

nums=[]

for i in range(N):
    nums.append(int(sys.stdin.readline()))

print(int(round(sum(nums)/N,0)))
print(sorted(nums)[N//2])
nums = sorted(nums)
cnt = Counter(nums)
if N!=1 and cnt.most_common(2)[0][1] == cnt.most_common(2)[1][1]:
    print(cnt.most_common(2)[1][0])
else:
    print(cnt.most_common(1)[0][0])
print(nums[-1]-nums[0])

                

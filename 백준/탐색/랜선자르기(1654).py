import sys

K, N = map(int,sys.stdin.readline().split())

arr=[]
for i in range(K):
    arr.append(int(input()))

max_ = max(arr)
min_ = 1

while (min_ <= max_):
    mid_ = (min_+max_)//2
    cnt=0
    for i in arr:
        cnt += i // mid_
    if cnt >= N:
        #길이 더 길게
        min_ = mid_ + 1
    else:
        #길이 더 짧게
        max_ = mid_ - 1


print(max_)

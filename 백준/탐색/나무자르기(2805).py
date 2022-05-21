import sys

K, N = map(int,sys.stdin.readline().split())

arr = list(map(int,sys.stdin.readline().split()))

max_ = max(arr)
min_ = 1

while (min_ <= max_):
    mid_ = (min_+max_)//2
    length=0
    for i in arr:
        if i > mid_:
            length += i - mid_
            if length > N:
                break
    if length >= N:
        min_ = mid_ + 1
    else:
        max_ = mid_ - 1


print(max_)

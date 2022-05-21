import sys
from collections import Counter

N= int(input())

arr_n = list(map(int,sys.stdin.readline().split()))

M= int(input())

arr_m = list(map(int,sys.stdin.readline().split()))

arr = Counter(arr_n)

for i in arr_m:
    print(arr[i],end=' ')


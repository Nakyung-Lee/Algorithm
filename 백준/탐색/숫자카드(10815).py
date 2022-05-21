import sys

N= int(input())

arr_n = set(map(int,sys.stdin.readline().split()))

M= int(input())

arr_m = list(map(int,sys.stdin.readline().split()))

for i in range(M):
    if arr_m[i] in arr_n:
        print(1,end=' ')
    else:
        print(0,end=' ')

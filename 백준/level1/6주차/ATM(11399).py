import sys

N=int(input())

p=list(map(int, input().split()))

p.sort()

sumn=0
for i in range(N):
    sumn+=sum(p[:i+1])
print(sumn)

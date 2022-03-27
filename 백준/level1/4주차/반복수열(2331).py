import sys

n,m=map(int, sys.stdin.readline().split())
nn=n

s=[]

s.append(n)

while True:
    num=0
    while n>0:
        num+=(n%10)**m
        n=n//10
    if num in s:
        idx=s.index(num)
        s=s[:idx]
        break
    n=num
    s.append(n)
    print(s)
    
print(len(s))

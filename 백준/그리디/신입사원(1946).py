import sys
N=int(input())


for i in range(N):
    n=int(input())
    cnt=1
    
    s=[list(map(int,sys.stdin.readline().split())) for _ in range(n)]

    s.sort()

    tmp = s[0][1]
    
    for j in range(n):
        if s[j][1] < tmp:
            cnt+=1
            tmp=s[j][1]
    print(cnt)

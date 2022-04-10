import sys

N,K=map(int, sys.stdin.readline().split())


p=[int(input()) for _ in range(N)]


#print(p)

cnt=0

cm=0

for i in range(N-1,-1,-1):
    j=1
    if p[i] <= K and cm + p[i]<=K:
        j=(K-cm)//p[i]
        cm+=p[i]*j
        cnt+=j
    #print(cm,K, p[i],cnt)
print(cnt)

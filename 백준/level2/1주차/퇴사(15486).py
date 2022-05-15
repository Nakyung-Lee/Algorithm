import sys

N=int(input())
d=[]
v=[]
dp=[0]*(N+1)
for i in range(N):
    a=list(map(int,sys.stdin.readline().split()))
    d.append(a[0])
    v.append(a[1])

for i in range(N):
    if d[i]<=N-i:
        if dp[i+d[i]]< dp[i]+v[i]:
            dp[i+d[i]]= dp[i]+v[i]
    dp[i+1]=max(dp[i+1],dp[i])
print(max(dp))

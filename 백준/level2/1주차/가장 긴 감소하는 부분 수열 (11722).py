N=int(input())

p=list(map(int, input().split()))

l=1

dp=[1 for i in range(N)]

for i in range(N):
    for j in range(i):
        if p[i]<p[j] and dp[i]<=dp[j]:
            dp[i]=dp[j]+1

print(max(dp))
    

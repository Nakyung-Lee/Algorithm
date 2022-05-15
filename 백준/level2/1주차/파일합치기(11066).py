import sys

n=int(input())
for i in range(n):
    N=int(sys.stdin.readline())
    arr=list(map(int,sys.stdin.readline().split()))
    dp=[[0]* N for i in range(N)]
    for j in range(1,N):
        for i in range(j-1,-1,-1):
            mm=float('inf')
            for k in range(j-i):
                mm=min(mm,dp[i][i+k]+dp[i+k+1][j])
            dp[i][j]=mm+sum(arr[i:j+1])
    print(dp[0][N-1])   

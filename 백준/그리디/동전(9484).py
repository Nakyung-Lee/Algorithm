import sys

T=int(input())

for i in range(T):
    N=int(input())
    coins = list(map(int,sys.stdin.readline().split()))
    M = int(input())
    dp = [0 for _ in range (M+1)]
    dp[0]=1
    for coin in coins:
        for j in range (1,M+1):
            if j-coin>=0:
                dp[j]+=dp[j-coin]
    print(dp[M])

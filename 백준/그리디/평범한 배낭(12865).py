import sys

N,K = map(int,sys.stdin.readline().split())

weight=[]
value=[]
for i in range(1,N+1):
    w = list(map(int,sys.stdin.readline().split()))
    weight.append(w[0])
    value.append(w[1])
    
dp = [[0]*(K+1) for _ in range(N+1)]


for i in range(1,N+1):
    #가방에 담을 수 있는 최대 무게를 1부터 차례대로 증가시켜 나가면서
    #j : 가방에 담을 수 있는 무게
    for j in range(1,K+1):
        #현재 물건이 가방에 담을 수 있는 무게보다 작으면
        if weight[i-1]<= j:
            #현재 물건을 넣지 않았을때, 현재 물건 넣었을때 가치 비교
            dp[i][j]=max(dp[i-1][j],dp[i-1][j-weight[i-1]]+value[i-1])
        else:
            dp[i][j]=dp[i-1][j]

print(dp[N][K])        
